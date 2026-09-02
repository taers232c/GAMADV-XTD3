#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# GAM
#
# Copyright 2023, All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import multiprocessing
import platform
import sys
import tempfile
import time
from pathlib import Path

import gam

# How old (in seconds) a leftover PyInstaller onefile extraction folder must
# be before we consider it abandoned and safe to remove. One hour comfortably
# exceeds the runtime of any single GAM invocation, so a folder still around
# after that was left behind by a run that crashed, was killed, or otherwise
# never reached PyInstaller's normal exit-time cleanup.
_STALE_TEMP_DIR_AGE_SECONDS = 60 * 60


def cleanup_stale_pyinstaller_temp_dirs():
  """Remove leftover _MEI* extraction folders from earlier GAM runs.

  PyInstaller's --onefile bootloader extracts the bundled application to a
  uniquely named _MEI* folder under the system temp directory on every run,
  and normally deletes it on clean exit. If a run is killed, crashes, or has
  a file locked (e.g. by antivirus) during that cleanup, the folder is left
  behind. Because GAM is frequently invoked many times in a row by scripts
  and automation, these orphaned folders can accumulate into tens of
  gigabytes over time (see GAM issue #460).

  This is a best-effort self-healing step, not a guarantee: it only runs
  when GAM is a frozen PyInstaller build, only touches folders matching the
  bootloader's own naming pattern, only removes ones old enough that they
  cannot belong to a run still in progress, and never raises - a failure
  here must never prevent GAM from doing the work the user actually asked
  for.
  """
  # sys._MEIPASS only exists in a frozen PyInstaller onefile build; a normal
  # `python -m gam` or `gam.py` invocation has nothing to clean up.
  current_extraction_dir = getattr(sys, '_MEIPASS', None)
  if not current_extraction_dir:
    return

  try:
    temp_root = Path(tempfile.gettempdir())
    current_extraction_dir = Path(current_extraction_dir).resolve()
    now = time.time()
    for candidate in temp_root.glob('_MEI*'):
      try:
        if candidate.resolve() == current_extraction_dir:
          continue
        if not candidate.is_dir():
          continue
        age_seconds = now - candidate.stat().st_mtime
        if age_seconds < _STALE_TEMP_DIR_AGE_SECONDS:
          continue
        _remove_dir_tree(candidate)
      except OSError:
        # Another process may be using it, or we may lack permissions.
        # Skip it and move on; it will be retried on a future run.
        continue
  except OSError:
    # Anything unexpected here (unreadable temp dir, etc.) should never
    # block GAM from running its actual command.
    pass


def _remove_dir_tree(path):
  import shutil
  shutil.rmtree(path, ignore_errors=True)


def main():
  cleanup_stale_pyinstaller_temp_dirs()
  gam.initializeLogging()
  rc = gam.ProcessGAMCommand(sys.argv)
  try:
    sys.stdout.flush()
  except (IOError, ValueError):
    pass
  sys.exit(rc)

# Run from command line
if __name__ == '__main__':
  if platform.system() != 'Linux':
    multiprocessing.freeze_support()
    multiprocessing.set_start_method('spawn')
  main()