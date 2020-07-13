# -*- coding: utf-8 -*-
"""DNA Center Sites API wrapper.

Copyright (c) 2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
)


class Sites(object):
    """DNA Center Sites API (version: 1.3.0).

    Wraps the DNA Center Sites
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Sites object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Sites, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_site_health(self,
                        timestamp,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Returns Overall Health information for all sites.

        Args:
            timestamp(basestring): Epoch time(in milliseconds) when
                the Site Hierarchy data is required.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(timestamp, basestring,
                   may_be_none=False)
        if headers is not None:
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
            'timestamp':
                timestamp,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_17a82ac94cf99ab0_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(headers)
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/site-health')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload, headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_17a82ac94cf99ab0_v1_3_0', json_data)

    def update_site(self,
                    site_id,
                    site=None,
                    type=None,
                    headers=None,
                    payload=None,
                    active_validation=True,
                    **request_parameters):
        """Update site area/building/floor with specified hierarchy and new
        values.

        Args:
            site(object): Site, property of the request body.
            type(string): Type, property of the request body.
                Available values are 'area', 'building'
                and 'floor'.
            site_id(basestring): site id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, basestring,
                   may_be_none=False)
        if headers is not None:
            check_type(headers.get('__runsync',
                                   self._session.headers.get(
                                       '__runsync')),
                       bool, may_be_none=False)
            check_type(headers.get('__runsynctimeout',
                                   self._session.headers.get(
                                       '__runsynctimeout')),
                       int)
            check_type(headers.get('__persistbapioutput',
                                   self._session.headers.get(
                                       '__persistbapioutput')),
                       bool, may_be_none=False)
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'siteId': site_id,
        }

        _payload = {
            'type':
                type,
            'site':
                site,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_33aab9b842388023_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(headers)
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/site/${siteId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_33aab9b842388023_v1_3_0', json_data)

    def create_site(self,
                    site=None,
                    type=None,
                    headers=None,
                    payload=None,
                    active_validation=True,
                    **request_parameters):
        """Creates site with area/building/floor with specified hierarchy.

        Args:
            site(object): Site, property of the request body.
            type(string): Type, property of the request body.
                Available values are 'area', 'building'
                and 'floor'.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            check_type(headers.get('__runsync',
                                   self._session.headers.get(
                                       '__runsync')),
                       bool, may_be_none=False)
            check_type(headers.get('__runsynctimeout',
                                   self._session.headers.get(
                                       '__runsynctimeout')),
                       int)
            check_type(headers.get('__persistbapioutput',
                                   self._session.headers.get(
                                       '__persistbapioutput')),
                       bool, may_be_none=False)
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
            'type':
                type,
            'site':
                site,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_23896b124bd8b9bf_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(headers)
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/site')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_23896b124bd8b9bf_v1_3_0', json_data)

    def get_site(self,
                 limit=None,
                 name=None,
                 offset=None,
                 site_id=None,
                 type=None,
                 headers=None,
                 payload=None,
                 active_validation=True,
                 **request_parameters):
        """Get site with area/building/floor with specified hierarchy.

        Args:
            name(basestring): groupNameHierarchy (ex:
                global/groupName).
            site_id(basestring): site id.
            type(basestring): type (ex: area, building, floor).
            offset(int): offset/starting row.
            limit(int): Number of sites to be retrieved.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(name, basestring)
        check_type(site_id, basestring)
        check_type(type, basestring)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            check_type(headers.get('__runsync',
                                   self._session.headers.get(
                                       '__runsync')),
                       bool, may_be_none=False)
            check_type(headers.get('__runsynctimeout',
                                   self._session.headers.get(
                                       '__runsynctimeout')),
                       int)
            check_type(headers.get('__persistbapioutput',
                                   self._session.headers.get(
                                       '__persistbapioutput')),
                       bool, may_be_none=False)
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
            'name':
                name,
            'siteId':
                site_id,
            'type':
                type,
            'offset':
                offset,
            'limit':
                limit,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_209509d247599e19_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(headers)
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/site')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload, headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_209509d247599e19_v1_3_0', json_data)

    def delete_site(self,
                    site_id,
                    headers=None,
                    payload=None,
                    active_validation=True,
                    **request_parameters):
        """Delete site with area/building/floor by siteId.

        Args:
            site_id(basestring): site id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, basestring,
                   may_be_none=False)
        if headers is not None:
            check_type(headers.get('__runsync',
                                   self._session.headers.get(
                                       '__runsync')),
                       bool, may_be_none=False)
            check_type(headers.get('__runsynctimeout',
                                   self._session.headers.get(
                                       '__runsynctimeout')),
                       int)
            check_type(headers.get('__persistbapioutput',
                                   self._session.headers.get(
                                       '__persistbapioutput')),
                       bool, may_be_none=False)
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'siteId': site_id,
        }

        _payload = {
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_92acda91406aa050_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(headers)
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/site/${siteId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=params,
                                             json=_payload, headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=params,
                                             json=_payload)

        return self._object_factory('bpm_92acda91406aa050_v1_3_0', json_data)

    def get_site_count(self,
                       site_id=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """API to get site count .

        Args:
            site_id(basestring): site id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, basestring)
        if headers is not None:
            check_type(headers.get('__persistbapioutput',
                                   self._session.headers.get(
                                       '__persistbapioutput')),
                       bool, may_be_none=False)
            check_type(headers.get('__runsynctimeout',
                                   self._session.headers.get(
                                       '__runsynctimeout')),
                       int)
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
            'siteId':
                site_id,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d9bdb9034df99dba_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(headers)
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/site/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload, headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_d9bdb9034df99dba_v1_3_0', json_data)

    def assign_device_to_site(self,
                              site_id,
                              device=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **request_parameters):
        """Assigns list of devices to a site.

        Args:
            device(list): Device, property of the request body (list
                of objects).
            site_id(basestring): Site id to which the device is
                assigned.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, basestring,
                   may_be_none=False)
        if headers is not None:
            check_type(headers.get('__runsync',
                                   self._session.headers.get(
                                       '__runsync')),
                       bool, may_be_none=False)
            check_type(headers.get('__persistbapioutput',
                                   self._session.headers.get(
                                       '__persistbapioutput')),
                       bool, may_be_none=False)
            check_type(headers.get('__runsynctimeout',
                                   self._session.headers.get(
                                       '__runsynctimeout')),
                       int)
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'siteId': site_id,
        }

        _payload = {
            'device':
                device,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_eeb168eb41988e07_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(headers)
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/site/${siteId}/device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_eeb168eb41988e07_v1_3_0', json_data)

    def get_membership(self,
                       site_id,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """Getting the site children details and device details.

        Args:
            site_id(basestring): site id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, basestring,
                   may_be_none=False)
        if headers is not None:
            check_type(headers.get('__runsync',
                                   self._session.headers.get(
                                       '__runsync')),
                       bool)
            check_type(headers.get('__runsynctimeout',
                                   self._session.headers.get(
                                       '__runsynctimeout')),
                       int)
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'siteId':
                site_id,
        }

        _payload = {
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_eba669054e08a60e_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(headers)
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/membership/${siteId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload, headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_eba669054e08a60e_v1_3_0', json_data)
