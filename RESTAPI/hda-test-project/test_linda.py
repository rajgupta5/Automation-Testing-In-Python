from Utils.common import get
from Utils.common import post
from Utils.common import read_data_from_csv
import requests
import pytest
from test_base import BaseTest
from Config.constants import TestData
from Utils.common import create_hotel_compset_watcher_json_object, \
    create_car_compset_watcher_json_object

class LindaTest(BaseTest):

    @pytest.mark.parametrize("customerid, email", read_data_from_csv(TestData.LINDA_CSV_PATH))
    def test_hotel_compset_watcher(self, customerid, email):
        url = self.linda_host + "/linda-cache/compset-watchers?hood-id=89686&star-rating=2.5&percent-recommended=85" \
                                "&start-date=2020-11-09&end-date=2020-11-12&num-rooms=1&num-adults=2&num-children=0" \
                                "&lodging_type=H"

        get_response_body = get(url)
        assert len(get_response_body) == 0, "Before Post: Length is not 0"

        post_url = self.linda_host + "/linda-cache/watched-compsets?customer-id=" + customerid
        post_response = post(url=post_url, data=create_hotel_compset_watcher_json_object())
        assert post_response.text == '1 watches are updated for the customer ' + customerid + ' for vertical Hotel'

        get_response_body = get(url)
        assert len(get_response_body) == 1, "After Post: Length is not 1"

        delete_url = self.linda_host + "/linda-cache/watched-compsets?customer-id=" + customerid
        delete_response = requests.delete(delete_url)
        assert delete_response.status_code == 200
        assert delete_response.text == '1 watched Compsets for customer ' + customerid + ' are removed from compset-winner cache successfully!!!'

        get_response_body = get(url)
        assert len(get_response_body) == 0, "After Delete: Length is not 0"

    @pytest.mark.parametrize("customerid, email", read_data_from_csv(TestData.LINDA_CSV_PATH))
    def test_car_compset_watcher(self, customerid, email):
        url = self.linda_host + "/linda-cache/compset-watchers/car?car-type=CCAR&rate-type=RETAIL&rental-agency=ZE" \
                                "&pickup=JFK&dropOff=JFK&start-date=2020-11-10&end-date=2020-11-15"

        get_response_body = get(url)
        assert len(get_response_body) == 0, "Before Post: Length is not 0"

        post_url = self.linda_host + "/linda-cache/watched-compsets/car?customer-id=" + customerid
        post_response = post(url=post_url, data=create_car_compset_watcher_json_object())
        assert post_response.text == '1 watches are updated for the customer ' + customerid + ' for vertical car'

        get_response_body = get(url)
        assert len(get_response_body) == 1,  "After Post: Length is not 1"

        delete_url = self.linda_host + "/linda-cache/watched-compsets/car?customer-id=" + customerid
        delete_response = requests.delete(delete_url)
        assert delete_response.status_code == 200
        assert delete_response.text == '1 watched Compsets for customer ' + customerid + ' are removed from compset-winner cache successfully!!!'

        get_response_body = get(url)
        assert len(get_response_body) == 0, "After Delete: Length is not 0"
