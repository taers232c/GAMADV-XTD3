# -*- coding: utf-8 -*-

# Copyright (C) 2023 Ross Scroggs All Rights Reserved.
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

"""Google Application Default Credentials"""

import datetime
import json

import google.auth
import google.oauth2.service_account

from gam import API_ACCESS_DENIED_RC
from gam import systemErrorExit
from gam import transportAuthorizedHttp, getHttpObj
from gam import getService
from gam import callGAPI
from gam.gamlib.api import GOOGLE_OAUTH2_TOKEN_ENDPOINT
from gam.gamlib.api import IAM_CREDENTIALS

_DEFAULT_TOKEN_LIFETIME_SECS = 3600  # 1 hour in seconds

class JWTCredentials(google.auth.jwt.Credentials):
  ''' Class used for DASA '''
  def _make_jwt(self):
    now = datetime.datetime.utcnow()
    lifetime = datetime.timedelta(seconds=self._token_lifetime)
    expiry = now + lifetime
    payload = {
      "iat": google.auth._helpers.datetime_to_secs(now),
      "exp": google.auth._helpers.datetime_to_secs(expiry),
      "iss": self._issuer,
      "sub": self._subject,
    }
    if self._audience:
      payload["aud"] = self._audience
    payload.update(self._additional_claims)
    jwt = self._signer.sign(payload)
    return jwt, expiry

class Credentials(google.oauth2.service_account.Credentials):
  ''' Class used for DwD '''

  def _make_authorization_grant_assertion(self):
    now = datetime.datetime.utcnow()
    lifetime = datetime.timedelta(seconds=_DEFAULT_TOKEN_LIFETIME_SECS)
    expiry = now + lifetime
    payload = {
        "iat": google.auth._helpers.datetime_to_secs(now),
        "exp": google.auth._helpers.datetime_to_secs(expiry),
        "iss": self._service_account_email,
        "aud": GOOGLE_OAUTH2_TOKEN_ENDPOINT,
        "scope": google.auth._helpers.scopes_to_string(self._scopes or ()),
    }
    payload.update(self._additional_claims)
    # The subject can be a user email for domain-wide delegation.
    if self._subject:
      payload.setdefault("sub", self._subject)
    token = self._signer(payload)
    return token

class SignJwt(google.auth.crypt.Signer):
  ''' Signer class for SignJWT '''
  def __init__(self, service_account_info):
    self.service_account_email = service_account_info['client_email']
    self.name = f'projects/-/serviceAccounts/{self.service_account_email}'
    self._key_id = None

  @property  # type: ignore
  def key_id(self):
    return self._key_id

  def sign(self, message):
    ''' Call IAM Credentials SignJWT API to get our signed JWT '''
    try:
      credentials, _ = google.auth.default()
    except google.auth.exceptions.DefaultCredentialsError as e:
      systemErrorExit(API_ACCESS_DENIED_RC, str(e))
    httpObj = transportAuthorizedHttp(credentials, http=getHttpObj())
    iamc = getService(IAM_CREDENTIALS, httpObj)
    response = callGAPI(iamc.projects().serviceAccounts(), 'signJwt',
                        name=self.name, body={'payload': json.dumps(message)})
    signed_jwt = response.get('signedJwt')
    return signed_jwt

