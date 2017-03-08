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
ABORTED = 'aborted'
ALREADY_EXISTS = 'alreadyExists'
AUTH_ERROR = 'authError'
BACKEND_ERROR = 'backendError'
BAD_GATEWAY = 'badGateway'
BAD_REQUEST = 'badRequest'
CANNOT_CHANGE_OWN_ACL = 'cannotChangeOwnAcl'
CANNOT_CHANGE_OWNER_ACL = 'cannotChangeOwnerAcl'
CANNOT_DELETE_PRIMARY_CALENDAR = 'cannotDeletePrimaryCalendar'
CANNOT_DELETE_PRIMARY_SENDAS = 'cannotDeletePrimarySendAs'
CONDITION_NOT_MET = 'conditionNotMet'
CONNECTION_REFUSED = 'connectionRefused'
CUSTOMER_NOT_FOUND = 'customerNotFound'
CYCLIC_MEMBERSHIPS_NOT_ALLOWED = 'cyclicMembershipsNotAllowed'
DELETED = 'deleted'
DELETED_USER_NOT_FOUND = 'deletedUserNotFound'
DOMAIN_ALIAS_NOT_FOUND = 'domainAliasNotFound'
DOMAIN_CANNOT_USE_APIS = 'domainCannotUseApis'
DOMAIN_NOT_FOUND = 'domainNotFound'
DOMAIN_NOT_VERIFIED_SECONDARY = 'domainNotVerifiedSecondary'
DUPLICATE = 'duplicate'
FAILED_PRECONDITION = 'failedPrecondition'
FILE_NOT_FOUND = 'fileNotFound'
FORBIDDEN = 'forbidden'
GROUP_NOT_FOUND = 'groupNotFound'
ILLEGAL_ACCESS_ROLE_FOR_DEFAULT = 'illegalAccessRoleForDefault'
INSUFFICIENT_PERMISSIONS = 'insufficientPermissions'
INTERNAL_ERROR = 'internalError'
INVALID = 'invalid'
INVALID_ARGUMENT = 'invalidArgument'
INVALID_CUSTOMER_ID = 'invalidCustomerId'
INVALID_INPUT = 'invalidInput'
INVALID_MEMBER = 'invalidMember'
INVALID_MESSAGE_ID = 'invalidMessageId'
INVALID_ORGUNIT = 'invalidOrgunit'
INVALID_OWNERSHIP_TRANSFER = 'invalidOwnershipTransfer'
INVALID_PARAMETER = 'invalidParameter'
INVALID_PARENT_ORGUNIT = 'invalidParentOrgunit'
INVALID_QUERY = 'invalidQuery'
INVALID_RESOURCE = 'invalidResource'
INVALID_SCHEMA_VALUE = 'invalidSchemaValue'
INVALID_SCOPE_VALUE = 'invalidScopeValue'
INVALID_SHARING_REQUEST = 'invalidSharingRequest'
LOGIN_REQUIRED = 'loginRequired'
MEMBER_NOT_FOUND = 'memberNotFound'
NOT_A_CALENDAR_USER = 'notACalendarUser'
NOT_FOUND = 'notFound'
NOT_IMPLEMENTED = 'notImplemented'
ORGUNIT_NOT_FOUND = 'orgunitNotFound'
PERMISSION_DENIED = 'permissionDenied'
PERMISSION_NOT_FOUND = 'permissionNotFound'
PHOTO_NOT_FOUND = 'photoNotFound'
QUOTA_EXCEEDED = 'quotaExceeded'
RATE_LIMIT_EXCEEDED = 'rateLimitExceeded'
REQUIRED = 'required'
RESOURCE_ID_NOT_FOUND = 'resourceIdNotFound'
RESOURCE_NOT_FOUND = 'resourceNotFound'
SERVICE_LIMIT = 'serviceLimit'
SERVICE_NOT_AVAILABLE = 'serviceNotAvailable'
SYSTEM_ERROR = 'systemError'
TIME_RANGE_EMPTY = 'timeRangeEmpty'
UNKNOWN_ERROR = 'unknownError'
USER_NOT_FOUND = 'userNotFound'
USER_RATE_LIMIT_EXCEEDED = 'userRateLimitExceeded'
#
DEFAULT_RETRY_REASONS = [QUOTA_EXCEEDED, RATE_LIMIT_EXCEEDED, USER_RATE_LIMIT_EXCEEDED, BACKEND_ERROR, BAD_GATEWAY, INTERNAL_ERROR]
ACTIVITY_THROW_REASONS = [SERVICE_NOT_AVAILABLE]
CALENDAR_THROW_REASONS = [SERVICE_NOT_AVAILABLE, AUTH_ERROR, NOT_A_CALENDAR_USER]
DRIVE_THROW_REASONS = [SERVICE_NOT_AVAILABLE, AUTH_ERROR]
GMAIL_THROW_REASONS = [SERVICE_NOT_AVAILABLE, BAD_REQUEST]
GMAIL_SMIME_THROW_REASONS = [SERVICE_NOT_AVAILABLE, BAD_REQUEST, FORBIDDEN]
GPLUS_THROW_REASONS = [SERVICE_NOT_AVAILABLE]
GROUP_GET_RETRY_REASONS = [INVALID, SYSTEM_ERROR]
GROUP_GET_THROW_REASONS = [GROUP_NOT_FOUND, DOMAIN_NOT_FOUND, DOMAIN_CANNOT_USE_APIS, FORBIDDEN, BAD_REQUEST]
GROUP_SETTINGS_THROW_REASONS = [GROUP_NOT_FOUND, DOMAIN_NOT_FOUND, DOMAIN_CANNOT_USE_APIS, FORBIDDEN, SYSTEM_ERROR]
GROUP_SETTINGS_RETRY_REASONS = [INVALID, SERVICE_LIMIT]
MEMBERS_THROW_REASONS = [GROUP_NOT_FOUND, DOMAIN_NOT_FOUND, DOMAIN_CANNOT_USE_APIS, INVALID, FORBIDDEN]
MEMBERS_RETRY_REASONS = [SYSTEM_ERROR]
USER_GET_THROW_REASONS = [USER_NOT_FOUND, DOMAIN_NOT_FOUND, DOMAIN_CANNOT_USE_APIS, FORBIDDEN, BAD_REQUEST, SYSTEM_ERROR]

REASON_MESSAGE_MAP = {
  ABORTED: [
    ('Label name exists or conflicts', DUPLICATE),
    ],
  CONDITION_NOT_MET: [
    ('Cyclic memberships not allowed', CYCLIC_MEMBERSHIPS_NOT_ALLOWED),
    ('undelete', DELETED_USER_NOT_FOUND),
    ],
  FAILED_PRECONDITION: [
    ('Bad Request', BAD_REQUEST),
    ('Mail service not enabled', SERVICE_NOT_AVAILABLE),
    ],
  INVALID: [
    ('userId', USER_NOT_FOUND),
    ('memberKey', INVALID_MEMBER),
    ('A system error has occurred', SYSTEM_ERROR),
    ('Invalid Customer Id', INVALID_CUSTOMER_ID),
    ('Invalid Input: INVALID_OU_ID', INVALID_ORGUNIT),
    ('Invalid Input: custom_schema', INVALID_SCHEMA_VALUE),
    ('Invalid Input: resource', INVALID_RESOURCE),
    ('Invalid Input:', INVALID_INPUT),
    ('Invalid Org Unit', INVALID_ORGUNIT),
    ('Invalid Ou Id', INVALID_ORGUNIT),
    ('Invalid Parent Orgunit Id', INVALID_PARENT_ORGUNIT),
    ('Invalid query', INVALID_QUERY),
    ('Invalid scope value', INVALID_SCOPE_VALUE),
    ('New domain name is not a verified secondary domain', DOMAIN_NOT_VERIFIED_SECONDARY),
    ],
  INVALID_ARGUMENT: [
    ('Cannot delete primary send-as', CANNOT_DELETE_PRIMARY_SENDAS),
    ('Invalid id value', INVALID_MESSAGE_ID),
    ('Invalid ids value', INVALID_MESSAGE_ID),
    ],
  NOT_FOUND: [
    ('userKey', USER_NOT_FOUND),
    ('groupKey', GROUP_NOT_FOUND),
    ('memberKey', MEMBER_NOT_FOUND),
    ('photo', PHOTO_NOT_FOUND),
    ('resource_id', RESOURCE_ID_NOT_FOUND),
    ('resourceId', RESOURCE_ID_NOT_FOUND),
    ('Customer doesn\'t exist', CUSTOMER_NOT_FOUND),
    ('Domain alias does not exist', DOMAIN_ALIAS_NOT_FOUND),
    ('Domain not found', DOMAIN_NOT_FOUND),
    ('domain', DOMAIN_NOT_FOUND),
    ('File not found', FILE_NOT_FOUND),
    ('Org unit not found', ORGUNIT_NOT_FOUND),
    ('Permission not found', PERMISSION_NOT_FOUND),
    ('Resource Not Found', RESOURCE_NOT_FOUND),
    ('Not Found', NOT_FOUND),
    ],
  REQUIRED: [
    ('Login Required', LOGIN_REQUIRED),
    ('memberKey', MEMBER_NOT_FOUND),
    ],
  RESOURCE_NOT_FOUND: [
    ('resourceId', RESOURCE_ID_NOT_FOUND),
    ],
  }

class aborted(Exception):
  pass
class alreadyExists(Exception):
  pass
class authError(Exception):
  pass
class backendError(Exception):
  pass
class badRequest(Exception):
  pass
class cannotChangeOwnAcl(Exception):
  pass
class cannotChangeOwnerAcl(Exception):
  pass
class cannotDeletePrimaryCalendar(Exception):
  pass
class cannotDeletePrimarySendAs(Exception):
  pass
class conditionNotMet(Exception):
  pass
class connectionRefused(Exception):
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
class duplicate(Exception):
  pass
class failedPrecondition(Exception):
  pass
class fileNotFound(Exception):
  pass
class forbidden(Exception):
  pass
class groupNotFound(Exception):
  pass
class illegalAccessRoleForDefault(Exception):
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
class notACalendarUser(Exception):
  pass
class notFound(Exception):
  pass
class notImplemented(Exception):
  pass
class orgunitNotFound(Exception):
  pass
class permissionDenied(Exception):
  pass
class permissionNotFound(Exception):
  pass
class photoNotFound(Exception):
  pass
class required(Exception):
  pass
class resourceIdNotFound(Exception):
  pass
class resourceNotFound(Exception):
  pass
class serviceLimit(Exception):
  pass
class serviceNotAvailable(Exception):
  pass
class systemError(Exception):
  pass
class timeRangeEmpty(Exception):
  pass
class unknownError(Exception):
  pass
class userNotFound(Exception):
  pass

REASON_EXCEPTION_MAP = {
  ABORTED: aborted,
  ALREADY_EXISTS: alreadyExists,
  AUTH_ERROR: authError,
  BACKEND_ERROR: backendError,
  BAD_REQUEST: badRequest,
  CANNOT_CHANGE_OWN_ACL: cannotChangeOwnAcl,
  CANNOT_CHANGE_OWNER_ACL: cannotChangeOwnerAcl,
  CANNOT_DELETE_PRIMARY_CALENDAR: cannotDeletePrimaryCalendar,
  CANNOT_DELETE_PRIMARY_SENDAS: cannotDeletePrimarySendAs,
  CONDITION_NOT_MET: conditionNotMet,
  CONNECTION_REFUSED: connectionRefused,
  CUSTOMER_NOT_FOUND: customerNotFound,
  CYCLIC_MEMBERSHIPS_NOT_ALLOWED: cyclicMembershipsNotAllowed,
  DELETED: deleted,
  DELETED_USER_NOT_FOUND: deletedUserNotFound,
  DOMAIN_ALIAS_NOT_FOUND: domainAliasNotFound,
  DOMAIN_CANNOT_USE_APIS: domainCannotUseApis,
  DOMAIN_NOT_FOUND: domainNotFound,
  DOMAIN_NOT_VERIFIED_SECONDARY: domainNotVerifiedSecondary,
  DUPLICATE: duplicate,
  FAILED_PRECONDITION: failedPrecondition,
  FILE_NOT_FOUND: fileNotFound,
  FORBIDDEN: forbidden,
  GROUP_NOT_FOUND: groupNotFound,
  ILLEGAL_ACCESS_ROLE_FOR_DEFAULT: illegalAccessRoleForDefault,
  INSUFFICIENT_PERMISSIONS: insufficientPermissions,
  INTERNAL_ERROR: internalError,
  INVALID: invalid,
  INVALID_ARGUMENT: invalidArgument,
  INVALID_CUSTOMER_ID: invalidCustomerId,
  INVALID_INPUT: invalidInput,
  INVALID_MEMBER: invalidMember,
  INVALID_MESSAGE_ID: invalidMessageId,
  INVALID_ORGUNIT: invalidOrgunit,
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
  NOT_A_CALENDAR_USER: notACalendarUser,
  NOT_FOUND: notFound,
  NOT_IMPLEMENTED: notImplemented,
  ORGUNIT_NOT_FOUND: orgunitNotFound,
  PERMISSION_DENIED: permissionDenied,
  PERMISSION_NOT_FOUND: permissionNotFound,
  PHOTO_NOT_FOUND: photoNotFound,
  REQUIRED: required,
  RESOURCE_ID_NOT_FOUND: resourceIdNotFound,
  RESOURCE_NOT_FOUND: resourceNotFound,
  SERVICE_LIMIT: serviceLimit,
  SERVICE_NOT_AVAILABLE: serviceNotAvailable,
  SYSTEM_ERROR: systemError,
  TIME_RANGE_EMPTY: timeRangeEmpty,
  UNKNOWN_ERROR: unknownError,
  USER_NOT_FOUND: userNotFound,
  }
