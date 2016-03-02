from django.contrib import admin
from .models import Glass, GlassImage
# Register your models here.

class GlassImageInline(admin.TabularInline):
    model = GlassImage
    extra = 0
    can_delete = True

    class Meta:
        ordering=('order',)

class GlassAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    inlines = [ GlassImageInline, ]

admin.site.register(Glass, GlassAdmin)

