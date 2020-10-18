import pytest
from test_base import BaseTest
from Config.constants import TestData
from Utils.common import read_data_from_csv
from Utils.common import get


class DeweyTest(BaseTest):

    @pytest.mark.parametrize("customerid, email", read_data_from_csv(TestData.DEWEY_CSV_PATH))
    def test_customer_sync_with_data_from_csv(self, customerid, email):
        url = self.dewey_host + "/customer/" + customerid + "/sync"
        response_body = get(url=url)
        assert response_body["email"] == email
        assert response_body["id"] == customerid
        assert len(response_body) == 10


    @pytest.mark.parametrize("customerid, email", read_data_from_csv(TestData.DEWEY_CSV_PATH))
    def test_customer_with_data_from_csv(self, customerid, email):
        url = self.dewey_host + "/customer/" + customerid + "/"
        response_body = get(url=url)
        assert response_body["email"] == email
        assert response_body["id"] == customerid
        assert len(response_body) == 10

    # @pytest.mark.smoke
    @pytest.mark.parametrize("customerid, email", read_data_from_csv(TestData.DEWEY_CSV_PATH))
    def test_customer_extended_with_data_from_csv(self, customerid, email):
        url = self.dewey_host + "/customer/" + customerid + "/extended"
        response_body = get(url=url)
        assert response_body["email"] == email
        assert response_body["id"] == customerid
        assert len(response_body) == 21
