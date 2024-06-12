from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock


## Views TEST - Start
class DailyViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('box_office.views.fetch_api_data')
    def test_daily_view_with_valid_data(self, mock_fetch_api_data):
        mock_data = {
            "boxOfficeResult": {
                "boxofficeType": "일별 박스오피스",
                "showRange": "20200404~20200404",
                "dailyBoxOfficeList": [
                    {
                        "rnum": "1",
                        "rank": "1",
                        "rankInten": "0",
                        "rankOldAndNew": "OLD",
                        "movieCd": "20205262",
                        "movieNm": "엽문4: 더 파이널",
                        "openDt": "2020-04-01",
                        "salesAmt": "75121500",
                        "salesShare": "20.0",
                        "audiCnt": "8288"
                    }
                ]
            }
        }
        mock_fetch_api_data.return_value = mock_data

        response = self.client.get(reverse('daily_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '엽문4: 더 파이널')
        self.assertTemplateUsed(response, 'index_view.html')

    @patch('box_office.views.fetch_api_data')
    def test_daily_view_with_invalid_data(self, mock_fetch_api_data):
        mock_fetch_api_data.return_value = None

        response = self.client.get(reverse('daily_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Failed to fetch API data or invalid JSON')
        self.assertTemplateUsed(response, 'index_view.html')


class MovieDetailViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('box_office.views.fetch_api_data')
    def test_movie_detail_with_valid_data(self, mock_fetch_api_data):
        mock_response = {
            "movieInfoResult": {
                "movieInfo": {
                    "movieCd": "20205262",
                    "movieNm": "엽문4: 더 파이널",
                    "showTm": "104",
                    "prdtYear": "2019",
                    "openDt": "20200401",
                    "typeNm": "장편",
                    "nations": [{"nationNm": "홍콩"}],
                    "genres": [{"genreNm": "액션"}],
                    "directors": [{"peopleNm": "엽위신"}],
                    "actors": [{"peopleNm": "견자단"}, {"peopleNm": "오건호"}]
                }
            }
        }
        mock_fetch_api_data.return_value = mock_response

        response = self.client.post(reverse('movie_detail'), {'movieCd': '20205262'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '엽문')
        self.assertTemplateUsed(response, 'movie_detail.html')

    @patch('box_office.views.fetch_api_data')
    def test_movie_detail_with_invalid_data(self, mock_fetch_api_data):
        mock_fetch_api_data.return_value = None

        response = self.client.post(reverse('movie_detail'), {'movieCd': '20205262'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Failed to fetch API data or invalid JSON')
        self.assertTemplateUsed(response, 'movie_detail.html')


class ActorDetailViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('box_office.views.fetch_api_data')
    def test_actor_detail_with_valid_data(self, mock_fetch_api_data):
        # 첫 번째 API 호출 모킹 값
        mock_actor_list_response = {
            "peopleListResult": {
                "peopleList": [
                    {
                        "peopleCd": "10000558",
                        "peopleNm": "배우1"
                    }
                ]
            }
        }

        # 두 번째 API 호출 모킹 값.
        mock_actor_info_response = {
            "peopleInfoResult": {
                "peopleInfo": {
                    "peopleCd": "10000558",
                    "peopleNm": "강동원",
                    "sex": "남",
                    "repRoleNm": "배우",
                    "filmos": [{"movieNm": "설계자"}, {"movieNm": "1987"}]
                }
            }
        }

        def side_effect(url):
            if "searchPeopleList" in url:
                return mock_actor_list_response
            elif "searchPeopleInfo" in url:
                return mock_actor_info_response
            return None

        mock_fetch_api_data.side_effect = side_effect

        # POST 요청을 시뮬레이션합니다.
        response = self.client.post(reverse('actor_detail'), {
            'peopleNmEn': 'GANG Dong-won',
            'peopleCd': '10000558'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '강동원')
        self.assertTemplateUsed(response, 'actor_detail.html')

    @patch('box_office.views.fetch_api_data')
    def test_actor_detail_with_invalid_data(self, mock_fetch_api_data):
        # 첫 번째 API 호출 모킹 값
        mock_actor_list_response = None

        # 두 번째 API 호출 모킹 값
        mock_actor_info_response = None

        # 두 번의 다른 URL 호출에 대해 서로 다른 값을 반환하도록 설정
        def side_effect(url):
            if "searchPeopleList" in url:
                return mock_actor_list_response
            elif "searchPeopleInfo" in url:
                return mock_actor_info_response
            return None

        mock_fetch_api_data.side_effect = side_effect

        # POST 요청을 시뮬레이션합니다.
        response = self.client.post(reverse('actor_detail'), {'peopleNmEn': 'GANG Dong-won'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Failed to fetch API data or invalid JSON')
        self.assertTemplateUsed(response, 'actor_detail.html')

## Views TEST - End
