"""update version string during build"""
#=============================================================================
# imports
#=============================================================================
from __future__ import absolute_import, division, print_function
# core
import datetime
from distutils.dist import Distribution
import os
import re
import subprocess
import time
# pkg
# local
__all__ = [
    "stamp_source",
    "stamp_distutils_output",
    "append_hg_revision",
    "as_bool",
]
#=============================================================================
# helpers
#=============================================================================
def get_command_class(opts, name):
    return opts['cmdclass'].get(name) or Distribution().get_command_class(name)

def get_command_options(opts, command):
    return opts.setdefault("options", {}).setdefault(command, {})

def set_command_options(opts, command, **kwds):
    get_command_options(opts, command).update(kwds)

def _get_file(path):
    with open(path, "r") as fh:
        return fh.read()


def _replace_file(path, content, dry_run=False):
    if dry_run:
        return
    if os.path.exists(path):
        # sdist likes to use hardlinks, have to remove them first,
        # or we modify *source* file
        os.unlink(path)
    with open(path, "w") as fh:
        fh.write(content)


def stamp_source(base_dir, version, dry_run=False):
    """
    update version info in passlib source
    """
    #
    # update version string in toplevel package source
    #
    path = os.path.join(base_dir, "passlib", "__init__.py")
    content = _get_file(path)
    content, count = re.subn('(?m)^__version__\s*=.*$',
                    '__version__ = ' + repr(version),
                    content)
    assert count == 1, "failed to replace version string"
    _replace_file(path, content, dry_run=dry_run)

    #
    # update flag in setup.py
    # (not present when called from bdist_wheel, etc)
    #
    path = os.path.join(base_dir, "setup.py")
    if os.path.exists(path):
        content = _get_file(path)
        content, count = re.subn('(?m)^stamp_build\s*=.*$',
                        'stamp_build = False', content)
        assert count == 1, "failed to update 'stamp_build' flag"
        _replace_file(path, content, dry_run=dry_run)


def stamp_distutils_output(opts, version):

    # subclass buildpy to update version string in source
    _build_py = get_command_class(opts, "build_py")
    class build_py(_build_py):
        def build_packages(self):
            _build_py.build_packages(self)
            stamp_source(self.build_lib, version, self.dry_run)
    opts['cmdclass']['build_py'] = build_py

    # subclass sdist to do same thing
    _sdist = get_command_class(opts, "sdist")
    class sdist(_sdist):
        def make_release_tree(self, base_dir, files):
            _sdist.make_release_tree(self, base_dir, files)
            stamp_source(base_dir, version, self.dry_run)
    opts['cmdclass']['sdist'] = sdist


def as_bool(value):
    return (value or "").lower() in "yes y true t 1".split()


def append_hg_revision(version):

    # call HG via subprocess
    # NOTE: for py26 compat, using Popen() instead of check_output()
    try:
        proc = subprocess.Popen(["hg", "tip", "--template", "{date(date, '%Y%m%d%H%M%S')}+hg.{node|short}"],
                                stdout=subprocess.PIPE)
        stamp, _ = proc.communicate()
        if proc.returncode:
            raise subprocess.CalledProcessError(1, [])
        stamp = stamp.decode("ascii")
    except (OSError, subprocess.CalledProcessError):
        # fallback - just use build date
        now = int(os.environ.get('SOURCE_DATE_EPOCH') or time.time())
        build_date = datetime.datetime.utcfromtimestamp(now)
        stamp = build_date.strftime("%Y%m%d%H%M%S")

    # modify version
    if version.endswith((".dev0", ".post0")):
        version = version[:-1] + stamp
    else:
        version += ".post" + stamp

    return version

def install_build_py_exclude(opts):

    _build_py = get_command_class(opts, "build_py")

    class build_py(_build_py):

        user_options = _build_py.user_options + [
            ("exclude-packages=", None,
                "exclude packages from builds"),
        ]

        exclude_packages = None

        def finalize_options(self):
            _build_py.finalize_options(self)
            target = self.packages
            for package in self.exclude_packages or []:
                if package in target:
                    target.remove(package)

    opts['cmdclass']['build_py'] = build_py

#=============================================================================
# eof
#=============================================================================
