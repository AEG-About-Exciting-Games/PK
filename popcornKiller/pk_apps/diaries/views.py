import os

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Diary
from .forms import DiariesForm
from pk_apis.movies_api import get_movie_detail
from pk_utils.general_utils import get_error_response


KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")


@login_required
def diary_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = DiariesForm(request.POST)

        if form.is_valid():
            diary = form.save(commit=False)
            diary.writer = request.user

            # 폼에서 받은 장소 정보를 모델에 저장
            diary.place_name = request.POST.get('place_name')
            loc_x = request.POST.get('place_x')
            loc_y = request.POST.get('place_y')

            # 소수점 4자리까지 자르기
            diary.loc_x = round(float(loc_x), 4) if loc_x else 33.4507
            diary.loc_y = round(float(loc_y), 4) if loc_y else 126.5706

            diary.save()
            return redirect('diaries:diary_detail', pk=diary.pk)

        movie_cd = request.POST.get('movieCd')
        if not movie_cd:
            return get_error_response(request, 'No movie code provided')

        data = get_movie_detail(movie_cd)

        if not data:
            return get_error_response(request, 'Failed to fetch API data or invalid JSON')

        movie_info = data.get('movieInfoResult', {}).get('movieInfo', {})
        # 영화 정보 중 영화 이름을 폼의 초기값으로 설정
        form = DiariesForm(initial={'movie': movie_info.get('movieNm')})

    else:
        form = DiariesForm()
    return render(request, 'diaries/diary_form.html', {'form': form, 'movieDetail': movie_info, "apiKey": KAKAO_API_KEY})


@login_required
def diary_list(request: HttpRequest) -> HttpResponse:
    diaries = Diary.objects.filter(writer=request.user)
    return render(request, 'diaries/diary_list.html', {'diaries': diaries})


@login_required
def diary_detail(request: HttpRequest, pk: int) -> HttpResponse:
    diary = get_object_or_404(Diary, pk=pk, writer=request.user)
    context = {
        'diary': diary,
        'apiKey': KAKAO_API_KEY
    }
    return render(request, 'diaries/diary_detail.html', context)


@login_required
def diary_update(request: HttpRequest, pk: int) -> HttpResponse:
    diary = get_object_or_404(Diary, pk=pk, writer=request.user)
    if request.method == "POST":
        form = DiariesForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
            return redirect('diaries:diary_detail', pk=diary.pk)
    else:
        form = DiariesForm(instance=diary)
    return render(request, 'diaries/diary_form.html', {'form': form})


@login_required
def diary_delete(request: HttpRequest, pk: int) -> HttpResponse:
    diary = get_object_or_404(Diary, pk=pk, writer=request.user)
    if request.method == "POST":
        diary.delete()
        return redirect('diaries:diary_list')
    return render(request, 'diaries/diary_confirm_delete.html', {'diary': diary})
