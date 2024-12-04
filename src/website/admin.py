from django.contrib import admin

from .models import (
    About, Brands, Reviews, Awards, WorkExperience, Expertise, Services, FAQ, Projects, ContactMe
)


# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_no', 'email', 'experience', 'projects_completed', 'happy_clients', 'available')
    search_fields = ('name', 'email')


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating')
    search_fields = ('name', 'role')
    list_filter = ('rating',)


@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('year', 'position')
    search_fields = ('position',)
    list_filter = ('year',)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('organization', 'designation', 'start_year', 'end_year')
    search_fields = ('organization', 'designation')
    list_filter = ('start_year', 'end_year')


@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('skill_name',)
    search_fields = ('skill_name',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ContactMe)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('name', 'email', 'subject')