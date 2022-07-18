from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from junior_invest.pages.models import Page


class PageAdminForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
        fields = '__all__'


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm


admin.site.register(Page, PageAdmin)