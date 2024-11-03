## Run Python Cat-Facts API Tests
![Running Python cat-facts API tests](py_cat-facts_apitest.gif)

## Run Locally
1. Install [python >= 3.8](https://www.python.org/downloads/)
2. Run `pip install -r requirements.txt`
3. Run `pytest -s`

## Test Features
* Using PyTest with XDist and ReportPortal to enhance the speed and logging of the test runs.

## Test Cases
| Header    | Heading |
| --------- | ------- |
| Find Fact by ID & Assert Status Code (200) | Asserting request's response status code is as expected. A basic test to verify positive scenarios. |
| Invalid Fact ID to Assert Negative Status Code (400) | Asserting that providing the wrong fact ID, gives the correct negative response. A basic test to verify negative scenarios. |
| Facts API Response Content Type Check | Verify response headers for content type. Headers are a very important part of API requests and therefore here we have a basic header test to verify the responses' content.         |
| Facts API Response Body Check | It is imperative we verify the actual body and object types of an API response. This is a simple hard-coded/prettified/string body response verification. |

## Additional Improvements
1. Tests can start having certain pre-requisites. For example, if we see that the content-type of a response is going to be JSON, we call a particular prettify function that is used for JSON response. Then we can check the body object types that we expect, instead of the hard-coded string.
2. Test data can be fed to the API functions which would then expect a response based on the data fed. In this case for this API, we only used GET requests, meaning that no data was pushed to the database hosting this API itself.
3. Tests can first call the API to get relevant data, then use that data to do additional checks. Example, we could get a list of cat facts in nested objects, then go through those objects and get the ID of the first one, which will then be used to assert that object's data. This would avoid the need of hard-coded cat fact IDs.
