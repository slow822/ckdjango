from django.shortcuts import render, get_object_or_404
from .models import Watch


def watch_list(request):
    query = request.GET.get('q')
    if query:
        watches = Watch.objects.filter(name__icontains=query)
    else:
        watches = Watch.objects.all()
    return render(request, 'watch_list.html', {'watches': watches})

def watch_detail(request, pk):
    watch = get_object_or_404(Watch, pk=pk)
    return render(request, 'watch_detail.html', {'watch': watch})
