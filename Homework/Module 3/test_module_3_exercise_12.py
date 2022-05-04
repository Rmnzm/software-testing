import pytest
import requests


class TestUserAgent:
    exclude_params = [
        ("'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, "
         "like Gecko) Version/4.0 Mobile Safari/534.30'"), 
        ("'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 "
         "Mobile/15E148 Safari/604.1'"),
        "'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'",
        ("'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 "
         "Safari/537.36 Edg/91.0.100.0'"), 
        ("'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
         "Version/13.0.3 Mobile/15E148 Safari/604.1'") 
    ]

    @pytest.mark.parametrize('condition', exclude_params)
    def test_user_agent(self, condition):
        if condition == "'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 " \
                        "(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'":
            payload = condition

            response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                    headers={"User-Agent": payload})
            response_as_json = response.json()
            platform = response.json()["platform"]
            browser = response_as_json["browser"]
            device = response_as_json["device"]
            expected_agents = "'platform': 'Mobile', 'browser': 'No', 'device': 'Android'"
            actual_agents = f"'platform': '{platform}', 'browser': '{browser}', 'device': '{device}'"
            assert actual_agents == expected_agents, f"Your agent is not equal to condition: '{condition}'"

        elif condition == "'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) " \
                          "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'": 
            payload = condition

            response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                    headers={"User-Agent": payload})
            response_as_json = response.json()
            platform = response.json()["platform"]
            browser = response_as_json["browser"]
            device = response_as_json["device"]
            expected_agents = "'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'"
            actual_agents = f"'platform': '{platform}', 'browser': '{browser}', 'device': '{device}'"
            assert actual_agents == expected_agents, f"Your agent is not equal to condition: '{condition}'"

        elif condition == "'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'":
            payload = condition

            response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                    headers={"User-Agent": payload})
            response_as_json = response.json()
            platform = response.json()["platform"]
            browser = response_as_json["browser"]
            device = response_as_json["device"]
            expected_agents = "'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'"
            actual_agents = f"'platform': '{platform}', 'browser': '{browser}', 'device': '{device}'"
            assert actual_agents == expected_agents, f"Your agent is not equal to condition: '{condition}'"

        elif condition == "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                          "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'": 
            payload = condition

            response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                    headers={"User-Agent": payload})
            response_as_json = response.json()
            platform = response.json()["platform"]
            browser = response_as_json["browser"]
            device = response_as_json["device"]
            expected_agents = "'platform': 'Web', 'browser': 'Chrome', 'device': 'No'"
            actual_agents = f"'platform': '{platform}', 'browser': '{browser}', 'device': '{device}'"
            assert actual_agents == expected_agents, f"Your agent is not equal to condition: '{condition}'"

        elif condition == "'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, " \
                          "like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'": 
            payload = condition

            response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                    headers={"User-Agent": payload})
            response_as_json = response.json()
            platform = response.json()["platform"]
            browser = response_as_json["browser"]
            device = response_as_json["device"]
            expected_agents = "'platform': 'Mobile', 'browser': 'No', 'device': 'iOS'"
            actual_agents = f"'platform': '{platform}', 'browser': '{browser}', 'device': '{device}'"
            assert actual_agents == expected_agents, f"Your agent is not equal to condition: '{condition}'"