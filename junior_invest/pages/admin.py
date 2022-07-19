from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from junior_invest.pages.models import Page


class PageAdminForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Page
        fields = '__all__'


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm


admin.site.register(Page, PageAdmin)