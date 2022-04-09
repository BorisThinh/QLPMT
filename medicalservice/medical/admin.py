from django.contrib import admin
from django.utils.html import mark_safe
from .models import Thuoc, DonThuoc, HoaDon, User, DanhMucThuocUong
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path

class DonThuocForm(forms.ModelForm):
    trieuChungBenh = forms.CharField(widget=CKEditorUploadingWidget)
    ketLuan = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        models = Thuoc
        fields = '__all__'


class DonThuocAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('/static/css/donthuoc.css',)
        }
        form = DonThuocForm


class ThuocAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('/static/css/main.css',)
        }
    list_display = ["id","tenThuoc","giaTien","created_date","updated_date"]
    search_fields = ["tenThuoc","giaTien"]
    list_filter = ["tenThuoc"]
    readonly_fields = ["avatar"]

    def avatar(self,thuoc):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120px' />".format(img_url=thuoc.image.name,alt = thuoc.tenThuoc))


class DonThuocInline(admin.StackedInline):
    model = DonThuoc
    pk_name = 'hoadon'



class MedicalAppAdminSite(admin.AdminSite):
    site_header = 'HE THONG DANG KY KHAM CHUA BENH'

    def get_urls(self):
        return [
            path('medical-stats/', self.medical_stats)
        ] + super().get_urls()

    def medical_stats(self):
        return "THONG KE"


admin_site = MedicalAppAdminSite("My Medical")



#admin.site.register(Thuoc,ThuocAdmin)
#admin.site.register(DonThuoc)
#admin.site.register(User)
#admin.site.register(DanhMucThuocUong)
#admin.site.register(HoaDon)

admin_site.register(Thuoc,ThuocAdmin)
admin_site.register(DonThuoc)
admin_site.register(User)
admin_site.register(DanhMucThuocUong)
admin_site.register(HoaDon)


