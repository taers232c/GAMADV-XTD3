#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Sample Python script to call GAM"""

import multiprocessing
import sys

from gam import initializeLogging
from gam import CallGAMCommand

if __name__ == '__main__':
# One time initialization
  if sys.platform == 'darwin':
    multiprocessing.set_start_method('fork')
  initializeLogging()
#
  CallGAMCommand(['gam', 'version'])
  # Issue command, output goes to stdout/stderr
  rc = CallGAMCommand(['gam', 'select', 'Aurora', 'info', 'domain'])
  # Issue command, redirect stdout/stderr
  rc = CallGAMCommand(['gam', 'redirect', 'stdout', 'domain.txt', 'redirect', 'stderr', 'stdout', 'info', 'domain'])
