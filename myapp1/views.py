from django.shortcuts import render, get_object_or_404, redirect
from .models import Video
from .forms import VideoForm

def video_list(request):
    videos = Video.objects.all().order_by('MovieTitle')
    return render(request, 'myapp1/video_list.html', {'videos': videos})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'myapp1/video_detail.html', {'video': video})

def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = VideoForm()
    return render(request, 'myapp1/video_form.html', {'form': form, 'title': 'Add Video'})

def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            video = form.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = VideoForm(instance=video)
    return render(request, 'myapp1/video_form.html', {'form': form, 'title': 'Edit Video'})

def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('video_list')
    return render(request, 'myapp1/video_confirm_delete.html', {'video': video})
