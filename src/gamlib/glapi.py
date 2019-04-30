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

"""Google API resources

"""
# APIs
ADMIN = 'admin'
ALERTCENTER = 'alertcenter'
APPSACTIVITY = 'appsactivity'
CALENDAR = 'calendar'
CHAT = 'chat'
CLASSROOM = 'classroom'
CLOUDPRINT = 'cloudprint'
CONTACTS = 'contacts'
DATATRANSFER = 'datatransfer'
DIRECTORY = 'directory'
DRIVE = 'drive'
DRIVE3 = 'drive3'
DRIVEACTIVITY = 'driveactivity'
EMAIL_AUDIT = 'email-audit'
EMAIL_SETTINGS = 'email-settings'
GMAIL = 'gmail'
GROUPSMIGRATION = 'groupsmigration'
GROUPSSETTINGS = 'groupssettings'
LICENSING = 'licensing'
PEOPLE = 'people'
PUBSUB = 'pubsub'
REPORTS = 'reports'
RESELLER = 'reseller'
SHEETS = 'sheets'
SITES = 'sites'
SITEVERIFICATION = 'siteVerification'
STORAGE = 'storage'
VAULT = 'vault'
#
FAM1_SCOPES = 'fam1'
FAM2_SCOPES = 'fam2'
FAM_LIST = [FAM1_SCOPES, FAM2_SCOPES]
PREV_FAM_LIST = ['gapi', 'gdata']
#
OAUTH2_TOKEN_ERRORS = [
  'access_denied',
  'access_denied: Requested client not authorized',
  'internal_failure: Backend Error',
  'internal_failure: None',
  'invalid_grant',
  'invalid_grant: Bad Request',
  'invalid_grant: Invalid email or User ID',
  'invalid_grant: Not a valid email',
  'invalid_grant: Invalid JWT: No valid verifier found for issuer',
  'invalid_request: Invalid impersonation prn email address',
  'unauthorized_client: Client is unauthorized to retrieve access tokens using this method',
  'unauthorized_client: Client is unauthorized to retrieve access tokens using this method, or client not authorized for any of the scopes requested',
  'unauthorized_client: Unauthorized client or scope in request',
  ]

PROJECT_APIS = [
  'admin.googleapis.com',
  'alertcenter.googleapis.com',
  'appsactivity.googleapis.com',
  'audit.googleapis.com',
  'calendar-json.googleapis.com',
  # 'chat.googleapis.com',
  'classroom.googleapis.com',
  'contacts.googleapis.com',
  'drive.googleapis.com',
  'driveactivity.googleapis.com',
  'gmail.googleapis.com',
  'groupsmigration.googleapis.com',
  'groupssettings.googleapis.com',
  'licensing.googleapis.com',
  'people.googleapis.com',
  'reseller.googleapis.com',
  'sheets.googleapis.com',
  'siteverification.googleapis.com',
  'storage-api.googleapis.com',
  'vault.googleapis.com',
  ]

_INFO = {
  APPSACTIVITY: {'version': 'v1', 'v2discovery': False,
                 'credfam': FAM1_SCOPES,
                 'svcacctscopes': ['https://www.googleapis.com/auth/activity',
                                   'https://www.googleapis.com/auth/drive',]},
  ALERTCENTER: {'version': 'v1beta1', 'v2discovery': True,
                'credfam': FAM2_SCOPES,
                'svcacctscopes': ['https://www.googleapis.com/auth/apps.alerts',]},
  CALENDAR: {'version': 'v3', 'v2discovery': False,
             'credfam': FAM1_SCOPES,
             'svcacctscopes': ['https://www.googleapis.com/auth/calendar',]},
  # CHAT: {'version': 'v1', 'v2discovery': False,
  #        'credfam': FAM2_SCOPES,
  #        'svcacctscopes': ['https://www.googleapis.com/auth/chat.bot',]},
  CLASSROOM: {'version': 'v1', 'v2discovery': True,
              'credfam': FAM2_SCOPES,
              'svcacctscopes': ['https://www.googleapis.com/auth/classroom.rosters',
                                'https://www.googleapis.com/auth/classroom.announcements',
                                'https://www.googleapis.com/auth/classroom.coursework.students',]},
  CLOUDPRINT: {'version': 'v2', 'v2discovery': True,
               'credfam': FAM2_SCOPES,
               'localjson': True},
  CONTACTS: {'version': 'v3', 'v2discovery': False,
             'credfam': FAM2_SCOPES,
             'svcacctscopes': ['https://www.google.com/m8/feeds',],
             'localjson': True},
  DATATRANSFER: {'version': 'datatransfer_v1', 'v2discovery': False,
                 'credfam': FAM1_SCOPES},
  DIRECTORY: {'version': 'directory_v1', 'v2discovery': False,
              'credfam': FAM1_SCOPES},
  DRIVE: {'version': 'v2', 'v2discovery': False,
          'credfam': FAM1_SCOPES,
          'svcacctscopes': ['https://www.googleapis.com/auth/drive',]},
  DRIVE3: {'version': 'v3', 'v2discovery': False,
           'credfam': FAM1_SCOPES,
           'svcacctscopes': ['https://www.googleapis.com/auth/drive',]},
  DRIVEACTIVITY: {'version': 'v2', 'v2discovery': True,
                  'credfam': FAM1_SCOPES,
                  'svcacctscopes': ['https://www.googleapis.com/auth/drive.activity',
                                    'https://www.googleapis.com/auth/drive',]},
  EMAIL_AUDIT: {'version': 'v1', 'v2discovery': False,
                'credfam': FAM2_SCOPES,
                'localjson': True},
  EMAIL_SETTINGS: {'version': 'v2', 'v2discovery': False,
                   'credfam': FAM1_SCOPES,
                   'localjson': True},
  GMAIL: {'version': 'v1', 'v2discovery': False,
          'credfam': FAM1_SCOPES,
          'svcacctscopes': ['https://mail.google.com/',
                            'https://www.googleapis.com/auth/gmail.modify',
                            'https://www.googleapis.com/auth/gmail.settings.basic',
                            'https://www.googleapis.com/auth/gmail.settings.sharing',]},
  GROUPSMIGRATION: {'version': 'v1', 'v2discovery': False,
                    'credfam': FAM2_SCOPES,
                    'svcacctscopes': ['https://www.googleapis.com/auth/apps.groups.migration',]},
  GROUPSSETTINGS: {'version': 'v1', 'v2discovery': False,
                   'credfam': FAM2_SCOPES},
  LICENSING: {'version': 'v1', 'v2discovery': False,
              'credfam': FAM1_SCOPES},
  PEOPLE: {'version': 'v1', 'v2discovery': True,
           'credfam': FAM2_SCOPES,
           'svcacctscopes': ['https://www.googleapis.com/auth/contacts',]},
  REPORTS: {'version': 'reports_v1', 'v2discovery': False,
            'credfam': FAM2_SCOPES},
  RESELLER: {'version': 'v1', 'v2discovery': False,
             'credfam': FAM2_SCOPES},
  SHEETS: {'version': 'v4', 'v2discovery': True,
           'credfam': FAM2_SCOPES,
           'svcacctscopes': ['https://www.googleapis.com/auth/spreadsheets',]},
  SITES: {'version': 'v1', 'v2discovery': False,
          'credfam': FAM2_SCOPES,
          'localjson': True,
          'svcacctscopes': ['https://sites.google.com/feeds',]},
  SITEVERIFICATION: {'version': 'v1', 'v2discovery': False,
                     'credfam': FAM2_SCOPES},
  STORAGE: {'version': 'v1', 'v2discovery': False,
            'credfam': FAM2_SCOPES},
  VAULT: {'version': 'v1', 'v2discovery': True,
          'credfam': FAM2_SCOPES},
  }

EMAIL_SCOPE = 'email'
PROFILE_SCOPE = 'profile'
VAULT_SCOPES = ['https://www.googleapis.com/auth/ediscovery', 'https://www.googleapis.com/auth/ediscovery.readonly']

READONLY = ['readonly',]

OAUTH2_SCOPES = [
  {'name': 'Calendar API',
   'api': CALENDAR,
   'credfam': FAM1_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/calendar'},
  {'name': 'Classroom API - Courses',
   'api': CLASSROOM,
   'credfam': FAM2_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.courses'},
  {'name': 'Classroom API - Course Announcements',
   'api': CLASSROOM,
   'credfam': FAM2_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.announcements'},
  {'name': 'Classroom API - Course Work/Submissions',
   'api': CLASSROOM,
   'credfam': FAM2_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.coursework.students'},
  {'name': 'Classroom API - Student Guardians',
   'api': CLASSROOM,
   'credfam': FAM2_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.guardianlinks.students'},
  {'name': 'Classroom API - Profile Emails',
   'api': CLASSROOM,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/classroom.profile.emails'},
  {'name': 'Classroom API - Profile Photos',
   'api': CLASSROOM,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/classroom.profile.photos'},
  {'name': 'Classroom API - Rosters',
   'api': CLASSROOM,
   'credfam': FAM2_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.rosters'},
  {'name': 'Cloudprint API',
   'api': CLOUDPRINT,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/cloudprint'},
  {'name': 'Cloud Storage (Vault Export - read only)',
   'api': STORAGE,
   'subscopes': [],
   'credfam': FAM2_SCOPES,
   'scope': 'https://www.googleapis.com/auth/devstorage.read_only'},
  {'name': 'Contacts API - Domain Shared and Users and GAL',
   'api': CONTACTS,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'scope': 'https://www.google.com/m8/feeds'},
  {'name': 'Data Transfer API',
   'api': DATATRANSFER,
   'credfam': FAM1_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.datatransfer'},
  {'name': 'Directory API - Chrome OS Devices',
   'api': DIRECTORY,
   'credfam': FAM1_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.device.chromeos'},
  {'name': 'Directory API - Customers',
   'api': DIRECTORY,
   'credfam': FAM1_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.customer'},
  {'name': 'Directory API - Domains',
   'api': DIRECTORY,
   'credfam': FAM1_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.domain'},
  {'name': 'Directory API - Groups',
   'api': DIRECTORY,
   'credfam': FAM1_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.group'},
  {'name': 'Directory API - Mobile Devices Directory',
   'api': DIRECTORY,
   'credfam': FAM1_SCOPES,
   'subscopes': ['readonly', 'action'],
   'scope': 'https://www.googleapis.com/auth/admin.directory.device.mobile'},
  {'name': 'Directory API - Organizational Units',
   'api': DIRECTORY,
   'credfam': FAM1_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.orgunit'},
  {'name': 'Directory API - Resource Calendars',
   'api': DIRECTORY,
   'credfam': FAM1_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.resource.calendar'},
  {'name': 'Directory API - Roles',
   'api': DIRECTORY,
   'credfam': FAM1_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.rolemanagement'},
  {'name': 'Directory API - User Schemas',
   'api': DIRECTORY,
   'credfam': FAM1_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.userschema'},
  {'name': 'Directory API - User Security',
   'api': DIRECTORY,
   'credfam': FAM1_SCOPES,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/admin.directory.user.security'},
  {'name': 'Directory API - Users',
   'api': DIRECTORY,
   'credfam': FAM1_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.user'},
  {'name': 'Email Audit API',
   'api': EMAIL_AUDIT,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'scope': 'https://apps-apis.google.com/a/feeds/compliance/audit/'},
  {'name': 'Email Settings API - Users',
   'api': EMAIL_SETTINGS,
   'credfam': FAM1_SCOPES,
   'subscopes': [],
   'scope': 'https://apps-apis.google.com/a/feeds/emailsettings/2.0/'},
  {'name': 'Groups Migration API',
   'api': GROUPSMIGRATION,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/apps.groups.migration'},
  {'name': 'Groups Settings API',
   'api': GROUPSSETTINGS,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/apps.groups.settings'},
  {'name': 'License Manager API',
   'api': LICENSING,
   'credfam': FAM1_SCOPES,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/apps.licensing'},
  {'name': 'People API',
   'api': PEOPLE,
   'credfam': FAM2_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/contacts'},
  {'name': 'Reports API - Audit Reports',
   'api': REPORTS,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/admin.reports.audit.readonly'},
  {'name': 'Reports API - Usage Reports',
   'api': REPORTS,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/admin.reports.usage.readonly'},
  {'name': 'Reseller API',
   'api': RESELLER,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'offByDefault': True,
   'scope': 'https://www.googleapis.com/auth/apps.order'},
  {'name': 'Site Verification API',
   'api': SITEVERIFICATION,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/siteverification'},
  {'name': 'Sites API',
   'api': SITES,
   'credfam': FAM2_SCOPES,
   'subscopes': [],
   'scope': 'https://sites.google.com/feeds'},
  {'name': 'Vault API',
   'api': VAULT,
   'credfam': FAM2_SCOPES,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/ediscovery'},
  ]

DRIVE3_TO_DRIVE2_ABOUT_FIELDS_MAP = {
  'displayName': 'name',
  'limit': 'quotaBytesTotal',
  'usage': 'quotaBytesUsedAggregate',
  'usageInDrive': 'quotaBytesUsed',
  'usageInDriveTrash': 'quotaBytesUsedInTrash',
  }

DRIVE3_TO_DRIVE2_CAPABILITIES_FIELDS_MAP = {
  'canComment': 'canComment',
  'canReadRevisions': 'canReadRevisions',
  'canCopy': 'copyable',
  'canEdit': 'editable',
  'canShare': 'shareable',
  }

DRIVE3_TO_DRIVE2_CAPABILITIES_NAMES_MAP = {
  'canChangeViewersCanCopyContent': 'canChangeRestrictedDownload',
  }

DRIVE3_TO_DRIVE2_CAPABILITIES_TITLES_MAP = {
  'capabilities.canComment': 'canComment',
  'capabilities.canReadRevisions': 'canReadRevisions',
  'capabilities.canCopy': 'copyable',
  'capabilities.canEdit': 'editable',
  'capabilities.canShare': 'shareable',
  }

DRIVE3_TO_DRIVE2_FILES_FIELDS_MAP = {
  'allowFileDiscovery': 'withLink',
  'createdTime': 'createdDate',
  'expirationTime': 'expirationDate',
  'modifiedByMe': 'modified',
  'modifiedByMeTime': 'modifiedByMeDate',
  'modifiedTime': 'modifiedDate',
  'name': 'title',
  'sharedWithMeTime': 'sharedWithMeDate',
  'size': 'fileSize',
  'trashedTime': 'trashedDate',
  'viewedByMe': 'viewed',
  'viewedByMeTime': 'lastViewedByMeDate',
  'webViewLink': 'alternateLink',
  }

DRIVE3_TO_DRIVE2_LABELS_MAP = {
  'modifiedByMe': 'modified',
  'starred': 'starred',
  'trashed': 'trashed',
  'viewedByMe': 'viewed',
  }

DRIVE3_TO_DRIVE2_REVISIONS_FIELDS_MAP = {
  'modifiedTime': 'modifiedDate',
  'keepForever': 'pinned',
  'size': 'fileSize',
  }

def getVersion(api):
  version = _INFO[api]['version']
  v2discovery = _INFO[api]['v2discovery']
  cred_family = _INFO[api]['credfam']
  if api in [DIRECTORY, REPORTS, DATATRANSFER]:
    api = ADMIN
  elif api == DRIVE3:
    api = DRIVE
  return (api, version, '{0}-{1}'.format(api, version), v2discovery, cred_family)

def getClientScopesSet(api):
  return set([scope['scope'] for scope in OAUTH2_SCOPES if scope['api'] == api])

def getSortedSvcAcctScopesList():
  all_scopes = []
  for api in _INFO:
    for scope in _INFO[api].get('svcacctscopes', []):
      if scope not in all_scopes:
        all_scopes.append(scope)
  all_scopes.sort()
  return (all_scopes, len(all_scopes))

def getSvcAcctScopesSet(api):
  return set(_INFO[api]['svcacctscopes'])

def hasLocalJSON(api):
  return _INFO[api].get('localjson', False)
