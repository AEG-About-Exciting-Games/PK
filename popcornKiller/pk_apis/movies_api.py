from datetime import datetime, timedelta
from dotenv import load_dotenv
from typing import Optional, Dict
import os

from pk_utils.api_utils import fetch_api_data


load_dotenv()
API_KEY = os.getenv("MOVIE_API_KEY")


def get_people_cd(people_nm: str) -> Optional[str]:
    url = (f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?'
            f'key={API_KEY}&peopleNm={people_nm}')
    people = fetch_api_data(url)
    people_list = people.get('peopleListResult', {}).get('peopleList', [])
    if people_list:
        return people_list[0].get('peopleCd')
    return None


def get_actor_info(people_cd) -> Optional[Dict[str, str]]:
    url = (f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.json?'
            f'key={API_KEY}&peopleCd={people_cd}')
    return fetch_api_data(url)


def get_daily_movie_chart() -> Optional[Dict[str, str]]:
    date = (datetime.now().date() - timedelta(days=1)).strftime('%Y%m%d')
    url = (f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
            f'key={API_KEY}&targetDt={date}')
    return fetch_api_data(url)



def get_movie_detail(movie_cd) -> Optional[Dict[str, str]]:
    url = (f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?'
            f'key={API_KEY}&movieCd={movie_cd}')
    return fetch_api_data(url)


def get_movie_search_list(movie_name) -> Optional[str]:
    url = (f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?'
            f'key={API_KEY}&movieNm={movie_name}')
    return fetch_api_data(url)
