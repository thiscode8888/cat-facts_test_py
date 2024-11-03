import pytest
from controllers.facts_controller import FactsController
from helpers.facts_helper import FactsHelper
from helpers.body_prettifier import prettifier
from assertpy.assertpy import assert_that

facts_controller = FactsController()
facts_helper = FactsHelper()

# testing positive scenarios
@pytest.mark.smoke
@pytest.mark.positive
def test_find_fact_by_id():
    response = facts_controller.find_by_id("58e00b5f0aac31001185ed24")
    assert_that(response.status_code).is_equal_to(200)

# testing negative scenarios
@pytest.mark.smoke
@pytest.mark.negative
def test_invalid_fact_id():
    response = facts_controller.find_by_id("58e00b5f0aa")
    assert_that(response.status_code).is_equal_to(400)

# testing headers
@pytest.mark.smoke
@pytest.mark.positive
def test_response_content_type():
    response = facts_controller.get_facts()
    assert_that(response.headers["Content-Type"]).is_equal_to("application/json; charset=utf-8")

# testing all request data and comparing JSON responses
@pytest.mark.smoke
@pytest.mark.positive
def test_json_response():
    body = facts_helper.valid_body()
    response = facts_controller.find_by_id("58e008780aac31001185ed05")
    assert_that(prettifier(response.text)).is_equal_to(body)