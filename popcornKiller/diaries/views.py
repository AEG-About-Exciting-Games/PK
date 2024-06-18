from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Diary
from .forms import DiariesForm


@login_required
def diary_create(request):
    if request.method == "POST":
        form = DiariesForm(request.POST)

        if form.is_valid():
            diary = form.save(commit=False)
            diary.writer = request.user
            diary.save()
            return redirect('diaries:diary_detail', pk=diary.pk)
    else:
        form = DiariesForm()
    return render(request, 'diaries/diary_form.html', {'form': form})


@login_required
def diary_list(request):
    diaries = Diary.objects.filter(writer=request.user)
    return render(request, 'diaries/diary_list.html', {'form': diaries})


@login_required
def diary_detail(request, pk):
    diary = get_object_or_404(Diary, pk=pk, writer=request.user)
    return render(request, 'diaries/diary_detail.html', {'diary': diary})


@login_required
def diary_update(request, pk):
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
def diary_delete(request, pk):
    diary = get_object_or_404(Diary, pk=pk, writer=request.user)
    if request.method == "POST":
        diary.delete()
        return redirect('diaries:diary_list')
    return render(request, 'diaries/diary_confirm_delete.html', {'diary': diary})
