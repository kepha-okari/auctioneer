from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Artifact, Comment, UserProfile, Bid


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


class BidAdmin(admin.ModelAdmin):
    list_display = (
        'artifact',
        'bid_price',
        'user'
        )
    list_filter = ('bid_price',)
    # search_fields = ('artifact',)
admin.site.register(Bid, BidAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'profile_pic',
        'date_joined',
        'phone_number',
        'user_type',
    )
    list_filter = ('date_joined',)
    search_fields = ('user',)
admin.site.register(UserProfile, UserProfileAdmin)
