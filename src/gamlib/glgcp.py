# -*- coding: utf-8 -*-

# Copyright (C) 2019 Ross Scroggs All Rights Reserved.
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""GAM GCP resources

"""
#
CANT_MODIFY_FINISHED_JOB = 'Can\'t modify the finished job.'
FAILED_TO_SHARE_THE_PRINTER = 'Failed to share the printer.'
NO_PRINT_JOBS = 'No print job available on specified printer.'
UNKNOWN_JOB_ID = 'Unknown job id.'
UNKNOWN_PRINTER = 'Unknown printer.'
USER_IS_NOT_AUTHORIZED = 'User is not authorized.'
class cantModifyFinishedJob(Exception):
  pass
class failedToShareThePrinter(Exception):
  pass
class noPrintJobs(Exception):
  pass
class unknownJobId(Exception):
  pass
class unknownPrinter(Exception):
  pass
class userIsNotAuthorized(Exception):
  pass
#
MESSAGE_EXCEPTION_MAP = {
  CANT_MODIFY_FINISHED_JOB: cantModifyFinishedJob,
  FAILED_TO_SHARE_THE_PRINTER: failedToShareThePrinter,
  NO_PRINT_JOBS: noPrintJobs,
  UNKNOWN_JOB_ID: unknownJobId,
  UNKNOWN_PRINTER: unknownPrinter,
  USER_IS_NOT_AUTHORIZED: userIsNotAuthorized,
  }
