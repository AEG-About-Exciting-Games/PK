from django.shortcuts import render
from datetime import datetime, timedelta
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def fetch_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, json.JSONDecodeError):
        return None


def get_error_response(request, message):
    return render(request, 'error.html', {'error': message})


def get_people_cd(people_nm):
    url = (f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?'
           f'key={API_KEY}&peopleNm={people_nm}')
    people = fetch_api_data(url)
    people_list = people.get('peopleListResult', {}).get('peopleList', [])
    if people_list:
        return people_list[0].get('peopleCd')
    return None


def get_actor_info(people_cd):
    url = (f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.json?'
           f'key={API_KEY}&peopleCd={people_cd}')
    return fetch_api_data(url)


def daily_view(request):
    date = (datetime.now().date() - timedelta(days=1)).strftime('%Y%m%d')
    url = (f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
           f'key={API_KEY}&targetDt={date}')
    data = fetch_api_data(url)

    if not data:
        return get_error_response(request, 'Failed to fetch API data or invalid JSON')

    daily_box_office_list = data.get('boxOfficeResult', {})
    return render(request, 'box_office/index_view.html', {'box_office': daily_box_office_list})


def movie_detail(request):
    if request.method != 'POST':
        return get_error_response(request, 'Invalid request method')

    movie_cd = request.POST.get('movieCd')
    if not movie_cd:
        return get_error_response(request, 'No movie code provided')

    url = (f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?'
           f'key={API_KEY}&movieCd={movie_cd}')
    data = fetch_api_data(url)

    if not data:
        return get_error_response(request, 'Failed to fetch API data or invalid JSON')

    movie_info = data.get('movieInfoResult', {}).get('movieInfo', {})
    return render(request, 'box_office/movie_detail.html', {'details': movie_info})


def actor_detail(request):
    if request.method != 'POST':
        return get_error_response(request, 'Invalid request method')

    people_nm_en = request.POST.get('peopleNmEn')
    if not people_nm_en:
        return get_error_response(request, 'No people name provided')

    people_cd = get_people_cd(people_nm_en)
    if not people_cd:
        return get_error_response(request, 'No people found')

    actor = get_actor_info(people_cd)
    if not actor:
        return get_error_response(request, 'Failed to fetch API data or invalid JSON')

    actor_info = actor.get('peopleInfoResult', {})
    return render(request, 'box_office/actor_detail.html', {'details': actor_info})


def search_list(request):
    if request.method != 'POST':
        return get_error_response(request, 'Invalid request method')
    
    movie_name = request.POST.get('movieNm')
    if not movie_name:
        return get_error_response(request, 'No Movie name provided')
    
    url = (f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?'
           f'key={API_KEY}&movieNm={movie_name}')
    data = fetch_api_data(url)

    if not data:
        return get_error_response(request, 'Failed to fetch API data or invalid JSON')
    
    movie_list = data.get('movieListResult', {}).get('movieList', {})
    return render(request, 'box_office/search_list.html', {'movies': movie_list})
