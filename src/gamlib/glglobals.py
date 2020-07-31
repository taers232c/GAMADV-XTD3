# -*- coding: utf-8 -*-

# Copyright (C) 2020 Ross Scroggs All Rights Reserved.
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
# GAM admin user
ADMIN = 'admin'
# Number/length of API call retries
API_CALLS_RETRY_DATA = 'rtry'
# GAM cache directory. If no_cache is True, this variable will be set to None
CACHE_DIR = 'gacd'
# Reset GAM cache directory after discovery
CACHE_DISCOVERY_ONLY = 'gcdo'
# Convert to local time
CONVERT_TO_LOCAL_TIME = 'ctlt'
# csvfile keyfield <FieldName> [delimiter <Character>] (matchfield <FieldName> <MatchPattern>)* [datafield <FieldName>(:<FieldName>*) [delimiter <String>]]
# { key: [datafieldvalues]}
CSV_DATA_DICT = 'csdd'
CSV_KEY_FIELD = 'cskf'
CSV_SUBKEY_FIELD = 'cssk'
CSV_DATA_FIELD = 'csdf'
# Column delimiter in CSV output file
CSV_OUTPUT_COLUMN_DELIMITER = 'codl'
# Quote character in CSV output file
CSV_OUTPUT_QUOTE_CHAR = 'coqc'
# Filter for column headers
CSV_OUTPUT_HEADER_FILTER = 'cohf'
# Filter for column headers to drop
CSV_OUTPUT_HEADER_DROP_FILTER = 'codf'
# Filter for column values
CSV_OUTPUT_ROW_FILTER = 'corf'
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
# datetime.datetime.now
DATETIME_NOW = 'dtno'
# Decoded ID token
DECODED_ID_TOKEN = 'didt'
# Index of start of <UserTypeEntity> in command line
ENTITY_CL_START = 'ecls'
ENTITY_CL_DELAY_START = 'eclD'
# Extra arguments to pass to GAPI functions
EXTRA_ARGS_LIST = 'exad'
# gam.cfg file
GAM_CFG_PATH = 'gcpa'
GAM_CFG_FILE = 'gcfi'
# File containing oauth create URL
GAM_OAUTH_URL_TXT = 'gout'
# Path to gam
GAM_PATH = 'gpth'
# Python source, PyInstaller or StaticX?
GAM_TYPE = 'gtyp'
# Length of last Got message
LAST_GOT_MSG_LEN = 'lgml'
# File containing time of last GAM update check
LAST_UPDATE_CHECK_TXT = 'lupc'
# Make Building ID/Name map
MAKE_BUILDING_ID_NAME_MAP = 'mkbm'
# Dictionary mapping Building ID to Name
MAP_BUILDING_ID_TO_NAME = 'bi2n'
# Dictionary mapping Building Name to ID
MAP_BUILDING_NAME_TO_ID = 'bn2i'
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
# Values retrieved from oauth2.txt
OAUTH2_CLIENT_ID = 'oaci'
# oauth2.txt lock file
OAUTH2_TXT_LOCK = 'oatl'
# Values retrieved from oauth2service.json
OAUTH2SERVICE_CLIENT_ID = 'osci'
OAUTH2SERVICE_JSON_DATA = 'osjd'
# Were scopes values retrieved from oauth2service.json
SVCACCT_SCOPES_DEFINED = 'sasd'
# Scopes values retrieved from oauth2service.json
SVCACCT_SCOPES = 'sasc'
# gam.cfg parser
PARSER = 'pars'
# Process ID
PID = 'pid '
# Check API calls rate
RATE_CHECK_COUNT = 'rccn'
RATE_CHECK_START = 'rcst'
# redirected files
CSVFILE = 'csvf'
STDOUT = 'stdo'
STDERR = 'stde'
SAVED_STDOUT = 'svso'
# redirected file fields: name, mode, encoding, write header, multiproces, queue
REDIRECT_NAME = 'rdfn'
REDIRECT_MODE = 'rdmo'
REDIRECT_FD = 'rdfd'
REDIRECT_MULTI_FD = 'rdmf'
REDIRECT_STD = 'rdst'
REDIRECT_ENCODING = 'rden'
REDIRECT_WRITE_HEADER = 'rdwh'
REDIRECT_MULTIPROCESS = 'rdmp'
REDIRECT_QUEUE = 'rdq'
REDIRECT_QUEUE_NAME = 'name'
REDIRECT_QUEUE_TODRIVE = 'todrive'
REDIRECT_QUEUE_CSVPF = 'csvpf'
REDIRECT_QUEUE_DATA = 'rows'
REDIRECT_QUEUE_ARGS = 'args'
REDIRECT_QUEUE_GLOBALS = 'globals'
REDIRECT_QUEUE_VALUES = 'values'
REDIRECT_QUEUE_START = 'start'
REDIRECT_QUEUE_END = 'end'
REDIRECT_QUEUE_EOF = 'eof'
# Section name from outer gam, passed to inner gams
SECTION = 'sect'
# Most errors print a message and bail out with a return code
# Some commands want to set a non-zero return code but not bail
SYSEXITRC = 'sxrc'
# Encodings
SYS_ENCODING = 'syen'
# Shared by threadBatchWorker and threadBatchGAMCommands
TBATCH_QUEUE = 'batq'
# CSV todrive options
CSV_TODRIVE = 'todr'
# Are we on Windows?
WINDOWS = 'wndo'
#
Globals = {
  ADMIN: None,
  API_CALLS_RETRY_DATA: {},
  CACHE_DIR: None,
  CACHE_DISCOVERY_ONLY: True,
  CONVERT_TO_LOCAL_TIME: False,
  CSV_DATA_DICT: {},
  CSV_KEY_FIELD: None,
  CSV_SUBKEY_FIELD: None,
  CSV_DATA_FIELD: None,
  CSV_OUTPUT_COLUMN_DELIMITER: ',',
  CSV_OUTPUT_QUOTE_CHAR: '"',
  CSV_OUTPUT_HEADER_FILTER: [],
  CSV_OUTPUT_HEADER_DROP_FILTER: [],
  CSV_OUTPUT_ROW_FILTER: [],
  CURRENT_API_SERVICES: {},
  CURRENT_CLIENT_API: None,
  CURRENT_CLIENT_API_SCOPES: set(),
  CURRENT_SVCACCT_API: None,
  CURRENT_SVCACCT_API_SCOPES: set(),
  CURRENT_SVCACCT_USER: None,
  DATETIME_NOW: None,
  DECODED_ID_TOKEN: None,
  ENTITY_CL_START: 1,
  ENTITY_CL_DELAY_START: 1,
  EXTRA_ARGS_LIST: [],
  GAM_CFG_PATH: '',
  GAM_CFG_FILE: '',
  GAM_OAUTH_URL_TXT: None,
  GAM_PATH: '.',
  GAM_TYPE: '',
  LAST_GOT_MSG_LEN: 0,
  LAST_UPDATE_CHECK_TXT: '',
  MAKE_BUILDING_ID_NAME_MAP: True,
  MAP_BUILDING_ID_TO_NAME: {},
  MAP_BUILDING_NAME_TO_ID: {},
  MAP_ORGUNIT_ID_TO_NAME: {},
  MAKE_ROLE_ID_NAME_MAP: True,
  MAP_ROLE_ID_TO_NAME: {},
  MAP_ROLE_NAME_TO_ID: {},
  MAP_USER_ID_TO_NAME: {},
  OAUTH2_CLIENT_ID: None,
  OAUTH2_TXT_LOCK: None,
  OAUTH2SERVICE_CLIENT_ID: None,
  OAUTH2SERVICE_JSON_DATA: {},
  SVCACCT_SCOPES_DEFINED: False,
  SVCACCT_SCOPES: {},
  PARSER: None,
  PID: 0,
  RATE_CHECK_COUNT: 0,
  RATE_CHECK_START: 0,
  CSVFILE: {},
  STDERR: {},
  STDOUT: {},
  SAVED_STDOUT: None,
  SECTION: None,
  SYSEXITRC: 0,
  SYS_ENCODING: 'utf-8',
  TBATCH_QUEUE: None,
  CSV_TODRIVE: {},
  WINDOWS: os.name == 'nt',
  }
