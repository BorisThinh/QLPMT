from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField



class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')

class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class DonThuoc(ModelBase):
    trieuChungBenh = RichTextField(max_length=255)
    ketLuan = RichTextField(max_length=255)
    ngayKham = models.DateTimeField(auto_now_add=True)
    bacsi = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    hoadon = models.ForeignKey('HoaDon', on_delete=models.CASCADE)
    danhmuc = models.ManyToManyField('DanhMucThuocUong')

class LichKham(ModelBase):
    ngayDangKy = models.DateTimeField()
    benhnhan = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)



class DanhMucThuocUong(ModelBase):
    tenDanhMuc = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tenDanhMuc


class Thuoc(ModelBase):
    tenThuoc =models.CharField(max_length=100, null=False, unique=True)
    giaTien = models.CharField(max_length=100, null=False)
    danhMucThuoc = models.ManyToManyField(DanhMucThuocUong)
    image = models.ImageField(upload_to='medicines/%Y/%m',default=None)

    def __str__(self):
        return self.tenThuoc



class HoaDon(ModelBase):
    chiPhiRaToa = models.IntegerField(blank=False)
    tienKham = models.IntegerField()
