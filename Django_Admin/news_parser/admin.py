from django.contrib import admin

from .models import Post, Urls, Polls


@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('url', 'post_id_id')


@admin.register(Polls)
class PollsAdmin(admin.ModelAdmin):
    list_display = ('question', 'post_id_id')


class PollsAdminInline(admin.StackedInline):
    model = Polls


class UrlsAdminInline(admin.StackedInline):
    model = Urls


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (PollsAdminInline, UrlsAdminInline,)

    list_display = ('tag', 'date', 'message', )

    list_filter = ('tag', 'date',)
