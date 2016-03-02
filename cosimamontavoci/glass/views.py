from django.shortcuts import render, get_object_or_404
from .models import Glass,GlassImage

# Create your views here.
def glass_list(request):
    glass_all=Glass.published.all()
    random_photo=GlassImage.objects.order_by('?').first()
    return render(request,'glass/list.html', {'glass_all': glass_all,
                                              'random_photo': random_photo})

def glass_detail(request, glass_item):
    glass_item = get_object_or_404(Glass, slug=glass_item,
                                      status='published',
                                      )
    return render(request, 'glass/detail.html', {'glass_item': glass_item,
                                                    'glass_photos': GlassImage.objects.filter(name=glass_item),
                                                    'all_glass': Glass.published.all()})