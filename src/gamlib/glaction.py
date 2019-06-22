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

"""GAM action processing

"""

class GamAction(object):

# Keys into NAMES; arbitrary values but must be unique
  ACCEPT = 'acpt'
  ADD = 'add '
  ADD_PREVIEW = 'addp'
  APPEND = 'apnd'
  ARCHIVE = 'arch'
  BACKUP = 'back'
  CANCEL = 'canc'
  CHECK = 'chek'
  CLAIM = 'clai'
  CLAIM_OWNERSHIP = 'clow'
  CLEAR = 'clea'
  CLOSE = 'clos'
  COLLECT = 'collect'
  COPY = 'copy'
  CREATE = 'crea'
  DEDUP = 'dedu'
  DELETE = 'dele'
  DELETE_EMPTY = 'delm'
  DEPROVISION = 'depr'
  DISABLE = 'disa'
  DOWNLOAD = 'down'
  DRAFT = 'draf'
  EMPTY = 'empt'
  ENABLE = 'enbl'
  EXPORT = 'expo'
  EXTRACT = 'extr'
  FETCH = 'fetc'
  FORWARD = 'forw'
  HIDE = 'hide'
  IMPORT = 'impo'
  INFO = 'info'
  INITIALIZE = 'init'
  INSERT = 'insr'
  INVALIDATE = 'inva'
  LIST = 'list'
  MERGE = 'merg'
  MODIFY = 'modi'
  MOVE = 'move'
  PERFORM = 'perf'
  PRINT = 'prin'
  PROCESS = 'proc'
  PURGE = 'purg'
  REENABLE = 'reen'
  REFRESH = 'refr'
  REGISTER = 'regi'
  RELABEL = 'rela'
  REMOVE = 'remo'
  REMOVE_PREVIEW = 'remp'
  RENAME = 'rena'
  REOPEN = 'reop'
  REPLACE = 'repl'
  REPORT = 'repo'
  RESTORE = 'rest'
  RESUBMIT = 'res'
  RETAIN = 'reta'
  RETRIEVE_DATA = 'retd'
  SAVE = 'save'
  SENDEMAIL = 'send'
  SET = 'set '
  SHOW = 'show'
  SKIP = u'skip'
  SPAM = 'spam'
  SUBMIT = 'subm'
  SUSPEND = 'susp'
  SYNC = 'sync'
  TRANSFER = 'tran'
  TRANSFER_OWNERSHIP = 'trow'
  TRASH = 'tras'
  UNDELETE = 'unde'
  UNHIDE = 'unhi'
  UNSUSPEND = 'unsu'
  UNTRASH = 'untr'
  UPDATE = 'upda'
  UPDATE_PREVIEW = 'updp'
  UPLOAD = 'uplo'
  UNZIP = 'unzi'
  USE = 'use '
  VERIFY = 'vrfy'
  WATCH = 'watc'
  WIPE = 'wipe'
  # Usage:
  # ACTION_NAMES[1] n Items - Delete 10 Users
  # Item xxx ACTION_NAMES[0] - User xxx Deleted
  # These values can be translated into other languages
  _NAMES = {
    ACCEPT: ['Accepted', 'Accept'],
    ADD: ['Added', 'Add'],
    ADD_PREVIEW: ['Added (Preview)', 'Add (Preview)'],
    APPEND: ['Appended', 'Append'],
    ARCHIVE: ['Archived', 'Archive'],
    BACKUP: ['Backed up', 'Backup'],
    CANCEL: ['Cancelled', 'Cancel'],
    CHECK: ['Checked', 'Check'],
    CLAIM: ['Claimed', 'Claim'],
    CLAIM_OWNERSHIP: ['Ownership Claimed', 'Claim Ownership'],
    CLEAR: ['Cleared', 'Clear'],
    CLOSE: ['Closed', 'Close'],
    COLLECT: ['Collected', 'Collect'],
    COPY: ['Copied', 'Copy'],
    CREATE: ['Created', 'Create'],
    DEDUP: ['Duplicates Deleted', 'Delete Duplicates'],
    DELETE: ['Deleted', 'Delete'],
    DELETE_EMPTY: ['Deleted', 'Delete Empty'],
    DEPROVISION: ['Deprovisioned', 'Deprovision'],
    DISABLE: ['Disabled', 'Disable'],
    DOWNLOAD: ['Downloaded', 'Download'],
    DRAFT: ['Drafted', 'Draft'],
    EMPTY: ['Emptied', 'Empty'],
    ENABLE: ['Enabled', 'Enable'],
    EXPORT: ['Exported', 'Export'],
    EXTRACT: ['Extracted', 'Extract'],
    FORWARD: ['Forwarded', 'Forward'],
    HIDE: ['Hidden', 'Hide'],
    IMPORT: ['Imported', 'Import'],
    INFO: ['Shown', 'Show Info'],
    INITIALIZE: ['Initialized', 'Initialize'],
    INSERT: ['Inserted', 'Insert'],
    INVALIDATE: ['Invalidated', 'Invalidate'],
    LIST: ['Listed', 'List'],
    MERGE: ['Merged', 'Merge'],
    MODIFY: ['Modified', 'Modify'],
    MOVE: ['Moved', 'Move'],
    PERFORM: ['Action Performed', 'Perform Action'],
    PRINT: ['Printed', 'Print'],
    PROCESS: ['Processed', 'Process'],
    PURGE: ['Purged', 'Purge'],
    REENABLE: ['Reenabled', 'Reenable'],
    REFRESH: ['Refreshed', 'Refresh'],
    REGISTER: ['Registered', 'Register'],
    RELABEL: ['Relabeled', 'Relabel'],
    REMOVE: ['Removed', 'Remove'],
    REMOVE_PREVIEW: ['Removed (Preview)', 'Remove (Preview)'],
    RENAME: ['Renamed', 'Rename'],
    REOPEN: ['Reopened', 'Reopen'],
    REPLACE: ['Replaced', 'Replace'],
    REPORT: ['Reported', 'Report'],
    RESTORE: ['Restored', 'Restore'],
    RESUBMIT: ['Resubmitted', 'Resubmit'],
    RETAIN: ['Retained', 'Retain'],
    RETRIEVE_DATA: ['Data Retrieved', 'Retrieve Data'],
    SAVE: ['Saved', 'Save'],
    SENDEMAIL: ['Email Sent', 'Send Email'],
    SET: ['Set', 'Set'],
    SHOW: ['Shown', 'Show'],
    SKIP: ['Skipped', 'Skip'],
    SPAM: ['Marked as Spam', 'Mark as Spam'],
    SUBMIT: ['Submitted', 'Submit'],
    SUSPEND: ['Suspended', 'Suspend'],
    SYNC: ['Synced', 'Sync'],
    TRANSFER: ['Transferred', 'Transfer'],
    TRANSFER_OWNERSHIP: ['Ownership Transferred', 'Transfer Ownership'],
    TRASH: ['Trashed', 'Trash'],
    UNDELETE: ['Undeleted', 'Undelete'],
    UNHIDE: ['Unhidden', 'Unhide'],
    UNSUSPEND: ['Unsuspended', 'Unsuspend'],
    UNTRASH: ['Untrashed', 'Untrash'],
    UNZIP: ['Unzipped', 'Unzip'],
    UPDATE: ['Updated', 'Update'],
    UPDATE_PREVIEW: ['Updated (Preview)', 'Update (Preview)'],
    UPLOAD: ['Uploaded', 'Upload'],
    USE: ['Used', 'Use'],
    VERIFY: ['Verified', 'Verify'],
    WATCH: ['Watched', 'Watch'],
    WIPE: ['Wiped', 'Wipe'],
    }
  #
  MODIFIER_CONTENTS_WITH = 'contents with'
  MODIFIER_FOR = 'for'
  MODIFIER_FROM = 'from'
  MODIFIER_IN = 'in'
  MODIFIER_INTO = 'into'
  MODIFIER_TO = 'to'
  MODIFIER_WITH = 'with'
  MODIFIER_WITH_CONTENT_FROM = 'with content from'
  PREFIX_NOT = 'Not'
  SUFFIX_FAILED = 'Failed'

  def __init__(self):
    self.action = None

  def Set(self, action):
    self.action = action

  def Get(self):
    return self.action

  def ToPerform(self):
    return self._NAMES[self.action][1]

  def Performed(self):
    return self._NAMES[self.action][0]

  def Failed(self):
    return '{0} {1}'.format(self._NAMES[self.action][1], self.SUFFIX_FAILED)

  def NotPerformed(self):
    actionWords = self._NAMES[self.action][0].split(' ')
    if len(actionWords) != 2:
      return '{0} {1}'.format(self.PREFIX_NOT, self._NAMES[self.action][0])
    return '{0} {1} {2}'.format(actionWords[0], self.PREFIX_NOT, actionWords[1])

  def PerformedName(self, action):
    return self._NAMES[action][0]

  def csvFormat(self):
    return self.action == self.PRINT
