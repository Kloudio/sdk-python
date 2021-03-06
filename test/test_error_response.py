# coding: utf-8

"""
    Kloudio APIs

"""


from __future__ import absolute_import

import unittest
import datetime

import kloudio
from kloudio.models.error_response import ErrorResponse  # noqa: E501
from kloudio.rest import ApiException

class TestErrorResponse(unittest.TestCase):
    """ErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ErrorResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kloudio.models.error_response.ErrorResponse()  # noqa: E501
        if include_optional :
            return ErrorResponse(
                id = 'XNfpjL4C9ZyCxo6j', 
                resource = 'connections | jobs | reports | templates | teams', 
                error = 'invalid_id | connection_already_exists', 
                message = 'The ID you have provided does not exist'
            )
        else :
            return ErrorResponse(
                error = 'invalid_id | connection_already_exists',
                message = 'The ID you have provided does not exist',
        )

    def testErrorResponse(self):
        """Test ErrorResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
