"""
"""

from unittest import TestCase

from .stub import NetworkTrafficProviderStub
from src.domain.use_cases.network_traffic.read_network_traffic_data import ReadNetworkTrafficDataUseCase
from src.domain.models.response.read_network_traffic_data_response_model import ReadNetworkTrafficDataResponseModel

class UseCaseTestCase(TestCase):

    def test_use_case(self):
        provider = NetworkTrafficProviderStub()
        use_case = ReadNetworkTrafficDataUseCase(provider)

        actual = use_case.execute()
        expected = ReadNetworkTrafficDataResponseModel(
            network_traffic_data=provider.get_data()
        )

        self.assertEqual(actual, expected)
