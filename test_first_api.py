import requests  # create request

class TestFirstApi: # test class
    def test_hello_call(self):  # test def
        url = "https://playground.learnqa.ru/api/hello"   #checking url
        name = "Roman"  # name
        data = {"name" : name}  # params or data

        response = requests.get(url, params=data)  # creating request and making response
        assert response.status_code == 200, "Wrong response code"  # checking the response code

        response_dict = response.json()  # converting response to json format
        assert "answer" in response_dict, "There is no field 'answer' in the response"  # checking the answer in response

        expected_response_text = f"Hello, {name}"  # making expected result to test
        actual_response_text = response_dict["answer"]  # making actual result to test
        assert actual_response_text == expected_response_text, "Actual text in the respnse is not correct"  # checking the response text results
