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
ADMIN = u'admin'
APPSACTIVITY = u'appsactivity'
CALENDAR = u'calendar'
CHAT = u'chat'
CLASSROOM = u'classroom'
CLOUDPRINT = u'cloudprint'
CONTACTS = u'contacts'
DATATRANSFER = u'datatransfer'
DIRECTORY = u'directory'
DRIVE = u'drive'
DRIVE3 = u'drive3'
DRIVEACTIVITY = u'driveactivity'
EMAIL_AUDIT = u'email-audit'
EMAIL_SETTINGS = u'email-settings'
GMAIL = u'gmail'
GPLUS = u'plus'
GROUPSMIGRATION = u'groupsmigration'
GROUPSSETTINGS = u'groupssettings'
LICENSING = u'licensing'
PEOPLE = u'people'
PUBSUB = u'pubsub'
REPORTS = u'reports'
RESELLER = u'reseller'
SHEETS = u'sheets'
SITES = u'sites'
SITEVERIFICATION = u'siteVerification'
STORAGE = u'storage'
VAULT = u'vault'
#
FAM1_SCOPES = u'fam1'
FAM2_SCOPES = u'fam2'
FAM_LIST = [FAM1_SCOPES, FAM2_SCOPES]
PREV_FAM_LIST = [u'gapi', u'gdata']
#
OAUTH2_TOKEN_ERRORS = [
  u'access_denied',
  u'access_denied: Requested client not authorized',
  u'internal_failure: Backend Error',
  u'invalid_grant',
  u'invalid_grant: Bad Request',
  u'invalid_grant: Invalid email or User ID',
  u'invalid_grant: Not a valid email',
  u'invalid_grant: Invalid JWT: No valid verifier found for issuer',
  u'invalid_request: Invalid impersonation prn email address',
  u'unauthorized_client: Client is unauthorized to retrieve access tokens using this method',
  u'unauthorized_client: Client is unauthorized to retrieve access tokens using this method, or client not authorized for any of the scopes requested',
  u'unauthorized_client: Unauthorized client or scope in request',
  ]

PROJECT_APIS = [
  u'admin.googleapis.com',
  u'appsactivity.googleapis.com',
  u'audit.googleapis.com',
  u'calendar-json.googleapis.com',
#  u'chat.googleapis.com',
  u'classroom.googleapis.com',
  u'contacts.googleapis.com',
  u'drive.googleapis.com',
  u'driveactivity.googleapis.com',
  u'gmail.googleapis.com',
  u'groupsmigration.googleapis.com',
  u'groupssettings.googleapis.com',
  u'licensing.googleapis.com',
  u'people.googleapis.com',
  u'plus.googleapis.com',
  u'reseller.googleapis.com',
  u'sheets.googleapis.com',
  u'siteverification.googleapis.com',
  u'storage-api.googleapis.com',
  u'vault.googleapis.com',
  ]

_INFO = {
  APPSACTIVITY: {u'version': u'v1', u'credfam': FAM1_SCOPES, u'svcacctscopes': [u'https://www.googleapis.com/auth/activity',
                                                                                u'https://www.googleapis.com/auth/drive',]},
  CALENDAR: {u'version': u'v3', u'credfam': FAM1_SCOPES, u'svcacctscopes': [u'https://www.googleapis.com/auth/calendar',]},
#  CHAT: {u'version': u'v1', u'credfam': FAM2_SCOPES, u'svcacctscopes': [u'https://www.googleapis.com/auth/chat.bot',]},
  CLASSROOM: {u'version': u'v1', u'credfam': FAM2_SCOPES, u'svcacctscopes': [u'https://www.googleapis.com/auth/classroom.rosters',
                                                                             u'https://www.googleapis.com/auth/classroom.announcements',
                                                                             u'https://www.googleapis.com/auth/classroom.coursework.students',]},
  CLOUDPRINT: {u'version': u'v2', u'credfam': FAM2_SCOPES, u'localjson': True},
  CONTACTS: {u'version': u'v3', u'credfam': FAM2_SCOPES, u'svcacctscopes': [u'https://www.google.com/m8/feeds',], u'localjson': True},
  DATATRANSFER: {u'version': u'datatransfer_v1', u'credfam': FAM1_SCOPES},
  DIRECTORY: {u'version': u'directory_v1', u'credfam': FAM1_SCOPES},
  DRIVE: {u'version': u'v2', u'credfam': FAM1_SCOPES, u'svcacctscopes': [u'https://www.googleapis.com/auth/drive',]},
  DRIVE3: {u'version': u'v3', u'credfam': FAM1_SCOPES, u'svcacctscopes': [u'https://www.googleapis.com/auth/drive',]},
  DRIVEACTIVITY: {u'version': u'v2', u'credfam': FAM1_SCOPES, u'svcacctscopes': [u'https://www.googleapis.com/auth/drive.activity',
                                                                                 u'https://www.googleapis.com/auth/drive',]},
  EMAIL_AUDIT: {u'version': u'v1', u'credfam': FAM2_SCOPES, u'localjson': True},
  EMAIL_SETTINGS: {u'version': u'v2', u'credfam': FAM1_SCOPES, u'localjson': True},
  GMAIL: {u'version': u'v1', u'credfam': FAM1_SCOPES, u'svcacctscopes': [u'https://mail.google.com/',
                                                                         u'https://www.googleapis.com/auth/gmail.modify',
                                                                         u'https://www.googleapis.com/auth/gmail.settings.basic',
                                                                         u'https://www.googleapis.com/auth/gmail.settings.sharing',]},
  GPLUS: {u'version': u'v1', u'credfam': FAM1_SCOPES, u'svcacctscopes': [u'https://www.googleapis.com/auth/plus.me',
                                                                         u'https://www.googleapis.com/auth/plus.profile.agerange.read',
                                                                         u'https://www.googleapis.com/auth/plus.profile.language.read', 
                                                                         u'https://www.googleapis.com/auth/userinfo.email',
                                                                         u'https://www.googleapis.com/auth/userinfo.profile',]},
  GROUPSMIGRATION: {u'version': u'v1', u'credfam': FAM2_SCOPES},
  GROUPSSETTINGS: {u'version': u'v1', u'credfam': FAM2_SCOPES},
  LICENSING: {u'version': u'v1', u'credfam': FAM1_SCOPES},
  PEOPLE: {u'version': u'v1', u'credfam': FAM2_SCOPES, u'svcacctscopes': [u'https://www.googleapis.com/auth/contacts',]},
  REPORTS: {u'version': u'reports_v1', u'credfam': FAM2_SCOPES},
  RESELLER: {u'version': u'v1', u'credfam': FAM2_SCOPES},
  SHEETS: {u'version': u'v4', u'credfam': FAM2_SCOPES, u'svcacctscopes': [u'https://www.googleapis.com/auth/spreadsheets',]},
  SITES: {u'version': u'v1', u'credfam': FAM2_SCOPES, u'svcacctscopes': [u'https://sites.google.com/feeds',], u'localjson': True},
  SITEVERIFICATION: {u'version': u'v1', u'credfam': FAM2_SCOPES},
  STORAGE: {u'version': u'v1', u'credfam': FAM2_SCOPES},
  VAULT: {u'version': u'v1', u'credfam': FAM2_SCOPES},
  }

EMAIL_SCOPE = u'email'
PROFILE_SCOPE = u'profile'
VAULT_SCOPES = [u'https://www.googleapis.com/auth/ediscovery', u'https://www.googleapis.com/auth/ediscovery.readonly']

READONLY = [u'readonly',]

OAUTH2_SCOPES = [
  {u'name': u'Calendar API',
   u'api': CALENDAR,
   u'credfam': FAM1_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/calendar'},
  {u'name': u'Classroom API - Courses',
   u'api': CLASSROOM,
   u'credfam': FAM2_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/classroom.courses'},
  {u'name': u'Classroom API - Course Announcements',
   u'api': CLASSROOM,
   u'credfam': FAM2_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/classroom.announcements'},
  {u'name': u'Classroom API - Course Work/Submissions',
   u'api': CLASSROOM,
   u'credfam': FAM2_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/classroom.coursework.students'},
  {u'name': u'Classroom API - Student Guardians',
   u'api': CLASSROOM,
   u'credfam': FAM2_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/classroom.guardianlinks.students'},
  {u'name': u'Classroom API - Profile Emails',
   u'api': CLASSROOM,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.googleapis.com/auth/classroom.profile.emails'},
  {u'name': u'Classroom API - Profile Photos',
   u'api': CLASSROOM,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.googleapis.com/auth/classroom.profile.photos'},
  {u'name': u'Classroom API - Rosters',
   u'api': CLASSROOM,
   u'credfam': FAM2_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/classroom.rosters'},
  {u'name': u'Cloudprint API',
   u'api': CLOUDPRINT,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.googleapis.com/auth/cloudprint'},
  {u'name': u'Cloud Storage (Vault Export - read only)',
   u'api': STORAGE,
   u'subscopes': [],
   u'credfam': FAM2_SCOPES,
   u'scope': u'https://www.googleapis.com/auth/devstorage.read_only'},
  {u'name': u'Contacts API - Domain Shared and Users and GAL',
   u'api': CONTACTS,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.google.com/m8/feeds'},
  {u'name': u'Data Transfer API',
   u'api': DATATRANSFER,
   u'credfam': FAM1_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/admin.datatransfer'},
  {u'name': u'Directory API - Chrome OS Devices',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/admin.directory.device.chromeos'},
  {u'name': u'Directory API - Customers',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/admin.directory.customer'},
  {u'name': u'Directory API - Domains',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/admin.directory.domain'},
  {u'name': u'Directory API - Groups',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/admin.directory.group'},
  {u'name': u'Directory API - Mobile Devices Directory',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': [u'readonly', u'action'],
   u'scope': u'https://www.googleapis.com/auth/admin.directory.device.mobile'},
  {u'name': u'Directory API - Notifications',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.googleapis.com/auth/admin.directory.notifications'},
  {u'name': u'Directory API - Organizational Units',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/admin.directory.orgunit'},
  {u'name': u'Directory API - Resource Calendars',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/admin.directory.resource.calendar'},
  {u'name': u'Directory API - Roles',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/admin.directory.rolemanagement'},
  {u'name': u'Directory API - User Schemas',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/admin.directory.userschema'},
  {u'name': u'Directory API - User Security',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.googleapis.com/auth/admin.directory.user.security'},
  {u'name': u'Directory API - Users',
   u'api': DIRECTORY,
   u'credfam': FAM1_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/admin.directory.user'},
  {u'name': u'Email Audit API',
   u'api': EMAIL_AUDIT,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'scope': u'https://apps-apis.google.com/a/feeds/compliance/audit/'},
  {u'name': u'Email Settings API - Users',
   u'api': EMAIL_SETTINGS,
   u'credfam': FAM1_SCOPES,
   u'subscopes': [],
   u'scope': u'https://apps-apis.google.com/a/feeds/emailsettings/2.0/'},
  {u'name': u'Groups Migration API',
   u'api': GROUPSMIGRATION,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.googleapis.com/auth/apps.groups.migration'},
  {u'name': u'Groups Settings API',
   u'api': GROUPSSETTINGS,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.googleapis.com/auth/apps.groups.settings'},
  {u'name': u'License Manager API',
   u'api': LICENSING,
   u'credfam': FAM1_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.googleapis.com/auth/apps.licensing'},
  {u'name': u'People API',
   u'api': PEOPLE,
   u'credfam': FAM2_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/contacts'},
  {u'name': u'Reports API - Audit Reports',
   u'api': REPORTS,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.googleapis.com/auth/admin.reports.audit.readonly'},
  {u'name': u'Reports API - Usage Reports',
   u'api': REPORTS,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.googleapis.com/auth/admin.reports.usage.readonly'},
  {u'name': u'Reseller API',
   u'api': RESELLER,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'offByDefault': True,
   u'scope': u'https://www.googleapis.com/auth/apps.order'},
  {u'name': u'Site Verification API',
   u'api': SITEVERIFICATION,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'scope': u'https://www.googleapis.com/auth/siteverification'},
  {u'name': u'Sites API',
   u'api': SITES,
   u'credfam': FAM2_SCOPES,
   u'subscopes': [],
   u'scope': u'https://sites.google.com/feeds'},
  {u'name': u'Vault API',
   u'api': VAULT,
   u'credfam': FAM2_SCOPES,
   u'subscopes': READONLY,
   u'scope': u'https://www.googleapis.com/auth/ediscovery'},
  ]

DRIVE3_TO_DRIVE2_ABOUT_FIELDS_MAP = {
  u'displayName': u'name',
  u'limit': u'quotaBytesTotal',
  u'usage': u'quotaBytesUsedAggregate',
  u'usageInDrive': u'quotaBytesUsed',
  u'usageInDriveTrash': u'quotaBytesUsedInTrash',
  }

DRIVE3_TO_DRIVE2_CAPABILITIES_FIELDS_MAP = {
  u'canComment': u'canComment',
  u'canReadRevisions': u'canReadRevisions',
  u'canCopy': u'copyable',
  u'canEdit': u'editable',
  u'canShare': u'shareable',
  }

DRIVE3_TO_DRIVE2_CAPABILITIES_NAMES_MAP = {
  u'canChangeViewersCanCopyContent': u'canChangeRestrictedDownload',
  }

DRIVE3_TO_DRIVE2_CAPABILITIES_TITLES_MAP = {
  u'capabilities.canComment': u'canComment',
  u'capabilities.canReadRevisions': u'canReadRevisions',
  u'capabilities.canCopy': u'copyable',
  u'capabilities.canEdit': u'editable',
  u'capabilities.canShare': u'shareable',
  }

DRIVE3_TO_DRIVE2_FILES_FIELDS_MAP = {
  u'allowFileDiscovery': u'withLink',
  u'createdTime': u'createdDate',
  u'expirationTime': u'expirationDate',
  u'modifiedByMe': u'modified',
  u'modifiedByMeTime': u'modifiedByMeDate',
  u'modifiedTime': u'modifiedDate',
  u'name': u'title',
  u'sharedWithMeTime': u'sharedWithMeDate',
  u'size': u'fileSize',
  u'trashedTime': u'trashedDate',
  u'viewedByMe': u'viewed',
  u'viewedByMeTime': u'lastViewedByMeDate',
  u'webViewLink': u'alternateLink',
  }

DRIVE3_TO_DRIVE2_LABELS_MAP = {
  u'modifiedByMe': u'modified',
  u'starred': u'starred',
  u'trashed': u'trashed',
  u'viewedByMe': u'viewed',
  }

DRIVE3_TO_DRIVE2_REVISIONS_FIELDS_MAP = {
  u'modifiedTime': u'modifiedDate',
  u'keepForever': u'pinned',
  u'size': u'fileSize',
  }

def getVersion(api):
  version = _INFO[api][u'version']
  cred_family = _INFO[api][u'credfam']
  if api in [DIRECTORY, REPORTS, DATATRANSFER]:
    api = ADMIN
  elif api == DRIVE3:
    api = DRIVE
  return (api, version, u'{0}-{1}'.format(api, version), cred_family)

def getClientScopesSet(api):
  return set([scope[u'scope'] for scope in OAUTH2_SCOPES if scope[u'api'] == api])

def getSortedSvcAcctScopesList():
  all_scopes = []
  for api in _INFO:
    for scope in _INFO[api].get(u'svcacctscopes', []):
      if scope not in all_scopes:
        all_scopes.append(scope)
  all_scopes.sort()
  return (all_scopes, len(all_scopes))

def getSvcAcctScopesSet(api):
  return set(_INFO[api][u'svcacctscopes'])

def hasLocalJSON(api):
  return _INFO[api].get(u'localjson', False)
