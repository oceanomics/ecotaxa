# coding: utf-8

"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from to_back.ecotaxa_cli_py.api_client import ApiClient
from to_back.ecotaxa_cli_py.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_export_emodnet_export_emodnet_post(self, emod_net_export_req, **kwargs):  # noqa: E501
        """Api Export Emodnet  # noqa: E501

        Export in EMODnet format, @see https://www.emodnet-ingestion.eu/ Produces a DwC-A archive into a temporary directory, ready for download. https://python-dwca-reader.readthedocs.io/en/latest/index.html  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_export_emodnet_export_emodnet_post(emod_net_export_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param EMODNetExportReq emod_net_export_req: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EMODNetExportRsp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_export_emodnet_export_emodnet_post_with_http_info(emod_net_export_req, **kwargs)  # noqa: E501

    def api_export_emodnet_export_emodnet_post_with_http_info(self, emod_net_export_req, **kwargs):  # noqa: E501
        """Api Export Emodnet  # noqa: E501

        Export in EMODnet format, @see https://www.emodnet-ingestion.eu/ Produces a DwC-A archive into a temporary directory, ready for download. https://python-dwca-reader.readthedocs.io/en/latest/index.html  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_export_emodnet_export_emodnet_post_with_http_info(emod_net_export_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param EMODNetExportReq emod_net_export_req: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EMODNetExportRsp, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'emod_net_export_req'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_export_emodnet_export_emodnet_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'emod_net_export_req' is set
        if self.api_client.client_side_validation and ('emod_net_export_req' not in local_var_params or  # noqa: E501
                                                        local_var_params['emod_net_export_req'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `emod_net_export_req` when calling `api_export_emodnet_export_emodnet_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'emod_net_export_req' in local_var_params:
            body_params = local_var_params['emod_net_export_req']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBearer']  # noqa: E501

        return self.api_client.call_api(
            '/export/emodnet', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EMODNetExportRsp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_import_import_prep_project_id_post(self, project_id, import_prep_req, **kwargs):  # noqa: E501
        """Api Import  # noqa: E501

        Prepare/validate the import of an EcoTaxa archive or directory.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_import_import_prep_project_id_post(project_id, import_prep_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int project_id: (required)
        :param ImportPrepReq import_prep_req: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ImportPrepRsp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_import_import_prep_project_id_post_with_http_info(project_id, import_prep_req, **kwargs)  # noqa: E501

    def api_import_import_prep_project_id_post_with_http_info(self, project_id, import_prep_req, **kwargs):  # noqa: E501
        """Api Import  # noqa: E501

        Prepare/validate the import of an EcoTaxa archive or directory.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_import_import_prep_project_id_post_with_http_info(project_id, import_prep_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int project_id: (required)
        :param ImportPrepReq import_prep_req: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ImportPrepRsp, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'import_prep_req'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_import_import_prep_project_id_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `api_import_import_prep_project_id_post`")  # noqa: E501
        # verify the required parameter 'import_prep_req' is set
        if self.api_client.client_side_validation and ('import_prep_req' not in local_var_params or  # noqa: E501
                                                        local_var_params['import_prep_req'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `import_prep_req` when calling `api_import_import_prep_project_id_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'import_prep_req' in local_var_params:
            body_params = local_var_params['import_prep_req']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBearer']  # noqa: E501

        return self.api_client.call_api(
            '/import_prep/{project_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImportPrepRsp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_import_import_real_project_id_post(self, project_id, import_real_req, **kwargs):  # noqa: E501
        """Api Import  # noqa: E501

        Import an EcoTaxa archive or directory.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_import_import_real_project_id_post(project_id, import_real_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int project_id: (required)
        :param ImportRealReq import_real_req: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_import_import_real_project_id_post_with_http_info(project_id, import_real_req, **kwargs)  # noqa: E501

    def api_import_import_real_project_id_post_with_http_info(self, project_id, import_real_req, **kwargs):  # noqa: E501
        """Api Import  # noqa: E501

        Import an EcoTaxa archive or directory.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_import_import_real_project_id_post_with_http_info(project_id, import_real_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int project_id: (required)
        :param ImportRealReq import_real_req: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'import_real_req'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_import_import_real_project_id_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `api_import_import_real_project_id_post`")  # noqa: E501
        # verify the required parameter 'import_real_req' is set
        if self.api_client.client_side_validation and ('import_real_req' not in local_var_params or  # noqa: E501
                                                        local_var_params['import_real_req'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `import_real_req` when calling `api_import_import_real_project_id_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'import_real_req' in local_var_params:
            body_params = local_var_params['import_real_req']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBearer']  # noqa: E501

        return self.api_client.call_api(
            '/import_real/{project_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_import_simple_import_project_id_post(self, project_id, simple_import_req, **kwargs):  # noqa: E501
        """Api Import  # noqa: E501

        Import images only, with same metadata for all.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_import_simple_import_project_id_post(project_id, simple_import_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int project_id: (required)
        :param SimpleImportReq simple_import_req: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SimpleImportRsp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_import_simple_import_project_id_post_with_http_info(project_id, simple_import_req, **kwargs)  # noqa: E501

    def api_import_simple_import_project_id_post_with_http_info(self, project_id, simple_import_req, **kwargs):  # noqa: E501
        """Api Import  # noqa: E501

        Import images only, with same metadata for all.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_import_simple_import_project_id_post_with_http_info(project_id, simple_import_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int project_id: (required)
        :param SimpleImportReq simple_import_req: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SimpleImportRsp, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'simple_import_req'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_import_simple_import_project_id_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `api_import_simple_import_project_id_post`")  # noqa: E501
        # verify the required parameter 'simple_import_req' is set
        if self.api_client.client_side_validation and ('simple_import_req' not in local_var_params or  # noqa: E501
                                                        local_var_params['simple_import_req'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `simple_import_req` when calling `api_import_simple_import_project_id_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'simple_import_req' in local_var_params:
            body_params = local_var_params['simple_import_req']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBearer']  # noqa: E501

        return self.api_client.call_api(
            '/simple_import/{project_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimpleImportRsp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_resolve_taxon_taxon_resolve_our_id_get(self, our_id, **kwargs):  # noqa: E501
        """Api Resolve Taxon  # noqa: E501

        Resolve in WoRMs the given taxon.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_resolve_taxon_taxon_resolve_our_id_get(our_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int our_id: (required)
        :param object t:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_resolve_taxon_taxon_resolve_our_id_get_with_http_info(our_id, **kwargs)  # noqa: E501

    def api_resolve_taxon_taxon_resolve_our_id_get_with_http_info(self, our_id, **kwargs):  # noqa: E501
        """Api Resolve Taxon  # noqa: E501

        Resolve in WoRMs the given taxon.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_resolve_taxon_taxon_resolve_our_id_get_with_http_info(our_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int our_id: (required)
        :param object t:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'our_id',
            't'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_resolve_taxon_taxon_resolve_our_id_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'our_id' is set
        if self.api_client.client_side_validation and ('our_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['our_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `our_id` when calling `api_resolve_taxon_taxon_resolve_our_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'our_id' in local_var_params:
            path_params['our_id'] = local_var_params['our_id']  # noqa: E501

        query_params = []
        if 't' in local_var_params and local_var_params['t'] is not None:  # noqa: E501
            query_params.append(('t', local_var_params['t']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/taxon/resolve/{our_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_status_status_get(self, **kwargs):  # noqa: E501
        """Api Status  # noqa: E501

        Report the status, mainly used for verifying that the server is up.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_status_status_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_status_status_get_with_http_info(**kwargs)  # noqa: E501

    def api_status_status_get_with_http_info(self, **kwargs):  # noqa: E501
        """Api Status  # noqa: E501

        Report the status, mainly used for verifying that the server is up.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_status_status_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_status_status_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
