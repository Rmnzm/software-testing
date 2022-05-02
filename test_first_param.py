import requests  # create request
import pytest  # enable pytest

class TestFirstApi: # test class
    names = [  # create typle names for 3 tests
        ("Roman"),
        ("Sasha"),
        ("")
    ]

    @pytest.mark.parametrize("name", names)  # creating test parametrized, enable names typle
    def test_hello_call(self, name):  # test def
        url = "https://playground.learnqa.ru/api/hello"   #checking url
        data = {"name" : name}  # params or data

        response = requests.get(url, params=data)  # creating request and making response
        assert response.status_code == 200, "Wrong response code"  # checking the response code

        if len(name) == 0:  # check to len param-name
            expected_response_text = "Hello, someone"  # expected result response when len name = 0
        else:
            expected_response_text = f"Hello, {name}"  # expected result response when len name != 0

        response_dict = response.json()  # converting response to json format
        assert "answer" in response_dict, "There is no field 'answer' in the response"  # checking the answer in response

        # expected_response_text = f"Hello, {name}"  # making expected result to test
        actual_response_text = response_dict["answer"]  # making actual result to test
        assert actual_response_text == expected_response_text, "Actual text in the respnse is not correct"  # checking the response text results
