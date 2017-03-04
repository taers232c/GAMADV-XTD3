# -*- coding: utf-8 -*-

# Copyright (C) 2016 Ross Scroggs All Rights Reserved.
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

"""Google API resources

"""
# APIs
ADMIN_SETTINGS = 'admin-settings'
APPSACTIVITY = 'appsactivity'
CALENDAR = 'calendar'
CLASSROOM = 'classroom'
CLOUDPRINT = 'cloudprint'
CONTACTS = 'contacts'
DATATRANSFER = 'datatransfer'
DIRECTORY = 'directory'
DRIVE = 'drive'
EMAIL_AUDIT = 'email-audit'
EMAIL_SETTINGS = 'email-settings'
GMAIL = 'gmail'
GPLUS = 'plus'
GROUPSMIGRATION = 'groupsmigration'
GROUPSSETTINGS = 'groupssettings'
LICENSING = 'licensing'
REPORTS = 'reports'
RESELLER = 'reseller'
SITES = 'sites'
SITEVERIFICATION = 'siteVerification'
#
FAM1_SCOPES = 'fam1'
FAM2_SCOPES = 'fam2'
FAM_LIST = [FAM1_SCOPES, FAM2_SCOPES]
PREV_FAM_LIST = ['gapi', 'gdata']
#
OAUTH2_TOKEN_ERRORS = [
  'access_denied', 'invalid_grant', 'unauthorized_client: Unauthorized client or scope in request.', 'access_denied: Requested client not authorized.',
  'invalid_grant: Not a valid email.', 'invalid_grant: Invalid email or User ID', 'invalid_grant: Bad Request',
  'invalid_request: Invalid impersonation prn email address.', 'internal_failure: Backend Error',
  ]

_INFO = {
  ADMIN_SETTINGS: {'version': 'v2', 'credfam': FAM2_SCOPES, 'localjson': True},
  APPSACTIVITY: {'version': 'v1', 'credfam': FAM1_SCOPES, 'svcacctscopes': ['https://www.googleapis.com/auth/activity', 'https://www.googleapis.com/auth/drive']},
  CALENDAR: {'version': 'v3', 'credfam': FAM1_SCOPES, 'svcacctscopes': ['https://www.googleapis.com/auth/calendar',]},
  CLASSROOM: {'version': 'v1', 'credfam': FAM2_SCOPES},
  CLOUDPRINT: {'version': 'v2', 'credfam': FAM2_SCOPES, 'localjson': True},
  CONTACTS: {'version': 'v3', 'credfam': FAM2_SCOPES, 'svcacctscopes': ['https://www.google.com/m8/feeds',], 'localjson': True},
  DATATRANSFER: {'version': 'datatransfer_v1', 'credfam': FAM1_SCOPES},
  DIRECTORY: {'version': 'directory_v1', 'credfam': FAM1_SCOPES},
  DRIVE: {'version': 'v2', 'credfam': FAM1_SCOPES, 'svcacctscopes': ['https://www.googleapis.com/auth/drive',]},
  EMAIL_AUDIT: {'version': 'v1', 'credfam': FAM2_SCOPES, 'localjson': True},
  EMAIL_SETTINGS: {'version': 'v2', 'credfam': FAM1_SCOPES, 'localjson': True},
  GMAIL: {'version': 'v1', 'credfam': FAM1_SCOPES, 'svcacctscopes': ['https://mail.google.com/', 'https://www.googleapis.com/auth/gmail.settings.basic',
                                                                         'https://www.googleapis.com/auth/gmail.settings.sharing',]},
  GPLUS: {'version': 'v1', 'credfam': FAM1_SCOPES, 'svcacctscopes': ['https://www.googleapis.com/auth/plus.me', 'https://www.googleapis.com/auth/plus.login',
                                                                         'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']},
  GROUPSMIGRATION: {'version': 'v1', 'credfam': FAM2_SCOPES},
  GROUPSSETTINGS: {'version': 'v1', 'credfam': FAM2_SCOPES},
  LICENSING: {'version': 'v1', 'credfam': FAM1_SCOPES},
  REPORTS: {'version': 'reports_v1', 'credfam': FAM2_SCOPES},
  RESELLER: {'version': 'v1', 'credfam': FAM2_SCOPES},
  SITES: {'version': 'v1', 'credfam': FAM2_SCOPES, 'svcacctscopes': ['https://sites.google.com/feeds',], 'localjson': True},
  SITEVERIFICATION: {'version': 'v1', 'credfam': FAM2_SCOPES},
  }
#
DRIVE_FILE_CREATED_DATE_TIME = 'createdDate'
DRIVE_FILE_MARKED_VIEWED_BY_ME_DATE_TIME = 'markedViewedByMeDate'
DRIVE_FILE_LAST_VIEWED_BY_ME_DATE_TIME = 'lastViewedByMeDate'
DRIVE_FILE_MODIFIED_BY_ME_DATE_TIME = 'modifiedByMeDate'
DRIVE_FILE_MODIFIED_DATE_TIME = 'modifiedDate'
DRIVE_FILE_NAME = 'title'
DRIVE_FILE_SHARED_WITH_ME_DATE_TIME = 'sharedWithMeDate'
DRIVE_FILE_SIZE = 'fileSize'
DRIVE_FILE_VIEW_LINK = 'alternateLink'
DRIVE_FILE_LABEL_RESTRICTED = 'restricted'
DRIVE_FILE_LABEL_VIEWED = 'viewed'
#
DRIVE_FILES_LIST = 'items'
DRIVE_CREATE_FILE = 'insert'
DRIVE_PATCH_FILE = 'patch'
DRIVE_UPDATE_FILE = 'update'
#
DRIVE_PERMISSIONS_DOMAIN_TYPE_VALUE = 'value'
DRIVE_PERMISSIONS_EXPIRATION_DATE_TIME = 'expirationDate'
DRIVE_PERMISSIONS_GROUP_USER_TYPE_VALUE = 'value'
DRIVE_PERMISSIONS_LIST = 'items'
DRIVE_PERMISSIONS_NAME = 'name'
#
DRIVE_CREATE_PERMISSIONS = 'insert'
DRIVE_PATCH_PERMISSIONS = 'patch'
#
DRIVE_REVISIONS_LIST = 'items'
#
DRIVE_PARENTS_ID = 'parents(id)'

def getVersion(api):
  version = _INFO[api]['version']
  cred_family = _INFO[api]['credfam']
  if api in [DIRECTORY, REPORTS, DATATRANSFER]:
    api = 'admin'
  return (api, version, '{0}-{1}'.format(api, version), cred_family)

def getSortedSvcAcctScopesList():
  all_scopes = []
  for api in _INFO:
    for scope in _INFO[api].get('svcacctscopes', []):
      if scope not in all_scopes:
        all_scopes.append(scope)
  all_scopes.sort()
  return (all_scopes, len(all_scopes))

def getSvcAcctScopes(api):
  return _INFO[api]['svcacctscopes']

def hasLocalJSON(api):
  return _INFO[api].get('localjson', False)
