from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('box_office.views.fetch_api_data')
    def test_daily_view(self, mock_fetch_api_data):
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
                        "salesInten": "37421400",
                        "salesChange": "99.3",
                        "salesAcc": "199632200",
                        "audiCnt": "8288",
                        "audiInten": "4008",
                        "audiChange": "93.6",
                        "audiAcc": "23532",
                        "scrnCnt": "199",
                        "showCnt": "618"
                    },
                ]
            }
        }

        mock_fetch_api_data.return_value = mock_data

        response = self.client.get(reverse('box_office:daily_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '일별 박스오피스')
        self.assertTemplateUsed(response, 'index_view.html')

    @patch('box_office.views.fetch_api_data')
    def test_movie_detail(self, mock_fetch_api_data):
        mock_data = {
            "movieInfoResult": {
                "movieInfo": {
                    "movieCd": "20205262",
                    "movieNm": "엽문4: 더 파이널",
                    "movieNmEn": "Ip Man4: The Finale",
                    "movieNmOg": "",
                    "showTm": "104",
                    "prdtYear": "2019",
                    "openDt": "20200401",
                    "prdtStatNm": "개봉",
                    "typeNm": "장편",
                    "nations": [
                        {
                            "nationNm": "홍콩"
                        }
                    ],
                    "genres": [
                        {
                            "genreNm": "액션"
                        },
                        {
                            "genreNm": "드라마"
                        }
                    ],
                    "directors": [
                        {
                            "peopleNm": "엽위신",
                            "peopleNmEn": "Wilson Yip"
                        }
                    ],
                    "actors": [
                        {
                            "peopleNm": "견자단",
                            "peopleNmEn": "Donnie Yen",
                            "cast": "",
                            "castEn": ""
                        },
                    ],
                    "showTypes": [
                        {
                            "showTypeGroupNm": "2D",
                            "showTypeNm": "디지털"
                        }
                    ],
                    "companys": [
                        {
                            "companyCd": "20168728",
                            "companyNm": "(주)키다리이엔티",
                            "companyNmEn": "KIDARI ENT",
                            "companyPartNm": "배급사"
                        },
                        {
                            "companyCd": "20168728",
                            "companyNm": "(주)키다리이엔티",
                            "companyNmEn": "KIDARI ENT",
                            "companyPartNm": "수입사"
                        }
                    ],
                    "audits": [
                        {
                            "auditNo": "2020-MF00167",
                            "watchGradeNm": "12세이상관람가"
                        }
                    ],
                    "staffs": []
                },
                "source": "영화진흥위원회"
            }
        }
        mock_fetch_api_data.return_value = mock_data

        response = self.client.post(reverse('box_office:movie_detail'), {'movieCd': '20205262'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '엽문4: 더 파이널')
        self.assertTemplateUsed(response, 'movie_detail.html')

    @patch('box_office.views.fetch_api_data')
    def test_actor_detail(self, mock_fetch_api_data):
        mock_actor_list_response = {
            "peopleListResult": {
                "totCnt": 7,
                "peopleList": [
                    {
                        "peopleCd": "10000558",
                        "peopleNm": "강동원",
                        "peopleNmEn": "GANG Dong-won",
                        "repRoleNm": "배우",
                        "filmoNames": "설계자|천박사 퇴마 연구소: 설경의 비밀|브로커|반도|인랑|쓰나미 LA|골든슬럼버|1987|마스터|가려진 시간|검사외전|검은 사제들|두근두근 내 인생|군도: 민란의 시대|초능력자|의형제|전우치|엠|그놈 목소리|우리들의 행복한 시간|형사 Duelist|늑대의 유혹|그녀를 믿지 마세요|더 엑스|카멜리아"
                    },
                    {
                        "peopleCd": "20363775",
                        "peopleNm": "강동원",
                        "peopleNmEn": "",
                        "repRoleNm": "배우",
                        "filmoNames": "찬실이는 복도 많지"
                    },
                ],
                "source": "영화진흥위원회"
            }
        }

        mock_actor_info_response = {
            "peopleInfoResult": {
                "peopleInfo": {
                    "peopleCd": "10000558",
                    "peopleNm": "강동원",
                    "peopleNmEn": "GANG Dong-won",
                    "sex": "남자",
                    "repRoleNm": "배우",
                    "homepages": [],
                    "filmos": [
                        {
                            "movieCd": "20234045",
                            "movieNm": "설계자",
                            "moviePartNm": "배우"
                        },
                        {
                            "movieCd": "20227410",
                            "movieNm": "천박사 퇴마 연구소: 설경의 비밀",
                            "moviePartNm": "배우"
                        },
                        {
                            "movieCd": "20206257",
                            "movieNm": "브로커",
                            "moviePartNm": "배우"
                        },
                        {
                            "movieCd": "20193450",
                            "movieNm": "반도",
                            "moviePartNm": "배우"
                        },
                        {
                            "movieCd": "20170590",
                            "movieNm": "1987",
                            "moviePartNm": "배우"
                        },
                        {
                            "movieCd": "20161725",
                            "movieNm": "마스터",
                            "moviePartNm": "배우"
                        },
                    ]
                },
                "source": "영화진흥위원회"
            }
        }

        def side_effect(url):
            if "searchPeopleList" in url:
                return mock_actor_list_response
            elif "searchPeopleInfo" in url:
                return mock_actor_info_response
            return None

        mock_fetch_api_data.side_effect = side_effect

        response = self.client.post(reverse('box_office:actor_detail'), {
            'peopleNmEn': 'GANG Dong-won',
            'peopleCd': '10000558'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '강동원')
        self.assertTemplateUsed(response, 'actor_detail.html')

    # @patch('box_office.views.fetch_api_data')
    # def test_daily_view_with_invalid_data(self, mock_fetch_api_data):
    #     mock_fetch_api_data.return_value = None
    #
    #     response = self.client.get(reverse('box_office:daily_view'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Failed to fetch API data or invalid JSON')
    #     self.assertTemplateUsed(response, 'error.html')

    # @patch('box_office.views.fetch_api_data')
    # def test_movie_detail_with_invalid_code(self, mock_fetch_api_data):
    #     mock_fetch_api_data.return_value = None
    #
    #     response = self.client.post(reverse('box_office:movie_detail'), {'movieCd': ''})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'No movie code provided')
    #     self.assertTemplateUsed(response, 'error.html')

    # @patch('requests.get')
    # def test_movie_detail_with_invalid_data(self, mock_fetch_api_data):
    #     mock_fetch_api_data.return_value = None
    #
    #     response = self.client.post(reverse('box_office:movie_detail'), {'movieCd': '1'})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Failed to fetch API data or invalid JSON')
    #     self.assertTemplateUsed(response, 'error.html')
    #
    # @patch('box_office.views.fetch_api_data')
    # def test_actor_detail_with_invalid_name(self, mock_fetch_api_data):
    #     mock_fetch_api_data.return_value = None
    #
    #     response = self.client.post(reverse('box_office:actor_detail'), {'peopleNmEn': ''})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'No people name provided')
    #     self.assertTemplateUsed(response, 'error.html')
    #
    # @patch('box_office.views.fetch_api_data')
    # def test_actor_detail_with_invalid_code(self, mock_fetch_api_data):
    #     mock_fetch_api_data.return_value = {
    #         "peopleListResult": {
    #             "totCnt": 7,
    #             "peopleList": [
    #                 {
    #                     "peopleCd": "",
    #                     "peopleNm": "강동원",
    #                     "peopleNmEn": "GANG Dong-won",
    #                     "repRoleNm": "배우",
    #                     "filmoNames": "설계자|천박사 퇴마 연구소: 설경의 비밀|브로커|반도|인랑|쓰나미 LA|골든슬럼버|1987|마스터|가려진 시간|검사외전|검은 사제들|두근두근 내 인생|군도: 민란의 시대|초능력자|의형제|전우치|엠|그놈 목소리|우리들의 행복한 시간|형사 Duelist|늑대의 유혹|그녀를 믿지 마세요|더 엑스|카멜리아"
    #                 },
    #                 {
    #                     "peopleCd": "20363775",
    #                     "peopleNm": "강동원",
    #                     "peopleNmEn": "",
    #                     "repRoleNm": "배우",
    #                     "filmoNames": "찬실이는 복도 많지"
    #                 },
    #             ],
    #             "source": "영화진흥위원회"
    #         }
    #     }
    #
    #     response = self.client.post(reverse('box_office:actor_detail'),
    #                                 {
    #                                     'peopleNmEn': 'GANG Dong-won',
    #                                     'peopleCd': ''
    #                                 })
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'No people found')
    #     self.assertTemplateUsed(response, 'error.html')

