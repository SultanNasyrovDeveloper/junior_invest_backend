from django.contrib import admin

from . import models


class ProjectImageInline(admin.TabularInline):
    model = models.ProjectImage


class ProjectMediaInline(admin.TabularInline):
    model = models.ProjectMedia


class ProjectVoteInline(admin.TabularInline):
    model = models.ProjectVote


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectImageInline,
        ProjectMediaInline,
        ProjectVoteInline
    ]


@admin.register(models.ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    pass
