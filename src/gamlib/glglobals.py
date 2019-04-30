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

"""GAM global variables

"""

import os

# The following GM_XXX constants are arbitrary but must be unique
# Most errors print a message and bail out with a return code
# Some commands want to set a non-zero return code but not bail
SYSEXITRC = 'sxrc'
# Process ID
PID = 'pid '
# Path to gam
GAM_PATH = 'gpth'
# Are we on Windows?
WINDOWS = 'wndo'
# Encodings
SYS_ENCODING = 'syen'
# Extra arguments to pass to GAPI functions
EXTRA_ARGS_LIST = 'exad'
# GAM admin user
ADMIN = 'admin'
# Current API services
CURRENT_API_SERVICES = 'caps'
# Current Client API
CURRENT_CLIENT_API = 'ccap'
# Current Client API scopes
CURRENT_CLIENT_API_SCOPES = 'ccas'
# Current Service Account API
CURRENT_SVCACCT_API = 'csap'
# Current Service Account API scopes
CURRENT_SVCACCT_API_SCOPES = 'csas'
# Current Service Account user
CURRENT_SVCACCT_USER = 'csa'
# Values retrieved from oauth2.txt
OAUTH2_CLIENT_ID = 'oaci'
# Values retrieved from oauth2service.json
OAUTH2SERVICE_JSON_DATA = 'osjd'
OAUTH2SERVICE_CLIENT_ID = 'osci'
# gam.cfg parser
PARSER = 'pars'
# gam.cfg file
GAM_CFG_PATH = 'gcpa'
GAM_CFG_FILE = 'gcfi'
# redirected file: name, mode, encoding, delimiter, quotechar, write header, multiproces, queue
STDOUT = 'stdo'
STDERR = 'stde'
CSVFILE = 'csvf'
SAVED_STDOUT = 'svso'
REDIRECT_NAME = 'rdfn'
REDIRECT_MODE = 'rdmo'
REDIRECT_FD = 'rdfd'
REDIRECT_MULTI_FD = 'rdmf'
REDIRECT_STD = 'rdst'
REDIRECT_ENCODING = 'rden'
REDIRECT_COLUMN_DELIMITER = 'rddl'
REDIRECT_QUOTE_CHAR = 'rdqc'
REDIRECT_WRITE_HEADER = 'rdwh'
REDIRECT_MULTIPROCESS = 'rdmp'
REDIRECT_QUEUE = 'rdq'
REDIRECT_QUEUE_NAME = 'name'
REDIRECT_QUEUE_TODRIVE = 'todrive'
REDIRECT_QUEUE_TITLES = 'titles'
REDIRECT_QUEUE_SORTTITLES = 'sorttitles'
REDIRECT_QUEUE_QUOTECHAR = 'quotechar'
REDIRECT_QUEUE_FIXPATHS = 'fixpaths'
REDIRECT_QUEUE_DATA = 'rows'
REDIRECT_QUEUE_ARGS = 'args'
REDIRECT_QUEUE_GLOBALS = 'globals'
REDIRECT_QUEUE_VALUES = 'values'
REDIRECT_QUEUE_START = 'start'
REDIRECT_QUEUE_END = 'end'
REDIRECT_QUEUE_EOF = 'eof'
# File containing time of last GAM update check
LAST_UPDATE_CHECK_TXT = 'lupc'
# Index of start of <UserTypeEntity> in command line
ENTITY_CL_START = 'ecls'
ENTITY_CL_DELAY_START = 'eclD'
# csvfile keyfield <FieldName> [delimiter <Character>] (matchfield <FieldName> <MatchPattern>)* [datafield <FieldName>(:<FieldName>*) [delimiter <String>]]
# { key: [datafieldvalues]}
CSV_DATA_DICT = 'csdd'
CSV_KEY_FIELD = 'cskf'
CSV_SUBKEY_FIELD = 'cssk'
CSV_DATA_FIELD = 'csdf'
# Dictionary mapping OrgUnit ID to Name
MAP_ORGUNIT_ID_TO_NAME = 'oi2n'
# Make Role ID/Name map
MAKE_ROLE_ID_NAME_MAP = 'mkrm'
# Dictionary mapping Role ID to Name
MAP_ROLE_ID_TO_NAME = 'ri2n'
# Dictionary mapping Role Name to ID
MAP_ROLE_NAME_TO_ID = 'rn2i'
# Dictionary mapping User ID to Name
MAP_USER_ID_TO_NAME = 'ui2n'
# oauth2.txt.lock lockfile
OAUTH2_TXT_LOCK = 'oalk'
# GAM cache directory. If no_cache is True, this variable will be set to None
CACHE_DIR = 'gacd'
# Reset GAM cache directory after discovery
CACHE_DISCOVERY_ONLY = 'gcdo'
# Make Building ID/Name map
MAKE_BUILDING_ID_NAME_MAP = 'mkbm'
# Dictionary mapping Building ID to Name
MAP_BUILDING_ID_TO_NAME = 'bi2n'
# Dictionary mapping Building Name to ID
MAP_BUILDING_NAME_TO_ID = 'bn2i'
# Shared by threadBatchWorker and threadBatchGAMCommands
TBATCH_QUEUE = 'batq'
# datetime.datetime.now
DATETIME_NOW = 'dtno'
# Convert to local time
CONVERT_TO_LOCAL_TIME = 'ctlt'
# Check API calls rate
RATE_CHECK_COUNT = 'rccn'
RATE_CHECK_START = 'rcst'
# Number/length of API call retries
API_CALLS_RETRY_DATA = 'rtry'
#
Globals = {
  SYSEXITRC: 0,
  PID: 0,
  GAM_PATH: '.',
  WINDOWS: os.name == 'nt',
  SYS_ENCODING: 'utf-8',
  EXTRA_ARGS_LIST: [],
  ADMIN: None,
  CURRENT_API_SERVICES: {},
  CURRENT_CLIENT_API: None,
  CURRENT_CLIENT_API_SCOPES: set(),
  CURRENT_SVCACCT_API: None,
  CURRENT_SVCACCT_API_SCOPES: set(),
  CURRENT_SVCACCT_USER: None,
  OAUTH2_CLIENT_ID: None,
  OAUTH2SERVICE_JSON_DATA: {},
  OAUTH2SERVICE_CLIENT_ID: None,
  PARSER: None,
  GAM_CFG_PATH: '',
  GAM_CFG_FILE: '',
  STDOUT: {},
  STDERR: {},
  CSVFILE: {},
  SAVED_STDOUT: None,
  LAST_UPDATE_CHECK_TXT: '',
  ENTITY_CL_START: 1,
  ENTITY_CL_DELAY_START: 1,
  CSV_DATA_DICT: {},
  CSV_KEY_FIELD: None,
  CSV_SUBKEY_FIELD: None,
  CSV_DATA_FIELD: None,
  MAP_ORGUNIT_ID_TO_NAME: {},
  MAKE_ROLE_ID_NAME_MAP: True,
  MAP_ROLE_ID_TO_NAME: {},
  MAP_ROLE_NAME_TO_ID: {},
  MAP_USER_ID_TO_NAME: {},
  OAUTH2_TXT_LOCK: None,
  CACHE_DIR: None,
  CACHE_DISCOVERY_ONLY: True,
  MAKE_BUILDING_ID_NAME_MAP: True,
  MAP_BUILDING_ID_TO_NAME: {},
  MAP_BUILDING_NAME_TO_ID: {},
  TBATCH_QUEUE: None,
  DATETIME_NOW: None,
  CONVERT_TO_LOCAL_TIME: False,
  RATE_CHECK_COUNT: 0,
  RATE_CHECK_START: 0,
  API_CALLS_RETRY_DATA: {}
  }
