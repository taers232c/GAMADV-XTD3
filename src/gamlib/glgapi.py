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

"""GAM GAPI resources

"""
# callGAPI throw reasons
ABORTED = u'aborted'
ACCESS_NOT_CONFIGURED = u'accessNotConfigured'
ALREADY_EXISTS = u'alreadyExists'
AUTH_ERROR = u'authError'
BACKEND_ERROR = u'backendError'
BAD_GATEWAY = u'badGateway'
BAD_REQUEST = u'badRequest'
CANNOT_CHANGE_ORGANIZER = u'cannotChangeOrganizer'
CANNOT_CHANGE_ORGANIZER_OF_INSTANCE = u'cannotChangeOrganizerOfInstance'
CANNOT_CHANGE_OWN_ACL = u'cannotChangeOwnAcl'
CANNOT_CHANGE_OWNER_ACL = u'cannotChangeOwnerAcl'
CANNOT_COPY_FILE = u'cannotCopyFile'
CANNOT_DELETE_ONLY_REVISION = u'cannotDeleteOnlyRevision'
CANNOT_DELETE_PRIMARY_CALENDAR = u'cannotDeletePrimaryCalendar'
CANNOT_DELETE_PRIMARY_SENDAS = u'cannotDeletePrimarySendAs'
CANNOT_DELETE_RESOURCE_WITH_CHILDREN = u'cannotDeleteResourceWithChildren'
CANNOT_MODIFY_INHERITED_TEAMDRIVE_PERMISSION = u'cannotModifyInheritedTeamDrivePermission'
CANNOT_MOVE_TRASHED_ITEM_INTO_TEAM_DRIVE = u'cannotMoveTrashedItemIntoTeamDrive'
CANNOT_REMOVE_OWNER = u'cannotRemoveOwner'
CANNOT_SHARE_GROUPS_WITHLINK = u'cannotShareGroupsWithLink'
CANNOT_SHARE_USERS_WITHLINK = u'cannotShareUsersWithLink'
CANNOT_SHARE_TEAMDRIVE_TOPFOLDER_WITH_ANYONEORDOMAINS = u'cannotShareTeamDriveTopFolderWithAnyoneOrDomains'
CONDITION_NOT_MET = u'conditionNotMet'
CUSTOMER_NOT_FOUND = u'customerNotFound'
CYCLIC_MEMBERSHIPS_NOT_ALLOWED = u'cyclicMembershipsNotAllowed'
DELETED = u'deleted'
DELETED_USER_NOT_FOUND = u'deletedUserNotFound'
DOMAIN_ALIAS_NOT_FOUND = u'domainAliasNotFound'
DOMAIN_CANNOT_USE_APIS = u'domainCannotUseApis'
DOMAIN_NOT_FOUND = u'domainNotFound'
DOMAIN_NOT_VERIFIED_SECONDARY = u'domainNotVerifiedSecondary'
DOMAIN_POLICY = u'domainPolicy'
DUPLICATE = u'duplicate'
FAILED_PRECONDITION = u'failedPrecondition'
FIELD_NOT_WRITABLE = u'fieldNotWritable'
FILE_NEVER_WRITABLE = u'fileNeverWritable'
FILE_NOT_FOUND = u'fileNotFound'
FILE_OWNER_NOT_MEMBER_OF_WRITER_DOMAIN = u'fileOwnerNotMemberOfWriterDomain'
FORBIDDEN = u'forbidden'
GROUP_NOT_FOUND = u'groupNotFound'
ILLEGAL_ACCESS_ROLE_FOR_DEFAULT = u'illegalAccessRoleForDefault'
INSUFFICIENT_FILE_PERMISSIONS = u'insufficientFilePermissions'
INSUFFICIENT_PERMISSIONS = u'insufficientPermissions'
INTERNAL_ERROR = u'internalError'
INVALID = u'invalid'
INVALID_ARGUMENT = u'invalidArgument'
INVALID_CUSTOMER_ID = u'invalidCustomerId'
INVALID_INPUT = u'invalidInput'
INVALID_MEMBER = u'invalidMember'
INVALID_MESSAGE_ID = u'invalidMessageId'
INVALID_ORGUNIT = u'invalidOrgunit'
INVALID_ORGUNIT_NAME = u'invalidOrgunitName'
INVALID_OWNERSHIP_TRANSFER = u'invalidOwnershipTransfer'
INVALID_PARAMETER = u'invalidParameter'
INVALID_PARENT_ORGUNIT = u'invalidParentOrgunit'
INVALID_QUERY = u'invalidQuery'
INVALID_RESOURCE = u'invalidResource'
INVALID_SCHEMA_VALUE = u'invalidSchemaValue'
INVALID_SCOPE_VALUE = u'invalidScopeValue'
INVALID_SHARING_REQUEST = u'invalidSharingRequest'
LOGIN_REQUIRED = u'loginRequired'
MEMBER_NOT_FOUND = u'memberNotFound'
NO_LIST_TEAMDRIVES_ADMINISTRATOR_PRIVILEGE = u'noListTeamDrivesAdministratorPrivilege'
NOT_A_CALENDAR_USER = u'notACalendarUser'
NOT_FOUND = u'notFound'
NOT_IMPLEMENTED = u'notImplemented'
OPERATION_NOT_SUPPORTED = u'operationNotSupported'
ORGANIZER_ON_NON_TEAMDRIVE_ITEM_NOT_SUPPORTED = u'organizerOnNonTeamDriveItemNotSupported'
ORGUNIT_NOT_FOUND = u'orgunitNotFound'
OWNER_ON_TEAMDRIVE_ITEM_NOT_SUPPORTED = u'ownerOnTeamDriveItemNotSupported'
PERMISSION_DENIED = u'permissionDenied'
PERMISSION_NOT_FOUND = u'permissionNotFound'
PHOTO_NOT_FOUND = u'photoNotFound'
QUERY_REQUIRES_ADMIN_CREDENTIALS = u'queryRequiresAdminCredentials'
QUOTA_EXCEEDED = u'quotaExceeded'
RATE_LIMIT_EXCEEDED = u'rateLimitExceeded'
REQUIRED = u'required'
RESOURCE_EXHAUSTED = u'resourceExhausted'
RESOURCE_ID_NOT_FOUND = u'resourceIdNotFound'
RESOURCE_NOT_FOUND = u'resourceNotFound'
RESPONSE_PREPARATION_FAILURE = u'responsePreparationFailure'
REVISION_DELETION_NOT_SUPPORTED = u'revisionDeletionNotSupported'
REVISION_NOT_FOUND = u'revisionNotFound'
REVISIONS_NOT_SUPPORTED = u'revisionsNotSupported'
SERVICE_LIMIT = u'serviceLimit'
SERVICE_NOT_AVAILABLE = u'serviceNotAvailable'
SYSTEM_ERROR = u'systemError'
TEAMDRIVE_MEMBERSHIP_REQUIRED = u'teamDriveMembershipRequired'
TEAMDRIVE_NOT_FOUND = u'teamDriveNotFound'
TEAMDRIVES_FOLDER_MOVE_IN_NOT_SUPPORTED = u'teamDrivesFolderMoveInNotSupported'
TEAMDRIVES_FOLDER_SHARING_NOT_SUPPORTED = u'teamDrivesFolderSharingNotSupported'
TEAMDRIVES_PARENT_LIMIT = u'teamDrivesParentLimit'
TEAMDRIVES_SHARING_RESTRICTION_NOT_ALLOWED = u'teamDrivesSharingRestrictionNotAllowed'
TIME_RANGE_EMPTY = u'timeRangeEmpty'
TRANSIENT_ERROR = u'transientError'
UNKNOWN_ERROR = u'unknownError'
USER_ACCESS = u'userAccess'
USER_NOT_FOUND = u'userNotFound'
USER_RATE_LIMIT_EXCEEDED = u'userRateLimitExceeded'
#
DEFAULT_RETRY_REASONS = [QUOTA_EXCEEDED, RATE_LIMIT_EXCEEDED, USER_RATE_LIMIT_EXCEEDED, BACKEND_ERROR, BAD_GATEWAY, INTERNAL_ERROR, TRANSIENT_ERROR]
ACTIVITY_THROW_REASONS = [SERVICE_NOT_AVAILABLE]
CALENDAR_THROW_REASONS = [SERVICE_NOT_AVAILABLE, AUTH_ERROR, NOT_A_CALENDAR_USER]
DRIVE_USER_THROW_REASONS = [SERVICE_NOT_AVAILABLE, AUTH_ERROR, DOMAIN_POLICY]
DRIVE_ACCESS_THROW_REASONS = DRIVE_USER_THROW_REASONS+[FILE_NOT_FOUND, FORBIDDEN, INTERNAL_ERROR, INSUFFICIENT_FILE_PERMISSIONS, UNKNOWN_ERROR, INVALID]
DRIVE_COPY_THROW_REASONS = DRIVE_ACCESS_THROW_REASONS+[CANNOT_COPY_FILE, RESPONSE_PREPARATION_FAILURE, RATE_LIMIT_EXCEEDED, USER_RATE_LIMIT_EXCEEDED]
DRIVE_GET_THROW_REASONS = DRIVE_USER_THROW_REASONS+[FILE_NOT_FOUND]
GMAIL_THROW_REASONS = [SERVICE_NOT_AVAILABLE, BAD_REQUEST]
GMAIL_SMIME_THROW_REASONS = [SERVICE_NOT_AVAILABLE, BAD_REQUEST, INVALID_ARGUMENT, FORBIDDEN]
GPLUS_THROW_REASONS = [SERVICE_NOT_AVAILABLE]
GROUP_GET_RETRY_REASONS = [INVALID, SYSTEM_ERROR]
GROUP_CREATE_THROW_REASONS = [DUPLICATE, DOMAIN_NOT_FOUND, DOMAIN_CANNOT_USE_APIS, FORBIDDEN, INVALID, INVALID_INPUT]
GROUP_GET_THROW_REASONS = [GROUP_NOT_FOUND, DOMAIN_NOT_FOUND, DOMAIN_CANNOT_USE_APIS, FORBIDDEN, BAD_REQUEST, INVALID, SYSTEM_ERROR]
GROUP_UPDATE_THROW_REASONS = [GROUP_NOT_FOUND, DOMAIN_NOT_FOUND, DOMAIN_CANNOT_USE_APIS, FORBIDDEN, INVALID, INVALID_INPUT]
GROUP_SETTINGS_THROW_REASONS = [NOT_FOUND, GROUP_NOT_FOUND, DOMAIN_NOT_FOUND, DOMAIN_CANNOT_USE_APIS, FORBIDDEN, SYSTEM_ERROR, PERMISSION_DENIED, INVALID, INVALID_INPUT, SERVICE_LIMIT]
GROUP_SETTINGS_RETRY_REASONS = [INVALID, SERVICE_LIMIT]
MEMBERS_THROW_REASONS = [GROUP_NOT_FOUND, DOMAIN_NOT_FOUND, DOMAIN_CANNOT_USE_APIS, INVALID, FORBIDDEN]
MEMBERS_RETRY_REASONS = [SYSTEM_ERROR]
SHEETS_ACCESS_THROW_REASONS = DRIVE_USER_THROW_REASONS+[NOT_FOUND, FORBIDDEN, INTERNAL_ERROR, INSUFFICIENT_FILE_PERMISSIONS, BAD_REQUEST, INVALID]
USER_GET_THROW_REASONS = [USER_NOT_FOUND, DOMAIN_NOT_FOUND, DOMAIN_CANNOT_USE_APIS, FORBIDDEN, BAD_REQUEST, SYSTEM_ERROR]

REASON_MESSAGE_MAP = {
  ABORTED: [
    (u'Label name exists or conflicts', DUPLICATE),
    ],
  CONDITION_NOT_MET: [
    (u'Cyclic memberships not allowed', CYCLIC_MEMBERSHIPS_NOT_ALLOWED),
    (u'undelete', DELETED_USER_NOT_FOUND),
    ],
  FAILED_PRECONDITION: [
    (u'Bad Request', BAD_REQUEST),
    (u'Mail service not enabled', SERVICE_NOT_AVAILABLE),
    ],
  INVALID: [
    (u'userId', USER_NOT_FOUND),
    (u'memberKey', INVALID_MEMBER),
    (u'A system error has occurred', SYSTEM_ERROR),
    (u'Invalid Customer Id', INVALID_CUSTOMER_ID),
    (u'Invalid Input: INVALID_OU_ID', INVALID_ORGUNIT),
    (u'Invalid Input: custom_schema', INVALID_SCHEMA_VALUE),
    (u'Invalid Input: resource', INVALID_RESOURCE),
    (u'Invalid Input:', INVALID_INPUT),
    (u'Invalid Input', INVALID_INPUT),
    (u'Invalid Org Unit', INVALID_ORGUNIT),
    (u'Invalid Ou Id', INVALID_ORGUNIT),
    (u'Invalid Ou Name', INVALID_ORGUNIT_NAME),
    (u'Invalid Parent Orgunit Id', INVALID_PARENT_ORGUNIT),
    (u'Invalid query', INVALID_QUERY),
    (u'Invalid scope value', INVALID_SCOPE_VALUE),
    (u'Invalid value', INVALID_INPUT),
    (u'New domain name is not a verified secondary domain', DOMAIN_NOT_VERIFIED_SECONDARY),
    (u'PermissionDenied', PERMISSION_DENIED),
    ],
  INVALID_ARGUMENT: [
    (u'Cannot delete primary send-as', CANNOT_DELETE_PRIMARY_SENDAS),
    (u'Invalid id value', INVALID_MESSAGE_ID),
    (u'Invalid ids value', INVALID_MESSAGE_ID),
    ],
  NOT_FOUND: [
    (u'userKey', USER_NOT_FOUND),
    (u'groupKey', GROUP_NOT_FOUND),
    (u'memberKey', MEMBER_NOT_FOUND),
    (u'photo', PHOTO_NOT_FOUND),
    (u'resource_id', RESOURCE_ID_NOT_FOUND),
    (u'resourceId', RESOURCE_ID_NOT_FOUND),
    (u'Customer doesn\'t exist', CUSTOMER_NOT_FOUND),
    (u'Domain alias does not exist', DOMAIN_ALIAS_NOT_FOUND),
    (u'Domain not found', DOMAIN_NOT_FOUND),
    (u'domain', DOMAIN_NOT_FOUND),
    (u'File not found', FILE_NOT_FOUND),
    (u'Org unit not found', ORGUNIT_NOT_FOUND),
    (u'Permission not found', PERMISSION_NOT_FOUND),
    (u'Resource Not Found', RESOURCE_NOT_FOUND),
    (u'Revision not found', REVISION_NOT_FOUND),
    (u'Team Drive not found', TEAMDRIVE_NOT_FOUND),
    (u'Not Found', NOT_FOUND),
    ],
  REQUIRED: [
    (u'Login Required', LOGIN_REQUIRED),
    (u'memberKey', MEMBER_NOT_FOUND),
    ],
  RESOURCE_NOT_FOUND: [
    (u'resourceId', RESOURCE_ID_NOT_FOUND),
    ],
  }

class aborted(Exception):
  pass
class accessNotConfigured(Exception):
  pass
class alreadyExists(Exception):
  pass
class authError(Exception):
  pass
class backendError(Exception):
  pass
class badRequest(Exception):
  pass
class cannotChangeOrganizer(Exception):
  pass
class cannotChangeOrganizerOfInstance(Exception):
  pass
class cannotChangeOwnAcl(Exception):
  pass
class cannotChangeOwnerAcl(Exception):
  pass
class cannotCopyFile(Exception):
  pass
class cannotDeleteOnlyRevision(Exception):
  pass
class cannotDeletePrimaryCalendar(Exception):
  pass
class cannotDeletePrimarySendAs(Exception):
  pass
class cannotDeleteResourceWithChildren(Exception):
  pass
class cannotModifyInheritedTeamDrivePermission(Exception):
  pass
class cannotMoveTrashedItemIntoTeamDrive(Exception):
  pass
class cannotRemoveOwner(Exception):
  pass
class cannotShareGroupsWithLink(Exception):
  pass
class cannotShareUsersWithLink(Exception):
  pass
class cannotShareTeamDriveTopFolderWithAnyoneOrDomains(Exception):
  pass
class conditionNotMet(Exception):
  pass
class customerNotFound(Exception):
  pass
class cyclicMembershipsNotAllowed(Exception):
  pass
class deleted(Exception):
  pass
class deletedUserNotFound(Exception):
  pass
class domainAliasNotFound(Exception):
  pass
class domainCannotUseApis(Exception):
  pass
class domainNotFound(Exception):
  pass
class domainNotVerifiedSecondary(Exception):
  pass
class domainPolicy(Exception):
  pass
class duplicate(Exception):
  pass
class failedPrecondition(Exception):
  pass
class fieldNotWritable(Exception):
  pass
class fileNeverWritable(Exception):
  pass
class fileNotFound(Exception):
  pass
class fileOwnerNotMemberOfWriterDomain(Exception):
  pass
class forbidden(Exception):
  pass
class groupNotFound(Exception):
  pass
class illegalAccessRoleForDefault(Exception):
  pass
class insufficientFilePermissions(Exception):
  pass
class insufficientPermissions(Exception):
  pass
class internalError(Exception):
  pass
class invalid(Exception):
  pass
class invalidArgument(Exception):
  pass
class invalidCustomerId(Exception):
  pass
class invalidInput(Exception):
  pass
class invalidMember(Exception):
  pass
class invalidMessageId(Exception):
  pass
class invalidOrgunit(Exception):
  pass
class invalidOrgunitName(Exception):
  pass
class invalidOwnershipTransfer(Exception):
  pass
class invalidParameter(Exception):
  pass
class invalidParentOrgunit(Exception):
  pass
class invalidQuery(Exception):
  pass
class invalidResource(Exception):
  pass
class invalidSchemaValue(Exception):
  pass
class invalidScopeValue(Exception):
  pass
class invalidSharingRequest(Exception):
  pass
class loginRequired(Exception):
  pass
class memberNotFound(Exception):
  pass
class noListTeamDrivesAdministratorPrivilege(Exception):
  pass
class notACalendarUser(Exception):
  pass
class notFound(Exception):
  pass
class notImplemented(Exception):
  pass
class operationNotSupported(Exception):
  pass
class organizerOnNonTeamDriveItemNotSupported(Exception):
  pass
class orgunitNotFound(Exception):
  pass
class ownerOnTeamDriveItemNotSupported(Exception):
  pass
class permissionDenied(Exception):
  pass
class permissionNotFound(Exception):
  pass
class photoNotFound(Exception):
  pass
class queryRequiresAdminCredentials(Exception):
  pass
class rateLimitExceeded(Exception):
  pass
class required(Exception):
  pass
class resourceExhausted(Exception):
  pass
class resourceIdNotFound(Exception):
  pass
class resourceNotFound(Exception):
  pass
class responsePreparationFailure(Exception):
  pass
class revisionDeletionNotSupported(Exception):
  pass
class revisionNotFound(Exception):
  pass
class revisionsNotSupported(Exception):
  pass
class serviceLimit(Exception):
  pass
class serviceNotAvailable(Exception):
  pass
class systemError(Exception):
  pass
class teamDriveMembershipRequired(Exception):
  pass
class teamDriveNotFound(Exception):
  pass
class teamDrivesFolderMoveInNotSupported(Exception):
  pass
class teamDrivesFolderSharingNotSupported(Exception):
  pass
class teamDrivesParentLimit(Exception):
  pass
class teamDrivesSharingRestrictionNotAllowed(Exception):
  pass
class timeRangeEmpty(Exception):
  pass
class transientError(Exception):
  pass
class unknownError(Exception):
  pass
class userAccess(Exception):
  pass
class userNotFound(Exception):
  pass
class userRateLimitExceeded(Exception):
  pass

REASON_EXCEPTION_MAP = {
  ABORTED: aborted,
  ACCESS_NOT_CONFIGURED: accessNotConfigured,
  ALREADY_EXISTS: alreadyExists,
  AUTH_ERROR: authError,
  BACKEND_ERROR: backendError,
  BAD_REQUEST: badRequest,
  CANNOT_CHANGE_ORGANIZER: cannotChangeOrganizer,
  CANNOT_CHANGE_ORGANIZER_OF_INSTANCE: cannotChangeOrganizerOfInstance,
  CANNOT_CHANGE_OWN_ACL: cannotChangeOwnAcl,
  CANNOT_CHANGE_OWNER_ACL: cannotChangeOwnerAcl,
  CANNOT_COPY_FILE: cannotCopyFile,
  CANNOT_DELETE_ONLY_REVISION: cannotDeleteOnlyRevision,
  CANNOT_DELETE_PRIMARY_CALENDAR: cannotDeletePrimaryCalendar,
  CANNOT_DELETE_PRIMARY_SENDAS: cannotDeletePrimarySendAs,
  CANNOT_DELETE_RESOURCE_WITH_CHILDREN: cannotDeleteResourceWithChildren,
  CANNOT_MODIFY_INHERITED_TEAMDRIVE_PERMISSION: cannotModifyInheritedTeamDrivePermission,
  CANNOT_MOVE_TRASHED_ITEM_INTO_TEAM_DRIVE: cannotMoveTrashedItemIntoTeamDrive,
  CANNOT_REMOVE_OWNER: cannotRemoveOwner,
  CANNOT_SHARE_GROUPS_WITHLINK: cannotShareGroupsWithLink,
  CANNOT_SHARE_USERS_WITHLINK: cannotShareUsersWithLink,
  CANNOT_SHARE_TEAMDRIVE_TOPFOLDER_WITH_ANYONEORDOMAINS: cannotShareTeamDriveTopFolderWithAnyoneOrDomains,
  CONDITION_NOT_MET: conditionNotMet,
  CUSTOMER_NOT_FOUND: customerNotFound,
  CYCLIC_MEMBERSHIPS_NOT_ALLOWED: cyclicMembershipsNotAllowed,
  DELETED: deleted,
  DELETED_USER_NOT_FOUND: deletedUserNotFound,
  DOMAIN_ALIAS_NOT_FOUND: domainAliasNotFound,
  DOMAIN_CANNOT_USE_APIS: domainCannotUseApis,
  DOMAIN_NOT_FOUND: domainNotFound,
  DOMAIN_NOT_VERIFIED_SECONDARY: domainNotVerifiedSecondary,
  DOMAIN_POLICY: domainPolicy,
  DUPLICATE: duplicate,
  FAILED_PRECONDITION: failedPrecondition,
  FIELD_NOT_WRITABLE: fieldNotWritable,
  FILE_NEVER_WRITABLE: fileNeverWritable,
  FILE_NOT_FOUND: fileNotFound,
  FILE_OWNER_NOT_MEMBER_OF_WRITER_DOMAIN: fileOwnerNotMemberOfWriterDomain,
  FORBIDDEN: forbidden,
  GROUP_NOT_FOUND: groupNotFound,
  ILLEGAL_ACCESS_ROLE_FOR_DEFAULT: illegalAccessRoleForDefault,
  INSUFFICIENT_FILE_PERMISSIONS: insufficientFilePermissions,
  INSUFFICIENT_PERMISSIONS: insufficientPermissions,
  INTERNAL_ERROR: internalError,
  INVALID: invalid,
  INVALID_ARGUMENT: invalidArgument,
  INVALID_CUSTOMER_ID: invalidCustomerId,
  INVALID_INPUT: invalidInput,
  INVALID_MEMBER: invalidMember,
  INVALID_MESSAGE_ID: invalidMessageId,
  INVALID_ORGUNIT: invalidOrgunit,
  INVALID_ORGUNIT_NAME: invalidOrgunitName,
  INVALID_OWNERSHIP_TRANSFER: invalidOwnershipTransfer,
  INVALID_PARAMETER: invalidParameter,
  INVALID_PARENT_ORGUNIT: invalidParentOrgunit,
  INVALID_QUERY: invalidQuery,
  INVALID_RESOURCE: invalidResource,
  INVALID_SCHEMA_VALUE: invalidSchemaValue,
  INVALID_SCOPE_VALUE: invalidScopeValue,
  INVALID_SHARING_REQUEST: invalidSharingRequest,
  LOGIN_REQUIRED: loginRequired,
  MEMBER_NOT_FOUND: memberNotFound,
  NO_LIST_TEAMDRIVES_ADMINISTRATOR_PRIVILEGE: noListTeamDrivesAdministratorPrivilege,
  NOT_A_CALENDAR_USER: notACalendarUser,
  NOT_FOUND: notFound,
  NOT_IMPLEMENTED: notImplemented,
  OPERATION_NOT_SUPPORTED: operationNotSupported,
  ORGANIZER_ON_NON_TEAMDRIVE_ITEM_NOT_SUPPORTED: organizerOnNonTeamDriveItemNotSupported,
  ORGUNIT_NOT_FOUND: orgunitNotFound,
  OWNER_ON_TEAMDRIVE_ITEM_NOT_SUPPORTED: ownerOnTeamDriveItemNotSupported,
  PERMISSION_DENIED: permissionDenied,
  PERMISSION_NOT_FOUND: permissionNotFound,
  PHOTO_NOT_FOUND: photoNotFound,
  QUERY_REQUIRES_ADMIN_CREDENTIALS: queryRequiresAdminCredentials,
  RATE_LIMIT_EXCEEDED: rateLimitExceeded,
  REQUIRED: required,
  RESOURCE_EXHAUSTED: resourceExhausted,
  RESOURCE_ID_NOT_FOUND: resourceIdNotFound,
  RESOURCE_NOT_FOUND: resourceNotFound,
  RESPONSE_PREPARATION_FAILURE: responsePreparationFailure,
  REVISION_DELETION_NOT_SUPPORTED: revisionDeletionNotSupported,
  REVISION_NOT_FOUND: revisionNotFound,
  REVISIONS_NOT_SUPPORTED: revisionsNotSupported,
  SERVICE_LIMIT: serviceLimit,
  SERVICE_NOT_AVAILABLE: serviceNotAvailable,
  SYSTEM_ERROR: systemError,
  TEAMDRIVE_MEMBERSHIP_REQUIRED: teamDriveMembershipRequired,
  TEAMDRIVE_NOT_FOUND: teamDriveNotFound,
  TEAMDRIVES_FOLDER_MOVE_IN_NOT_SUPPORTED: teamDrivesFolderMoveInNotSupported,
  TEAMDRIVES_FOLDER_SHARING_NOT_SUPPORTED: teamDrivesFolderSharingNotSupported,
  TEAMDRIVES_PARENT_LIMIT: teamDrivesParentLimit,
  TEAMDRIVES_SHARING_RESTRICTION_NOT_ALLOWED: teamDrivesSharingRestrictionNotAllowed,
  TIME_RANGE_EMPTY: timeRangeEmpty,
  TRANSIENT_ERROR: transientError,
  UNKNOWN_ERROR: unknownError,
  USER_ACCESS: userAccess,
  USER_NOT_FOUND: userNotFound,
  USER_RATE_LIMIT_EXCEEDED: userRateLimitExceeded,
  }
