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

"""Google SKUs

"""

import re

# Products/SKUs
_PRODUCTS = {
  u'101001': u'Cloud Identity',
  u'101005': u'Cloud Identity Premium',
  u'101031': u'G Suite Enterprise for Education',
  u'Google-Apps': u'G Suite',
  u'Google-Chrome-Device-Management': u'Google Chrome Device Management',
  u'Google-Coordinate': u'Google Coordinate',
  u'Google-Drive-storage': u'Google Drive storage',
  u'Google-Vault': u'Google Vault',
  }
_SKUS = {
  u'1010010001': {
    u'product': u'101001', u'aliases': [u'identity', u'cloudidentity'], u'displayName': 'Cloud Identity'},
  u'1010050001': {
    u'product': u'101005', u'aliases': [u'identitypremium', u'cloudidentitypremium'], u'displayName': 'Cloud Identity Premium'},
  u'1010310002': {
    u'product': u'101031', u'aliases': [u'gsefe', u'e4e', u'gsuiteenterpriseeducation'], u'displayName': u'G Suite Enterprise for Education'},
  u'Google-Apps': {
    u'product': u'Google-Apps', u'aliases': [u'standard', u'free'], u'displayName': u'G Suite Free/Standard'},
  u'Google-Apps-For-Business': {
    u'product': u'Google-Apps', u'aliases': [u'gafb', u'gafw', u'basic', u'gsuitebasic'], u'displayName': u'G Suite Basic'},
  u'Google-Apps-For-Government': {
    u'product': u'Google-Apps', u'aliases': [u'gafg', u'gsuitegovernment', u'gsuitegov'], u'displayName': u'G Suite Government'},
  u'Google-Apps-For-Postini': {
    u'product': u'Google-Apps', u'aliases': [u'gams', u'postini', u'gsuitegams', u'gsuitepostini', u'gsuitemessagesecurity'], u'displayName': u'G Suite Message Security'},
  u'Google-Apps-Lite': {
    u'product': u'Google-Apps', u'aliases': [u'gal', u'lite', u'gsuitelite'], u'displayName': u'G Suite Lite'},
  u'Google-Apps-Unlimited': {
    u'product': u'Google-Apps', u'aliases': [u'gau', u'unlimited', u'gsuitebusiness'], u'displayName': u'G Suite Business'},
  u'1010020020': {
    u'product': u'Google-Apps', u'aliases': [u'gae', u'enterprise', u'gsuiteenterprise'], u'displayName': u'G Suite Enterprise'},
  u'Google-Drive-storage-20GB': {
    u'product': u'Google-Drive-storage', u'aliases': [u'drive20gb', u'20gb', u'googledrivestorage20gb'], u'displayName': u'Google Drive Storage 20GB'},
  u'Google-Drive-storage-50GB': {
    u'product': u'Google-Drive-storage', u'aliases': [u'drive50gb', u'50gb', u'googledrivestorage50gb'], u'displayName': u'Google Drive Storage 50GB'},
  u'Google-Drive-storage-200GB': {
    u'product': u'Google-Drive-storage', u'aliases': [u'drive200gb', u'200gb', u'googledrivestorage200gb'], u'displayName': u'Google Drive Storage 200GB'},
  u'Google-Drive-storage-400GB': {
    u'product': u'Google-Drive-storage', u'aliases': [u'drive400gb', u'400gb', u'googledrivestorage400gb'], u'displayName': u'Google Drive Storage 400GB'},
  u'Google-Drive-storage-1TB': {
    u'product': u'Google-Drive-storage', u'aliases': [u'drive1tb', u'1tb', u'googledrivestorage1tb'], u'displayName': u'Google Drive Storage 1TB'},
  u'Google-Drive-storage-2TB': {
    u'product': u'Google-Drive-storage', u'aliases': [u'drive2tb', u'2tb', u'googledrivestorage2tb'], u'displayName': u'Google Drive Storage 2TB'},
  u'Google-Drive-storage-4TB': {
    u'product': u'Google-Drive-storage', u'aliases': [u'drive4tb', u'4tb', u'googledrivestorage4tb'], u'displayName': u'Google Drive Storage 4TB'},
  u'Google-Drive-storage-8TB': {
    u'product': u'Google-Drive-storage', u'aliases': [u'drive8tb', u'8tb', u'googledrivestorage8tb'], u'displayName': u'Google Drive Storage 8TB'},
  u'Google-Drive-storage-16TB': {
    u'product': u'Google-Drive-storage', u'aliases': [u'drive16tb', u'16tb', u'googledrivestorage16tb'], u'displayName': u'Google Drive Storage 16TB'},
  u'Google-Vault': {
    u'product': u'Google-Vault', u'aliases': [u'vault', u'googlevault'], u'displayName': u'Google Vault'},
  u'Google-Vault-Former-Employee': {
    u'product': u'Google-Vault', u'aliases': [u'vfe', u'googlevaultformeremployee'], u'displayName': u'Google Vault Former Employee'},
  u'Google-Coordinate': {
    u'product': u'Google-Coordinate', u'aliases': [u'coordinate', u'googlecoordinate'], u'displayName': u'Google Coordinate'},
  u'Google-Chrome-Device-Management': {
    u'product': u'Google-Chrome-Device-Management', u'aliases': [u'chrome', u'cdm', u'googlechromedevicemanagement'], u'displayName': u'Google Chrome Device Management'}
  }

def getProductAndSKU(sku):
  l_sku = sku.lower().replace(u'-', u'').replace(u' ', u'')
  for a_sku, sku_values in list(_SKUS.items()):
    if l_sku == a_sku.lower().replace(u'-', u'') or l_sku in sku_values[u'aliases'] or l_sku == sku_values[u'displayName'].lower().replace(u' ', u''):
      return (sku_values[u'product'], a_sku)
  try:
    product = re.search(u'^([A-Z,a-z]*-[A-Z,a-z]*)', sku).group(1)
  except AttributeError:
    product = sku
  return (product, sku)

def productIdToDisplayName(productId):
  return _PRODUCTS.get(productId, productId)

def formatProductIdDisplayName(productId):
  productIdDisplay = productIdToDisplayName(productId)
  if productId == productIdDisplay:
    return productId
  return u'{0} ({1})'.format(productId, productIdDisplay)

def normalizeProductId(product):
  l_product = product.lower().replace(u'-', u'').replace(u' ', u'')
  for a_sku, sku_values in list(_SKUS.items()):
    if ((l_product == sku_values[u'product'].lower().replace(u'-', u''))
        or (l_product == a_sku.lower().replace(u'-', u''))
        or (l_product in sku_values[u'aliases'])
        or (l_product == sku_values[u'displayName'].lower().replace(u' ', u''))):
      return sku_values[u'product']
  return product

def getSortedProductList():
  return sorted(_PRODUCTS.keys())

def skuIdToDisplayName(skuId):
  return _SKUS[skuId][u'displayName'] if skuId in _SKUS else skuId

def formatSKUIdDisplayName(skuId):
  skuIdDisplay = skuIdToDisplayName(skuId)
  if skuId == skuIdDisplay:
    return skuId
  return u'{0} ({1})'.format(skuId, skuIdDisplay)

def getSortedSKUList():
  return sorted(_SKUS.keys())

def convertProductListToSKUList(productList):
  skuList = []
  for productId in productList:
    skuList += [skuId for skuId in _SKUS if _SKUS[skuId][u'product'] == productId]
  return skuList

def getGSuiteSKUs():
  return convertProductListToSKUList([u'Google-Apps', u'101031'])
