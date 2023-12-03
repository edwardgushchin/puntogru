#! coding: utf-8

from django.contrib import admin
from puntogru_kernel.models import *

class PhotoInline(admin.TabularInline):
    model = PortfolioPhoto

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'interior',)
    inlines = [
        PhotoInline,
    ]

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'descript',)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('text', 'autor',)

@admin.register(HowWeWork)
class HowWeWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'descript',)

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('number', 'address', 'email', 'year_of_foundation', 'designers', 'contractors', 'active',)

    fieldsets = [
        ('Общая информация', {'fields': ['about_descript', 'year_of_foundation', 'designers', 'contractors']}),
        ('Контакты', {'fields': ['number', 'alt_number', 'address', 'email']}),
        ('Ссылки на социальные сети', {'fields': ['vk_url', 'instagram_url', 'twitter_url', 'fb_url']}),
        ('Техническая информация', {'fields': ['active']}),
    ]