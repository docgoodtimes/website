from django.contrib import admin
from .models import Artwork, ArtworkImage
# Register your models here.

class ArtworkImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 0
    can_delete = True

    class Meta:
        ordering=('order',)

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    inlines = [ ArtworkImageInline, ]

admin.site.register(Artwork, ArtworkAdmin)

