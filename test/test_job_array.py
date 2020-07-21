# coding: utf-8

"""
    Kloudio APIs

"""


from __future__ import absolute_import

import unittest
import datetime

import kloudio
from kloudio.models.job_array import JobArray  # noqa: E501
from kloudio.rest import ApiException

class TestJobArray(unittest.TestCase):
    """JobArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobArray
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kloudio.models.job_array.JobArray()  # noqa: E501
        if include_optional :
            return JobArray(
                job_ids = [12,1231,432]
            )
        else :
            return JobArray(
                job_ids = [12,1231,432],
        )

    def testJobArray(self):
        """Test JobArray"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
