from django.shortcuts import render
from django.http import HttpResponse

from dotenv import load_dotenv
from datetime import datetime, timedelta
import requests
import json
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")


def fetch_api_daily_data(date):
    url = ('http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
           f'?key={API_KEY}&targetDt={date}')

    response = requests.get(url)

    if response.status_code != 200:
        return None

    try:
        movies = response.json()
    except json.JSONDecodeError:
        return None

    return movies


def fetch_api_actor_data(people_nm):
    print(f"movie_cd = {people_nm}")
    url = ('http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json'
           f'?key={API_KEY}&peopleNm={people_nm}')

    response = requests.get(url)

    if response.status_code != 200:
        return None

    try:
        people = response.json()
    except json.JSONDecodeError:
        return None

    return people


def daily_view(request):
    date = datetime.now().date() - timedelta(days=1)
    date = str(date).replace("-", "")

    if date:
        data = fetch_api_daily_data(date)
        if data:
            daily_box_office_list = (data.get('boxOfficeResult', {}))
            return render(request, 'index_view.html', {'box_office': daily_box_office_list})
        else:
            return render(request, 'index_view.html', {'error': 'Failed to fetch API data or invalid JSON'})
    else:
        return render(request, 'index_view.html', {'error': 'No date provided'})


def movie_detail(request):
    if request.method == 'POST':
        movie_cd = request.POST.get('movieCd')
        print(f"movie_cd = {movie_cd}")
        url = ('http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
               f'?key={API_KEY}&movieCd={movie_cd}')

        response = requests.get(url)
        if response.status_code != 200:
            return None

        try:
            data = response.json()
        except json.JSONDecodeError:
            return None

        if data:
            movie_info = (data.get('movieInfoResult', {}).get('movieInfo', {}))
            return render(request, 'movie_detail.html', {'details': movie_info})
        else:
            return render(request, 'movie_detail.html', {'error': 'Failed to fetch API data or invalid JSON'})
    else:
        return render(request, 'movie_detail.html', {'error': 'No date provided'})


def actor_detail(request):
    if request.method == 'POST':
        people_nm = request.POST.get('peopleNmEn')

        if people_nm:
            people = fetch_api_actor_data(people_nm)

            people_cd = (people.get('peopleListResult').get('peopleList')[0].get('peopleCd'))

            url = ('http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.json'
                   f'?key={API_KEY}&peopleCd={people_cd}')

            response = requests.get(url)
            if response.status_code != 200:
                return None

            try:
                actor = response.json()
            except json.JSONDecodeError:
                return None

            if actor:
                actor_info = (actor.get('peopleInfoResult', {}))
                return render(request, 'actor_detail.html', {'details': actor_info})
            else:
                return render(request, 'actor_detail.html', {'error': 'Failed to fetch API data or invalid JSON'})
        else:
            return render(request, 'actor_detail.html', {'error': 'No date provided'})
