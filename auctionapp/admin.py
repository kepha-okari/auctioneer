from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from .models import Artifact, Comment

class ArtifactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'date_posted',
        'image',
        'is_sold',
    )
    list_filter = ('date_posted',)
    search_fields = ('name',)
admin.site.register(Artifact, ArtifactAdmin)


class CommentAdmin(admin.ModelAdmin):
	list_display = (
		'artifact',
		'date_posted',
		'comment'
	)
	list_filter = ('date_posted',)
	search_fields = ('artifact','comment')
admin.site.register(Comment, CommentAdmin)
