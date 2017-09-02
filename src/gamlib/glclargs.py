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

"""GAM command line argument processing

"""

class GamCLArgs(object):

# GAM entity types as specified on the command line
  ENTITY_COURSEPARTICIPANTS = u'courseparticipants'
  ENTITY_CROS = u'cros'
  ENTITY_CROS_QUERY = u'crosquery'
  ENTITY_CROS_OU = u'cros_ou'
  ENTITY_CROS_OU_AND_CHILDREN = u'cros_ou_and_children'
  ENTITY_CROS_OUS = u'cros_ous'
  ENTITY_CROS_OUS_AND_CHILDREN = u'cros_ous_and_children'
  ENTITY_GROUP = u'group'
  ENTITY_GROUPS = u'groups'
  ENTITY_GROUP_USERS = u'group_users'
  ENTITY_LICENSES = u'licenses'
  ENTITY_OU = u'ou'
  ENTITY_OU_AND_CHILDREN = u'ou_and_children'
  ENTITY_OUS = u'ous'
  ENTITY_OUS_AND_CHILDREN = u'ous_and_children'
  ENTITY_QUERY = u'query'
  ENTITY_STUDENTS = u'students'
  ENTITY_TEACHERS = u'teachers'
  ENTITY_USER = u'user'
  ENTITY_USERS = u'users'
#
  CROS_ENTITIES = [
    ENTITY_CROS,
    ENTITY_CROS_QUERY,
    ENTITY_CROS_OU,
    ENTITY_CROS_OU_AND_CHILDREN,
    ENTITY_CROS_OUS,
    ENTITY_CROS_OUS_AND_CHILDREN,
    ]
  USER_ENTITIES = [
    ENTITY_COURSEPARTICIPANTS,
    ENTITY_GROUP,
    ENTITY_GROUPS,
    ENTITY_GROUP_USERS,
    ENTITY_LICENSES,
    ENTITY_OU,
    ENTITY_OU_AND_CHILDREN,
    ENTITY_OUS,
    ENTITY_OUS_AND_CHILDREN,
    ENTITY_QUERY,
    ENTITY_STUDENTS,
    ENTITY_TEACHERS,
    ENTITY_USER,
    ENTITY_USERS,
    ]
# Aliases for CL entity types
  ENTITY_ALIAS_MAP = {
    u'crosorg': ENTITY_CROS_OU,
    u'crosorg_and_child': ENTITY_CROS_OU_AND_CHILDREN,
    u'crosorg_and_children': ENTITY_CROS_OU_AND_CHILDREN,
    u'crosorgs': ENTITY_CROS_OUS,
    u'crosorgs_and_child': ENTITY_CROS_OUS_AND_CHILDREN,
    u'crosorgs_and_children': ENTITY_CROS_OUS_AND_CHILDREN,
    u'crosou_and_child': ENTITY_CROS_OU_AND_CHILDREN,
    u'crosou_and_childen': ENTITY_CROS_OU_AND_CHILDREN,
    u'crosous_and_child': ENTITY_CROS_OUS_AND_CHILDREN,
    u'cros_org': ENTITY_CROS_OU,
    u'cros_org_and_child': ENTITY_CROS_OU_AND_CHILDREN,
    u'cros_org_and_children': ENTITY_CROS_OU_AND_CHILDREN,
    u'cros_orgs': ENTITY_CROS_OUS,
    u'cros_orgs_and_child': ENTITY_CROS_OUS_AND_CHILDREN,
    u'cros_orgs_and_children': ENTITY_CROS_OUS_AND_CHILDREN,
    u'cros_ou_and_child': ENTITY_CROS_OU_AND_CHILDREN,
    u'cros_ou_and_childen': ENTITY_CROS_OU_AND_CHILDREN,
    u'cros_ous_and_child': ENTITY_CROS_OUS_AND_CHILDREN,
    u'license': ENTITY_LICENSES,
    u'licence': ENTITY_LICENSES,
    u'licences': ENTITY_LICENSES,
    u'org': ENTITY_OU,
    u'org_and_child': ENTITY_OU_AND_CHILDREN,
    u'org_and_children': ENTITY_OU_AND_CHILDREN,
    u'orgs': ENTITY_OUS,
    u'orgs_and_child': ENTITY_OUS_AND_CHILDREN,
    u'orgs_and_children': ENTITY_OUS_AND_CHILDREN,
    u'ou_and_child': ENTITY_OU_AND_CHILDREN,
    u'ous_and_child': ENTITY_OUS_AND_CHILDREN,
    }
# CL entity source selectors
  ENTITY_SELECTOR_ALL = u'all'
  ENTITY_SELECTOR_CSV = u'csv'
  ENTITY_SELECTOR_CSVFILE = u'csvfile'
  ENTITY_SELECTOR_FILE = u'file'
  ENTITY_SELECTOR_DATAFILE = u'datafile'
  ENTITY_SELECTOR_CROSCSV = u'croscsv'
  ENTITY_SELECTOR_CROSCSVFILE = u'croscsvfile'
  ENTITY_SELECTOR_CROSFILE = u'crosfile'
  ENTITY_SELECTOR_CSVKMD = u'csvkmd'
  ENTITY_SELECTOR_CSVSUBKEY = u'csvsubkey'
  ENTITY_SELECTOR_CSVDATA = u'csvdata'
  ENTITY_SELECTOR_CROSCSVDATA = u'croscsvdata'
#
  CROS_ENTITY_SELECTORS = [
    ENTITY_SELECTOR_CROSCSV,
    ENTITY_SELECTOR_CROSCSVFILE,
    ENTITY_SELECTOR_CROSFILE,
    ]
  ENTITY_SELECTORS = [
    ENTITY_SELECTOR_ALL,
    ENTITY_SELECTOR_CSV,
    ENTITY_SELECTOR_CSVFILE,
    ENTITY_SELECTOR_FILE,
    ENTITY_SELECTOR_DATAFILE,
    ENTITY_SELECTOR_CSVKMD,
    ENTITY_SELECTOR_CSVSUBKEY,
    ]
  CROS_CSVDATA_ENTITY_SELECTORS = [
    ENTITY_SELECTOR_CROSCSVDATA,
    ]
  CSVDATA_ENTITY_SELECTORS = [
    ENTITY_SELECTOR_CSVDATA,
    ]
# Allowed values for CL source selector all
  CROS_ENTITY_SELECTOR_ALL_SUBTYPES = [
    ENTITY_CROS,
    ]
  USER_ENTITY_SELECTOR_ALL_SUBTYPES = [
    ENTITY_USERS,
    ]
#
  ENTITY_ALL_CROS = ENTITY_SELECTOR_ALL+u' '+ENTITY_CROS
  ENTITY_ALL_USERS = ENTITY_SELECTOR_ALL+u' '+ENTITY_USERS
#
  ENTITY_SELECTOR_ALL_SUBTYPES_MAP = {
    ENTITY_CROS: ENTITY_ALL_CROS,
    ENTITY_USERS: ENTITY_ALL_USERS,
    }
# Allowed values for CL source selector datafile, csvkmd
  CROS_ENTITY_SELECTOR_DATAFILE_CSVKMD_SUBTYPES = [
    ENTITY_CROS,
    ENTITY_CROS_OUS,
    ENTITY_CROS_OUS_AND_CHILDREN,
    ]
  USER_ENTITY_SELECTOR_DATAFILE_CSVKMD_SUBTYPES = [
    ENTITY_USERS,
    ENTITY_GROUPS,
    ENTITY_GROUP_USERS,
    ENTITY_OUS,
    ENTITY_OUS_AND_CHILDREN,
    ENTITY_COURSEPARTICIPANTS,
    ENTITY_STUDENTS,
    ENTITY_TEACHERS,
    ]
# Batch file commands
  GAM_CMD = u'gam'
  COMMIT_BATCH_CMD = u'commit-batch'
  PRINT_CMD = u'print'
# Command line batch/csv/loop/tbatch keywords
  BATCH_CMD = u'batch'
  CSV_CMD = u'csv'
  LOOP_CMD = u'loop'
  TBATCH_CMD = u'tbatch'
# Command line select/config/redirect arguments
  SELECT_CMD = u'select'
  CONFIG_CMD = u'config'
  REDIRECT_CMD = u'redirect'
  GAM_META_COMMANDS = [SELECT_CMD, CONFIG_CMD, REDIRECT_CMD,]
# Command line arguments
  ARG_3LO = u'3lo'
  ARG_ACL = u'acl'
  ARG_ACLS = u'acls'
  ARG_ADMIN = u'admin'
  ARG_ADMINS = u'admins'
  ARG_ADMINROLES = u'adminroles'
  ARG_ALIAS = u'alias'
  ARG_ALIASES = u'aliases'
  ARG_APPLICATIONSPECIFICPASSWORDS = u'applicationspecificpasswords'
  ARG_ASP = u'asp'
  ARG_ASPS = u'asps'
  ARG_BACKUPCODE = u'backupcode'
  ARG_BACKUPCODES = u'backupcodes'
  ARG_CALATTENDEES = u'calattendees'
  ARG_CALENDAR = u'calendar'
  ARG_CALENDARS = u'calendars'
  ARG_CALENDARACL = u'calendaracl'
  ARG_CALENDARACLS = u'calendaracls'
  ARG_CALSETTINGS = u'calsettings'
  ARG_CONTACT = u'contact'
  ARG_CONTACTS = u'contacts'
  ARG_CONTACT_GROUP = u'contactgroup'
  ARG_CONTACT_GROUPS = u'contactgroups'
  ARG_COURSE = u'course'
  ARG_COURSES = u'courses'
  ARG_COURSE_PARTICIPANTS = u'course-participants'
  ARG_CROS = u'cros'
  ARG_CROSES = u'croses'
  ARG_CROS_ACTIVITY = u'crosactivity'
  ARG_CUSTOMER = u'customer'
  ARG_DATA_TRANSFER = u'datatransfer'
  ARG_DATA_TRANSFERS = u'datatransfers'
  ARG_DELEGATE = u'delegate'
  ARG_DELEGATES = u'delegates'
  ARG_DOMAIN = u'domain'
  ARG_DOMAINS = u'domains'
  ARG_DOMAIN_ALIAS = u'domainalias'
  ARG_DOMAIN_ALIASES = u'domainaliases'
  ARG_DRIVE = u'drive'
  ARG_DRIVEACTIVITY = u'driveactivity'
  ARG_DRIVEFILE = u'drivefile'
  ARG_DRIVEFILEACL = u'drivefileacl'
  ARG_DRIVEFILEACLS = u'drivefileacls'
  ARG_DRIVESETTINGS = u'drivesettings'
  ARG_DRIVETRASH = u'drivetrash'
  ARG_EMPTYDRIVEFOLDERS = u'emptydrivefolders'
  ARG_EVENT = u'event'
  ARG_EVENTS = u'events'
  ARG_FILEINFO = u'fileinfo'
  ARG_FILELIST = u'filelist'
  ARG_FILEPATH = u'filepath'
  ARG_FILEPATHS = u'filepaths'
  ARG_FILEREVISION = u'filerevision'
  ARG_FILEREVISIONS = u'filerevisions'
  ARG_FILETREE = u'filetree'
  ARG_FILTER = u'filter'
  ARG_FILTERS = u'filters'
  ARG_FORWARD = u'forward'
  ARG_FORWARDINGADDRESS = u'forwardingaddress'
  ARG_FORWARDINGADDRESSES = u'forwardingaddresses'
  ARG_GAL = u'gal'
  ARG_GMAILPROFILE = u'gmailprofile'
  ARG_GPLUSPROFILE = u'gplusprofile'
  ARG_GROUP = u'group'
  ARG_GROUPS = u'groups'
  ARG_GROUP_MEMBERS = u'group-members'
  ARG_GUARDIAN = u'guardian'
  ARG_GUARDIANS = u'guardians'
  ARG_GUARDIAN_INVITATION = u'guardianinvitation'
  ARG_GUARDIAN_INVITATIONS = u'guardianinvitations'
  ARG_HOLD = u'hold'
  ARG_HOLDS = u'holds'
  ARG_IMAP = u'imap'
  ARG_IMAP4 = u'imap4'
  ARG_INSTANCE = u'instance'
  ARG_LABEL = u'label'
  ARG_LABELS = u'labels'
  ARG_LABELSETTINGS = u'labelsettings'
  ARG_LICENCE = u'licence'
  ARG_LICENCES = u'licences'
  ARG_LICENSE = u'license'
  ARG_LICENSES = u'licenses'
  ARG_LOGO = u'logo'
  ARG_MATTER = u'matter'
  ARG_MATTERS = u'matters'
  ARG_MESSAGE = u'message'
  ARG_MESSAGES = u'messages'
  ARG_MOBILE = u'mobile'
  ARG_MOBILES = u'mobiles'
  ARG_NOTE = u'note'
  ARG_NOTIFICATION = u'notification'
  ARG_OAUTH = u'oauth'
  ARG_ORG = u'org'
  ARG_ORGS = u'orgs'
  ARG_ORGTREE = u'orgtree'
  ARG_ORPHANS = u'orphans'
  ARG_OWNERSHIP = u'ownership'
  ARG_PERMISSIONS = u'permissions'
  ARG_PHOTO = u'photo'
  ARG_POP = u'pop'
  ARG_POP3 = u'pop3'
  ARG_PRINTER = u'printer'
  ARG_PRINTERS = u'printers'
  ARG_PRINTJOBS = u'printjobs'
  ARG_PROFILE = u'profile'
  ARG_PROJECT = u'project'
  ARG_PROJECTS = u'projects'
  ARG_RESELLERCUSTOMER = u'resellercustomer'
  ARG_RESELLERCUSTOMERS = u'resellercustomers'
  ARG_RESELLERSUBSCRIPTION = u'resellersubscription'
  ARG_RESELLERSUBSCRIPTIONS = u'resellersubscriptions'
  ARG_RESOLDCUSTOMER = u'resoldcustomer'
  ARG_RESOLDCUSTOMERS = u'resoldcustomers'
  ARG_RESOLDSUBSCRIPTION = u'resoldsubscription'
  ARG_RESOLDSUBSCRIPTIONS = u'resoldsubscriptions'
  ARG_RESOURCE = u'resource'
  ARG_RESOURCES = u'resources'
  ARG_SCHEMA = u'schema'
  ARG_SCHEMAS = u'schemas'
  ARG_SECCALS = u'seccals'
  ARG_SENDAS = u'sendas'
  ARG_SERVICEACCOUNT = u'serviceaccount'
  ARG_SIG = u'sig'
  ARG_SIGNATURE = u'signature'
  ARG_SITE = u'site'
  ARG_SITES = u'sites'
  ARG_SITEACL = u'siteacl'
  ARG_SITEACLS = u'siteacls'
  ARG_SITEACTIVITY = u'siteactivity'
  ARG_SMIME = u'smime'
  ARG_SMIMES = u'smimes'
  ARG_TEAMDRIVE = u'teamdrive'
  ARG_TEAMDRIVES = u'teamdrives'
  ARG_THREAD = u'thread'
  ARG_THREADS = u'threads'
  ARG_TOKEN = u'token'
  ARG_TOKENS = u'tokens'
  ARG_TRANSFERAPPS = u'transferapps'
  ARG_USER = u'user'
  ARG_USERS = u'users'
  ARG_VACATION = u'vacation'
  ARG_VAULTHOLD = u'vaulthold'
  ARG_VAULTHOLDS = u'vaultholds'
  ARG_VAULTMATTER = u'vaultmatter'
  ARG_VAULTMATTERS = u'vaultmatters'
  ARG_VERIFICATIONCODES = u'verificationcodes'
  ARG_VERIFY = u'verify'
# Lists of arguments for use in checkArgumentPresent
  CLEAR_NONE_ARGUMENT = [u'clear', u'none',]
  CLIENTID_ARGUMENT = [u'clientid',]
  COLUMN_DELIMITER_ARGUMENT = [u'columndelimiter',]
  DATA_ARGUMENT = [u'data',]
  FILE_ARGUMENT = [u'file',]
  FROM_ARGUMENT = [u'from',]
  LOGO_ARGUMENT = [u'logo',]
  MOVE_ADD_ARGUMENT = [u'move', u'add',]
  MULTIVALUE_ARGUMENT = [u'multivalued', u'multivalue', u'value', u'multinonempty']
  NOINFO_ARGUMENT = [u'noinfo',]
  NOTSUSPENDED_ARGUMENT = [u'notsuspended',]
  ORG_OU_ARGUMENT = [u'org', u'ou',]
  PRIMARY_NOTPRIMARY_CHOICE_MAP = {u'primary': True, u'notprimary': False}
  QUERY_ARGUMENT = [u'query',]
  SHOWTITLES_ARGUMENT = [u'showtitles',]
  TODRIVE_ARGUMENT = [u'todrive',]
  TO_ARGUMENT = [u'to',]
  UNSTRUCTURED_FORMATTED_ARGUMENT = [u'unstructured', u'formatted',]

# Object BNF names
  OB_ACCESS_TOKEN = u'AccessToken'
  OB_ACL_SCOPE = u'ACLScope'
  OB_ACL_SCOPE_ENTITY = u'ACLScopeEntity'
  OB_ARGUMENT = u'argument'
  OB_ASP_ID = u'AspID'
  OB_CALENDAR_ENTITY = u'CalendarEntity'
  OB_CALENDAR_ITEM = u'CalendarItem'
  OB_CHAR_SET = u'CharacterSet'
  OB_CIDR_NETMASK = u'CIDRnetmask'
  OB_CLIENT_ID = u'ClientID'
  OB_COLLABORATOR_ITEM = u'CollaboratorItem'
  OB_COLLABORATOR_ENTITY = u'CollaboratorEntity'
  OB_CONTACT_EMAIL_TYPE = u'ContactEmailType'
  OB_CONTACT_ENTITY = u'ContactEntity'
  OB_CONTACT_GROUP_ENTITY = u'ContactGroupEntity'
  OB_CONTACT_GROUP_ITEM = u'ContactGroupItem'
  OB_COURSE_ALIAS = u'CourseAlias'
  OB_COURSE_ALIAS_ENTITY = u'CourseAliasEntity'
  OB_COURSE_ENTITY = u'CourseEntity'
  OB_COURSE_ID = u'CourseID'
  OB_CROS_DEVICE_ENTITY = u'CrOSDeviceEntity'
  OB_CROS_ENTITY = u'CrOSEntity'
  OB_CUSTOMER_ID = u'CustomerID'
  OB_CUSTOMER_AUTH_TOKEN = u'CustomerAuthToken'
  OB_DELIMITER = u'Delimiter'
  OB_DOMAIN_ALIAS = u'DomainAlias'
  OB_DOMAIN_NAME = u'DomainName'
  OB_DOMAIN_NAME_ENTITY = u'DomainNameEntity'
  OB_DRIVE_FILE_ENTITY = u'DriveFileEntity'
  OB_DRIVE_FILE_ID = u'DriveFileID'
  OB_DRIVE_FILE_NAME = u'DriveFileName'
  OB_DRIVE_FILE_PERMISSION_ENTITY = u'DriveFilePermissionEntity'
  OB_DRIVE_FILE_PERMISSION_ID = u'DriveFilePermissionID'
  OB_DRIVE_FILE_PERMISSION_ID_ENTITY = u'DriveFilePermissionIDEntity'
  OB_DRIVE_FILE_REVISION_ID = u'DriveFileRevisionID'
  OB_DRIVE_FOLDER_ID = u'DriveFolderID'
  OB_DRIVE_FOLDER_ID_LIST = u'DriveFolderIDList'
  OB_DRIVE_FOLDER_NAME = u'DriveFolderName'
  OB_EMAIL_ADDRESS = u'EmailAddress'
  OB_EMAIL_ADDRESS_ENTITY = u'EmailAddressEntity'
  OB_EMAIL_ADDRESS_OR_UID = u'EmailAaddress|UniqueID'
  OB_ENTITY = u'Entity'
  OB_ENTITY_TYPE = u'EntityType'
  OB_EVENT_ID = u'EventID'
  OB_EVENT_ID_ENTITY = u'EventIDEntity'
  OB_FIELD_NAME = u'FieldName'
  OB_FIELD_NAME_LIST = "FieldNameList"
  OB_FILE_NAME = u'FileName'
  OB_FILE_NAME_FIELD_NAME = OB_FILE_NAME+u'(:'+OB_FIELD_NAME+u')+'
  OB_FILE_NAME_OR_URL = u'FileName|URL'
  OB_FILE_PATH = u'FilePath'
  OB_FILTER_ID_ENTITY = u'FilterIDEntity'
  OB_FORMAT_LIST = u'FormatList'
  OB_GAM_ARGUMENT_LIST = u'GAM argument list'
  OB_GROUP_ENTITY = u'GroupEntity'
  OB_GROUP_ITEM = u'GroupItem'
  OB_GUARDIAN_INVITATION_ID = u'GuardianInvitationID'
  OB_GUARDIAN_ITEM = u'GuardianItem'
  OB_GUARDIAN_STATE_LIST = u'GuardianStateList'
  OB_HOLD_ITEM = u'HoldItem'
  OB_HOST_NAME = u'HostName'
  OB_ICALUID = u'iCalUID'
  OB_JOB_ID = u'JobID'
  OB_JOB_OR_PRINTER_ID = u'JobID|PrinterID'
  OB_LABEL_NAME = u'LabelName'
  OB_LABEL_REPLACEMENT = u'LabelReplacement'
  OB_MATTER_ITEM = u'MatterItem'
  OB_MATTER_ITEM_LIST = u'MatterItemList'
  OB_MESSAGE_ID = u'MessageID'
  OB_MOBILE_DEVICE_ENTITY = u'MobileDeviceEntity'
  OB_MOBILE_ENTITY = u'MobileEntity'
  OB_NAME = u'Name'
  OB_NOTIFICATION_ID = u'NotificationID'
  OB_ORGUNIT_ENTITY = u'OrgUnitEntity'
  OB_ORGUNIT_ITEM = u'OrgUnitItem'
  OB_ORGUNIT_PATH = u'OrgUnitPath'
  OB_PARAMETER_KEY = u'ParameterKey'
  OB_PARAMETER_VALUE = u'ParameterValue'
  OB_PASSWORD = u'Password'
  OB_PHOTO_FILENAME_PATTERN = u'FilenameNamePattern'
  OB_PRINTER_ID = u'PrinterID'
  OB_PRINTER_ID_ENTITY = u'PrinterIDEntity'
  OB_PRINTJOB_AGE = u'PrintJobAge'
  OB_PRINTJOB_ID = u'PrintJobID'
  OB_PRODUCT_ID = u'ProductID'
  OB_PRODUCT_ID_LIST = u'ProductIDList'
  OB_PROPERTY_KEY = u'PropertyKey'
  OB_PROPERTY_VALUE = u'PropertyValue'
  OB_QUERY = u'Query'
  OB_RECURRENCE = u'RRULE EXRULE RDATE and EXDATE lines'
  OB_REQUEST_ID = u'RequestID'
  OB_RESOURCE_ENTITY = u'ResourceEntity'
  OB_RESOURCE_ID = u'ResourceID'
  OB_RE_PATTERN = u'REPattern'
  OB_ROLE_ASSIGNMENT_ID = u'RoleAssignmentID'
  OB_ROLE_ID = u'RoleID'
  OB_ROLE_LIST = u'RoleList'
  OB_SCHEMA_ENTITY = u'SchemaEntity'
  OB_SCHEMA_NAME = u'SchemaName'
  OB_SCHEMA_NAME_FIELD_NAME = u'SchemaName.FieldName'
  OB_SCHEMA_NAME_LIST = u'SchemaNameList'
  OB_SECTION_NAME = u'SectionName'
  OB_SERVICE_NAME = u'ServiceName'
  OB_SITE_ENTITY = u'SiteEntity'
  OB_SKU_ID = u'SKUID'
  OB_SKU_ID_LIST = u'SKUIDList'
  OB_SMIME_ID = u'S/MIMEID'
  OB_STRING = u'String'
  OB_STUDENT_ITEM = u'StudentItem'
  OB_TAG = u'Tag'
  OB_TEAMDRIVE_ID = u'TeamDriveID'
  OB_TEAMDRIVE_ID_LIST = u'TeamDriveIDList'
  OB_TEAMDRIVE_NAME = u'TeamDriveName'
  OB_THREAD_ID = u'ThreadID'
  OB_TRANSFER_ID = u'TransferID'
  OB_URI = u'URI'
  OB_URL = u'URL'
  OB_USER_ENTITY = u'UserEntity'
  OB_USER_ITEM = u'UserItem'

#
# Error message types; keys into ARGUMENT_ERROR_NAMES; arbitrary values but must be unique
  ARGUMENT_BLANK = u'blnk'
  ARGUMENT_DEPRECATED = u'depr'
  ARGUMENT_EMPTY = u'empt'
  ARGUMENT_EXTRANEOUS = u'extr'
  ARGUMENT_INVALID = u'inva'
  ARGUMENT_MISSING = u'miss'
# ARGUMENT_ERROR_NAMES[0] is plural,ARGUMENT_ERROR_NAMES[1] is singular
# These values can be translated into other languages
  ARGUMENT_ERROR_NAMES = {
    ARGUMENT_BLANK: [u'Blank arguments', u'Blank argument'],
    ARGUMENT_DEPRECATED: [u'Deprecated arguments', u'Deprecated argument'],
    ARGUMENT_EMPTY: [u'Empty arguments', u'Empty argument'],
    ARGUMENT_EXTRANEOUS: [u'Extra arguments', u'Extra argument'],
    ARGUMENT_INVALID: [u'Invalid arguments', u'Invalid argument'],
    ARGUMENT_MISSING: [u'Missing arguments', u'Missing argument'],
    }

  def __init__(self):
    self.argv = []
    self.argvI = 0
    self.argvLen = 0
    self.argvIsave = 0
    self.encoding = u'utf-8'

# Initialize arguments
  def InitializeArguments(self, args):
    self.argv = args[:]
    self.argvI = 1
    self.argvLen = len(self.argv)

# Any arguments remaining
  def ArgumentsRemaining(self):
    return self.argvI < self.argvLen

# Multiple arguments remaining
  def MultipleArgumentsRemaining(self):
    return not self.argvI+1 == self.argvLen

# All arguments
  def AllArguments(self):
    return self.argv

# Specific argument
  def Argument(self, index):
    return self.argv[index]

# Current argument
  def Current(self):
    return self.argv[self.argvI]

# Previous argument
  def Previous(self):
    return self.argv[self.argvI-1]

# Remaining arguments
  def Remaining(self):
    return self.argv[self.argvI:]

# Argument location
  def Location(self):
    return self.argvI

# Advance to next argument
  def Advance(self):
    self.argvI += 1

# Backup to previous argument
  def Backup(self):
    self.argvI -= 1

# Save argument location
  def SaveLocation(self):
    self.argvIsave = self.argvI

# Reset argument location
  def ResetLocation(self, offset):
    self.argvI = self.argvIsave+offset

# Set argument location
  def SetLocation(self, location):
    self.argvI = location

# Set encoding
  def SetEncoding(self, encoding):
    self.encoding = encoding

# Concatenate list members, any item containing spaces is enclosed in ""
  def QuotedArgumentList(self, items):
    qstr = u''
    for item in items:
      if isinstance(item, str):
        item = unicode(item, self.encoding, 'replace')
      if item and (item.find(u' ') == -1) and (item.find(u',') == -1):
        qstr += item
      else:
        qstr += u'"'+item+u'"'
      qstr += u' '
    return qstr[:-1] if len(qstr) > 0 else u''

# Mark bad argument in command line
  def CommandLineWithBadArgumentMarked(self, extraneous):
    if extraneous:
      return u'Command: {0} >>>{1}<<<\n'.format(self.QuotedArgumentList(self.argv[:self.argvI]),
                                                self.QuotedArgumentList(self.argv[self.argvI:]))
    if self.ArgumentsRemaining():
      return u'Command: {0} >>>{1}<<< {2}\n'.format(self.QuotedArgumentList(self.argv[:self.argvI]),
                                                    self.QuotedArgumentList([self.argv[self.argvI]]),
                                                    self.QuotedArgumentList(self.argv[self.argvI+1:]))
    return u'Command: {0} >>><<<\n'.format(self.QuotedArgumentList(self.argv))
