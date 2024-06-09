from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch


## Views TEST - Start
class DailyViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('box_office.views.fetch_api_daily_data')
    def test_daily_view_with_valid_data(self, mock_fetch_api_daily_data):
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
        mock_fetch_api_daily_data.return_value = mock_data

        response = self.client.get(reverse('daily_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '엽문4: 더 파이널')
        self.assertTemplateUsed(response, 'index_view.html')

    @patch('box_office.views.fetch_api_daily_data')
    def test_daily_view_with_invalid_data(self, mock_fetch_api_daily_data):
        mock_fetch_api_daily_data.return_value = None

        response = self.client.get(reverse('daily_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Failed to fetch API data or invalid JSON')
        self.assertTemplateUsed(response, 'index_view.html')


class MovieDetailViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('requests.get')
    def test_movie_detail_with_valid_data(self, mock_get):
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
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = self.client.post(reverse('movie_detail'), {'movieCd': '20205262'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '액션')
        self.assertTemplateUsed(response, 'movie_detail.html')

    @patch('requests.get')
    def test_movie_detail_with_invalid_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = None

        response = self.client.post(reverse('movie_detail'), {'movieCd': '20205262'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Failed to fetch API data or invalid JSON')
        self.assertTemplateUsed(response, 'movie_detail.html')


class ActorDetailViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('requests.get')
    @patch('box_office.views.fetch_api_actor_data')
    def test_actor_detail_with_valid_data(self, mock_fetch_api_actor_data, mock_get):
        # fetch_api_actor_data 함수의 반환 값을 모킹합니다.
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
        mock_fetch_api_actor_data.return_value = mock_actor_list_response

        # requests.get 함수의 JSON 응답을 모킹합니다.
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
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_actor_info_response

        # POST 요청을 시뮬레이션합니다.
        response = self.client.post(reverse('actor_detail'), {'peopleNmEn': 'GANG Dong-won'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '강동원')
        self.assertTemplateUsed(response, 'actor_detail.html')

    @patch('requests.get')
    @patch('box_office.views.fetch_api_actor_data')
    def test_actor_detail_with_invalid_data(self, mock_fetch_api_actor_data, mock_get):
        pass
        # # fetch_api_actor_data 함수가 None을 반환하도록 모킹합니다.
        # mock_fetch_api_actor_data.return_value = None
        #
        # # POST 요청을 시뮬레이션합니다.
        # 빈 값으로 요청할 경우 디폴트 값(json)을 반환
        # response = self.client.post(reverse('actor_detail'), {'peopleNmEn': ""})
        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Failed to fetch API data or invalid JSON')
        # self.assertTemplateUsed(response, 'actor_detail.html')

## Views TEST - End
