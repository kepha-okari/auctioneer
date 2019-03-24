from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Artifact, Comment, UserProfile, Bid, Category, ContactInfo, Customer, Staff


class ArtifactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'date_posted',
        'image',
        'category',
        'is_sold',
    )
    list_filter = ('date_posted',)
    search_fields = ('name',)
admin.site.register(Artifact, ArtifactAdmin)


class CommentAdmin(admin.ModelAdmin):
	list_display = (
        'posted_by',
		'artifact',
		'date_posted',
		'comment'
	)
	list_filter = ('date_posted',)
	search_fields = ('artifact', 'comment')
admin.site.register(Comment, CommentAdmin)


class BidAdmin(admin.ModelAdmin):
    list_display = (
        'artifact',
        'bid_price',
        'bidder'
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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    list_filter = ('name',)
admin.site.register(Category, CategoryAdmin)

class CutomerAdmin(admin.ModelAdmin):
    list_display = (
        'purchase_history',
        'category',
        'name',
        'email',
        
    )
    list_filter = ('name',)
admin.site.register(Customer, CutomerAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'bio',
        'position',
        'name',
        'email'
    )
    list_filter = ('name',)
admin.site.register(Staff, StaffAdmin)
