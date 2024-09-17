from typing import Optional
import re

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from pk_utils.general_utils import get_error_response
from pk_apis.movies_api import (get_people_cd
                                , get_actor_info
                                , get_daily_movie_chart
                                , get_movie_detail
                                , get_movie_search_list
                            )


def daily_view(request: HttpRequest) -> HttpResponse:
    data: Optional[str] = get_daily_movie_chart()

    if not data:
        return get_error_response(request, 'Failed to fetch API data or invalid JSON')

    daily_box_office_list: Optional[str] = data.get('boxOfficeResult', {})
    return render(request, 'box_office/index_view.html', {'box_office': daily_box_office_list})


def movie_detail(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return get_error_response(request, 'Invalid request method')

    movie_cd = request.POST.get('movieCd')
    if not movie_cd:
        return get_error_response(request, 'No movie code provided')

    data = get_movie_detail(movie_cd)

    if not data:
        return get_error_response(request, 'Failed to fetch API data or invalid JSON')

    movie_info = data.get('movieInfoResult', {}).get('movieInfo', {})

    # 영화 시리즈 검색
    movie_nm = movie_info["movieNm"]
    if ":" in movie_nm:
        movie_nm = movie_nm.split(":")[0]
    elif "-" in movie_nm:
        movie_nm = movie_nm.split("-")[0]
    elif re.search(r'\d', movie_nm):
        # 숫자를 제거하는 코드
        movie_nm = re.sub(r'\d', '', movie_nm)
    else:
        movie_nm = movie_nm.split(" ")[0]

    movie_series = get_movie_search_list(movie_nm)
    movie_series = movie_series.get('movieListResult', {}).get('movieList', {})

    return render(request, 'box_office/movie_detail.html', {'details': movie_info, "series": movie_series})


def actor_detail(request: HttpRequest) -> HttpResponse:
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


def search_list(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return get_error_response(request, 'Invalid request method')
    
    movie_name = request.POST.get('movieNm')
    if not movie_name:
        return get_error_response(request, 'No Movie name provided')
    
    data = get_movie_search_list(movie_name)

    if not data:
        return get_error_response(request, 'Failed to fetch API data or invalid JSON')
    
    movie_list = data.get('movieListResult', {}).get('movieList', {})
    return render(request, 'box_office/search_list.html', {'movies': movie_list})
