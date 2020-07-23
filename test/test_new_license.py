# coding: utf-8

"""
    Kloudio APIs

"""


from __future__ import absolute_import

import unittest
import datetime

import kloudio
from kloudio.models.new_license import NewLicense  # noqa: E501
from kloudio.rest import ApiException

class TestNewLicense(unittest.TestCase):
    """NewLicense unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewLicense
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kloudio.models.new_license.NewLicense()  # noqa: E501
        if include_optional :
            return NewLicense(
                first_name = 'John', 
                id = 3995, 
                last_name = 'Doe', 
                email = 'admin@kloud.io', 
                role = 'creator | viewer'
            )
        else :
            return NewLicense(
                first_name = 'John',
                id = 3995,
                last_name = 'Doe',
                email = 'admin@kloud.io',
                role = 'creator | viewer',
        )

    def testNewLicense(self):
        """Test NewLicense"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
