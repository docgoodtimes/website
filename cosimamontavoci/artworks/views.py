from django.shortcuts import render, get_object_or_404
from .models import Artwork,ArtworkImage

# Create your views here.
def artwork_list(request):
    artworks=Artwork.published.all().order_by('-publish')
    random_photo=ArtworkImage.objects.filter(order=1).order_by('?').first()
    return render(request,'artworks/list.html', {'artworks': artworks,
                                                 'random_photo': random_photo})

def artwork_detail(request, artwork):
    artwork = get_object_or_404(Artwork, slug=artwork,
                                      status='published',
                                      )
    return render(request, 'artworks/detail.html', {'artwork': artwork,
                                                    'photo_gallery': ArtworkImage.objects.filter(name=artwork),
                                                    'all_artworks': Artwork.published.all()})