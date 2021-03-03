#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Sample Python script to call GAM

import gam

if __name__ == '__main__':
  gam.initializeLogging()
  # Issue command, output goes to stdout/stderr
  rc = gam.CallGAMCommand(['gam', 'info', 'domain'])
  # Issue command, redirect stdout/stderr
  rc = gam.CallGAMCommand(['gam', 'redirect', 'stdout', 'domain.txt', 'redirect', 'stderr', 'stdout', 'info', 'domain'])
