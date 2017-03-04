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

"""GAM entity processing

"""

class GamEntity(object):

  ROLE_MANAGER = 'MANAGER'
  ROLE_MEMBER = 'MEMBER'
  ROLE_OWNER = 'OWNER'
  ROLE_USER = 'USER'
  ROLE_MANAGER_MEMBER = ','.join([ROLE_MANAGER, ROLE_MEMBER])
  ROLE_MANAGER_OWNER = ','.join([ROLE_MANAGER, ROLE_OWNER])
  ROLE_MEMBER_OWNER = ','.join([ROLE_MEMBER, ROLE_OWNER])
  ROLE_MANAGER_MEMBER_OWNER = ','.join([ROLE_MANAGER, ROLE_MEMBER, ROLE_OWNER])

# Keys into NAMES; arbitrary values but must be unique
  ACCESS_TOKEN = 'atok'
  ACCOUNT = 'acct'
  ACTION = 'actn'
  ACTIVITY = 'actv'
  ADMINISTRATOR = 'admi'
  ALIAS = 'alia'
  ALIAS_EMAIL = 'alie'
  ALIAS_TARGET = 'alit'
  API = 'api '
  APPLICATION_SPECIFIC_PASSWORD = 'aspa'
  ARROWS_ENABLED = 'arro'
  ATTENDEE = 'atnd'
  AUDIT_ACTIVITY_REQUEST = 'auda'
  AUDIT_EXPORT_REQUEST = 'audx'
  AUDIT_MONITOR_REQUEST = 'audm'
  BACKUP_VERIFICATION_CODES = 'buvc'
  CALENDAR = 'cale'
  CALENDAR_ACL = 'cacl'
  CALENDAR_SETTINGS = 'cset'
  CLIENT_SECRETS_JSON_FILE = 'clis'
  CONFIG_FILE = 'conf'
  CONTACT = 'cont'
  CONTACT_GROUP = 'cogr'
  CONTACT_GROUP_NAME = 'cogn'
  COURSE = 'cour'
  COURSE_ALIAS = 'coal'
  COURSE_ID = 'coid'
  CUSTOMER_ID = 'cust'
  CREDENTIALS = 'cred'
  CRITERIA = 'crit'
  CROS_DEVICE = 'cros'
  CUSTOMER_DOMAIN = 'cudo'
  CUSTOMER_ID = 'cuid'
  DEFAULT_LANGUAGE = 'dfla'
  DELEGATE = 'dele'
  DELEGATOR = 'delo'
  DELETED_USER = 'delu'
  DISCOVERY_JSON_FILE = 'disc'
  DOMAIN = 'doma'
  DOMAIN_ALIAS = 'doal'
  DRIVE_FILE = 'file'
  DRIVE_FILE_ID = 'fili'
  DRIVE_FILE_NAME = 'filn'
  DRIVE_FILE_OR_FOLDER = 'fifo'
  DRIVE_FILE_OR_FOLDER_ACL = 'fiac'
  DRIVE_FILE_OR_FOLDER_ID = 'fifi'
  DRIVE_FOLDER = 'fold'
  DRIVE_FOLDER_ID = 'foli'
  DRIVE_FOLDER_NAME = 'foln'
  DRIVE_PATH = 'drvp'
  DRIVE_SETTINGS = 'drvs'
  DRIVE_TRASH = 'drvt'
  EMAIL = 'emai'
  EMAIL_ALIAS = 'emal'
  EMAIL_SETTINGS = 'emse'
  ENTITY = 'enti'
  EVENT = 'evnt'
  FIELD = 'fiel'
  FILTER = 'filt'
  FORWARD_ENABLED = 'fwde'
  FORWARDING_ADDRESS = 'fwda'
  GMAIL_PROFILE = 'gmpr'
  GPLUS_PROFILE = 'gppr'
  GROUP = 'grou'
  GROUP_ALIAS = 'gali'
  GROUP_EMAIL = 'gale'
  GROUP_MEMBERSHIP = 'gmem'
  GROUP_SETTINGS = 'gset'
  GUARDIAN = 'guar'
  GUARDIAN_INVITATION = 'gari'
  IMAP_ENABLED = 'imap'
  INSTANCE = 'inst'
  ITEM = 'item'
  ISSUER_CN = 'issu'
  KEYBOARD_SHORTCUTS_ENABLED = 'kbsc'
  LABEL = 'labe'
  LANGUAGE = 'lang'
  LICENSE = 'lice'
  LOGO = 'logo'
  MEMBER = 'memb'
  MESSAGE = 'mesg'
  MOBILE_DEVICE = 'mobi'
  NOTIFICATION = 'noti'
  OAUTH2_TXT_FILE = 'oaut'
  OAUTH2SERVICE_JSON_FILE = 'oau2'
  ORGANIZATIONAL_UNIT = 'orgu'
  PAGE_SIZE = 'page'
  PARENT_ORGANIZATIONAL_UNIT = 'porg'
  PARTICIPANT = 'part'
  PERMISSION = 'perm'
  PERMISSION_ID = 'peid'
  PERMITTEE = 'prmt'
  PHOTO = 'phot'
  POP_ENABLED = 'popa'
  PRINTER = 'prin'
  PRINTER_ACL = 'pacl'
  PRINTJOB = 'prjo'
  PRODUCT = 'prod'
  PROFILE_SHARING_ENABLED = 'prof'
  PROJECT = 'proj'
  QUERY = 'quer'
  REPORT = 'rept'
  REQUEST_ID = 'reqi'
  RESOURCE_CALENDAR = 'resc'
  RESOURCE_ID = 'resi'
  REVISION_ID = 'revi'
  ROLE = 'role'
  ROLE_ASSIGNMENT_ID = 'raid'
  SCOPE = 'scop'
  SECTION = 'sect'
  SENDAS_ADDRESS = 'sasa'
  SERVICE = 'serv'
  SIGNATURE = 'sign'
  SITE = 'site'
  SITE_ACL = 'sacl'
  SKU = 'sku '
  SMIME_ID = 'smid'
  SNIPPETS_ENABLED = 'snip'
  SSO_KEY = 'ssok'
  SSO_SETTINGS = 'ssos'
  SOURCE_USER = 'srcu'
  STUDENT = 'stud'
  SUBSCRIPTION = 'subs'
  TARGET_USER = 'tgtu'
  TEACHER = 'teac'
  THREAD = 'thre'
  TOKEN = 'tokn'
  TRANSFER_ID = 'trid'
  TRANSFER_REQUEST = 'trnr'
  UNICODE_ENCODING_ENABLED = 'unic'
  UNIQUE_ID = 'uniq'
  USER = 'user'
  USER_ALIAS = 'uali'
  USER_EMAIL = 'ual'
  USER_SCHEMA = 'usch'
  VACATION = 'vaca'
  VACATION_ENABLED = 'vace'
  VALUE = 'valu'
  WEBCLIPS_ENABLED = 'webc'
  # _NAMES[0] is plural, _NAMES[1] is singular unless the item name is explicitly plural (Calendar Settings)
  # For items with Boolean values, both entries are singular (Forward, POP)
  # These values can be translated into other languages
  _NAMES = {
    ACCESS_TOKEN: ['Access Tokens', 'Access Token'],
    ACCOUNT: ['G Suite Accounts', 'G Suite Account'],
    ACTION: ['Actions', 'Action'],
    ACTIVITY: ['Activities', 'Activity'],
    ADMINISTRATOR: ['Administrators', 'Administrator'],
    ALIAS: ['Aliases', 'Alias'],
    ALIAS_EMAIL: ['Alias Emails', 'Alias Email'],
    ALIAS_TARGET: ['Alias Targets', 'Alias Target'],
    API: ['APIs', 'API'],
    APPLICATION_SPECIFIC_PASSWORD: ['Application Specific Passwords', 'Application Specific Password'],
    ARROWS_ENABLED: ['Personal Indicator Arrows Enabled', 'Personal Indicator Arrows Enabled'],
    ATTENDEE: ['Attendees', 'Attendee'],
    AUDIT_ACTIVITY_REQUEST: ['Audit Activity Requests', 'Audit Activity Request'],
    AUDIT_EXPORT_REQUEST: ['Audit Export Requests', 'Audit Export Request'],
    AUDIT_MONITOR_REQUEST: ['Audit Monitor Requests', 'Audit Monitor Request'],
    BACKUP_VERIFICATION_CODES: ['Backup Verification Codes', 'Backup Verification Codes'],
    CALENDAR: ['Calendars', 'Calendar'],
    CALENDAR_ACL: ['Calendar ACLs', 'Calendar ACL'],
    CALENDAR_SETTINGS: ['Calendar Settings', 'Calendar Settings'],
    CLIENT_SECRETS_JSON_FILE: ['Client Secrets File', 'Client Secrets File'],
    CONFIG_FILE: ['Config File', 'Config File'],
    CONTACT: ['Contacts', 'Contact'],
    CONTACT_GROUP: ['Contact Groups', 'Contact Group'],
    CONTACT_GROUP_NAME: ['Contact Group Names', 'Contact Group Name'],
    COURSE: ['Courses', 'Course'],
    COURSE_ALIAS: ['Course Aliases', 'Course Alias'],
    COURSE_ID: ['Course IDs', 'Course ID'],
    CUSTOMER_DOMAIN: ['Customer Domains', 'Customer Domain'],
    CUSTOMER_ID: ['Customer IDs', 'Customer ID'],
    CREDENTIALS: ['Credentials', 'Credentials'],
    CRITERIA: ['Criteria', 'Criteria'],
    CROS_DEVICE: ['CrOS Devices', 'CrOS Device'],
    CUSTOMER_ID: ['Customer IDs', 'Customer ID'],
    DEFAULT_LANGUAGE: ['Default Language', 'Default Language'],
    DELEGATE: ['Delegates', 'Delegate'],
    DELEGATOR: ['Delegators', 'Delegator'],
    DELETED_USER: ['Deleted Users', 'Deleted User'],
    DISCOVERY_JSON_FILE: ['Discovery File', 'Discovery File'],
    DOMAIN: ['Domains', 'Domain'],
    DOMAIN_ALIAS: ['Domain Aliases', 'Domain Alias'],
    DRIVE_FILE: ['Drive Files', 'Drive File'],
    DRIVE_FILE_ID: ['Drive File IDs', 'Drive File ID'],
    DRIVE_FILE_NAME: ['Drive File Names', 'Drive File Name'],
    DRIVE_FILE_OR_FOLDER: ['Drive Files/Folders', 'Drive File/Folder'],
    DRIVE_FILE_OR_FOLDER_ACL: ['Drive File/Folder ACLs', 'Drive File/Folder ACL'],
    DRIVE_FILE_OR_FOLDER_ID: ['Drive File/Folder IDs', 'Drive File/Folder ID'],
    DRIVE_FOLDER: ['Drive Folders', 'Drive Folder'],
    DRIVE_FOLDER_ID: ['Drive Folder IDs', 'Drive Folder ID'],
    DRIVE_FOLDER_NAME: ['Drive Folder Names', 'Drive Folder Name'],
    DRIVE_PATH: ['Drive Paths', 'Drive Path'],
    DRIVE_SETTINGS: ['Drive Settings', 'Drive Settings'],
    DRIVE_TRASH: ['Drive Trash', 'Drive Trash'],
    EMAIL: ['Email Addresses', 'Email Address'],
    EMAIL_ALIAS: ['Email Aliases', 'Email Alias'],
    EMAIL_SETTINGS: ['Email Settings', 'Email Settings'],
    ENTITY: ['Entities', 'Entity'],
    EVENT: ['Events', 'Event'],
    FIELD: ['Fields', 'Field'],
    FILTER: ['Filters', 'Filter'],
    FORWARD_ENABLED: ['Forward Enabled', 'Forward Enabled'],
    FORWARDING_ADDRESS: ['Forwarding Addresses', 'Forwarding Address'],
    GMAIL_PROFILE: ['Gmail profile', 'Gmail profile'],
    GPLUS_PROFILE: ['Gplus profile', 'Gplus profile'],
    GROUP: ['Groups', 'Group'],
    GROUP_ALIAS: ['Group Aliases', 'Group Alias'],
    GROUP_EMAIL: ['Group Emails', 'Group Email'],
    GROUP_MEMBERSHIP: ['Group Memberships', 'Group Membership'],
    GROUP_SETTINGS: ['Group Settings', 'Group Settings'],
    GUARDIAN: ['Guardians', 'Guardian'],
    GUARDIAN_INVITATION: ['Guardian Invitations', 'Guardian Invitation'],
    IMAP_ENABLED: ['IMAP Enabled', 'IMAP Enabled'],
    INSTANCE: ['Instances', 'Instance'],
    ISSUER_CN: ['Issuer CNs', 'Issuer CN'],
    ITEM: ['Items', 'Item'],
    KEYBOARD_SHORTCUTS_ENABLED: ['Keyboard Shortcuts Enabled', 'Keyboard Shortcuts Enabled'],
    LABEL: ['Labels', 'Label'],
    LANGUAGE: ['Languages', 'Language'],
    LICENSE: ['Licenses', 'License'],
    LOGO: ['Logos', 'Logo'],
    MEMBER: ['Members', 'Member'],
    MESSAGE: ['Messages', 'Message'],
    MOBILE_DEVICE: ['Mobile Devices', 'Mobile Device'],
    NOTIFICATION: ['Notifications', 'Notification'],
    OAUTH2_TXT_FILE: ['Client OAuth2 File', 'Client OAuth2 File'],
    OAUTH2SERVICE_JSON_FILE: ['Service Account OAuth2 File', 'Service Account OAuth2 File'],
    ORGANIZATIONAL_UNIT: ['Organizational Units', 'Organizational Unit'],
    PAGE_SIZE: ['Page Size', 'Page Size'],
    PARENT_ORGANIZATIONAL_UNIT: ['Parent Organizational Units', 'Parent Organizational Unit'],
    PARTICIPANT: ['Participants', 'Participant'],
    PERMISSION: ['Permissions', 'Permission'],
    PERMISSION_ID: ['Permission IDs', 'Permission ID'],
    PERMITTEE: ['Permittees', 'Permittee'],
    PHOTO: ['Photos', 'Photo'],
    POP_ENABLED: ['POP Enabled', 'POP Enabled'],
    PRINTER: ['Printers', 'Printer'],
    PRINTER_ACL: ['Printer ACLs', 'Printer ACL'],
    PRINTJOB: ['Print Jobs', 'Print Job'],
    PRODUCT: ['Products', 'Product'],
    PROFILE_SHARING_ENABLED: ['Profile Sharing Enabled', 'Profile Sharing Enabled'],
    PROJECT: ['Projects', 'Project'],
    QUERY: ['Queries', 'Query'],
    REPORT: ['Reports', 'Report'],
    REQUEST_ID: ['Request IDs', 'Request ID'],
    RESOURCE_CALENDAR: ['Resource Calendars', 'Resource Calendar'],
    RESOURCE_ID: ['Resource IDs', 'Resource ID'],
    REVISION_ID: ['Revision IDs', 'Revision ID'],
    ROLE: ['Roles', 'Role'],
    ROLE_ASSIGNMENT_ID: ['Role Assignment IDs', 'Role Assignment ID'],
    SCOPE: ['Scopes', 'Scope'],
    SECTION: ['Sections', 'Section'],
    SENDAS_ADDRESS: ['SendAs Addresses', 'SendAs Address'],
    SERVICE: ['Services', 'Service'],
    SIGNATURE: ['Signatures', 'Signature'],
    SITE: ['Sites', 'Site'],
    SITE_ACL: ['Site ACLs', 'Site ACL'],
    SKU: ['SKUs', 'SKU'],
    SMIME_ID: ['S/MIME Certificate IDs', 'S/MIME Certificate ID'],
    SNIPPETS_ENABLED: ['Preview Snippets Enabled', 'Preview Snippets Enabled'],
    SSO_KEY: ['SSO Key', 'SSO Key'],
    SSO_SETTINGS: ['SSO Settings', 'SSO Settings'],
    SOURCE_USER: ['Source Users', 'Source User'],
    SUBSCRIPTION: ['Subscriptions', 'Subscription'],
    STUDENT: ['Students', 'Student'],
    TARGET_USER: ['Target Users', 'Target User'],
    TEACHER: ['Teachers', 'Teacher'],
    THREAD: ['Threads', 'Thread'],
    TOKEN: ['Tokens', 'Token'],
    TRANSFER_ID: ['Transfer IDs', 'Transfer ID'],
    TRANSFER_REQUEST: ['Transfer Requests', 'Transfer Request'],
    UNICODE_ENCODING_ENABLED: ['UTF-8 Encoding Enabled', 'UTF-8 Encoding Enabled'],
    UNIQUE_ID: ['Unique IDs', 'Unique ID'],
    USER: ['Users', 'User'],
    USER_ALIAS: ['User Aliases', 'User Alias'],
    USER_EMAIL: ['User Emails', 'User Email'],
    USER_SCHEMA: ['Schemas', 'Schema'],
    VACATION: ['Vacation', 'Vacation'],
    VACATION_ENABLED: ['Vacation Enabled', 'Vacation Enabled'],
    VALUE: ['Values', 'Value'],
    WEBCLIPS_ENABLED: ['Web Clips Enabled', 'Web Clips Enabled'],
    ROLE_MANAGER: ['Managers', 'Manager'],
    ROLE_MEMBER: ['Members', 'Member'],
    ROLE_OWNER: ['Owners', 'Owner'],
    ROLE_USER: ['Users', 'User'],
    ROLE_MANAGER_MEMBER: ['Members, Managers', 'Member, Manager'],
    ROLE_MANAGER_OWNER: ['Managers, Owners', 'Manager, Owner'],
    ROLE_MEMBER_OWNER: ['Members, Owners', 'Member, Owner'],
    ROLE_MANAGER_MEMBER_OWNER: ['Members, Managers, Owners', 'Member, Manager, Owner'],
    }

  def __init__(self):
    self.entityType = None
    self.forWhom = None
    self.showTotal = False

  def SetGetting(self, entityType):
    self.entityType = entityType

  def Getting(self):
    return self.entityType

  def SetGettingForWhom(self, forWhom):
    self.forWhom = forWhom

  def GettingForWhom(self):
    return self.forWhom

  def SetGettingShowTotal(self, showTotal):
    self.showTotal = showTotal

  def GettingShowTotal(self):
    return self.showTotal

  def Choose(self, entityType, count):
    return self._NAMES[entityType][[0, 1][count == 1]]

  def ChooseGetting(self, count):
    return self._NAMES[self.entityType][[0, 1][count == 1]]

  def Plural(self, entityType):
    return self._NAMES[entityType][0]

  def PluralGetting(self):
    return self._NAMES[self.entityType][0]

  def Singular(self, entityType):
    return self._NAMES[entityType][1]

  def SingularGetting(self):
    return self._NAMES[self.entityType][1]

  def FormatEntityValueList(self, entityValueList):
    evList = []
    for j in range(0, len(entityValueList), 2):
      evList.append(self.Singular(entityValueList[j]))
      evList.append(entityValueList[j+1])
    return evList

  def EntityTypeName(self, entityType, entityName):
    return '{0}: {1}'.format(self.Singular(entityType), entityName)

  def EntityTypeNameMessage(self, entityType, entityName, message):
    return '{0}: {1} {2}'.format(self.Singular(entityType), entityName, message)

