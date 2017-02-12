# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title
class Instance(models.Model):
    CloundPlatform = models.CharField(max_length=20) #云平台名称
    IpAddress = models.GenericIPAddressField()#主机IP地址
    Note = models.CharField(max_length=140)#主机备注
    CPUINumber = models.PositiveSmallIntegerField()#物理CPU个数 0-32767  cat /proc/cpuinfo |grep "physical id"|sort|uniq|wc -l
    CPUCoreNumber = models.PositiveSmallIntegerField()#CPU核数 0-32767 cat /proc/cpuinfo |grep "cores"|sort|uniq|wc -l
    CPUMhz = models.PositiveSmallIntegerField()#CPU频率 0-32767  cpu MHz: 2299.996   单位：MHz
    MemInfo = models.PositiveIntegerField() #内存大小 0-2147483647  单位：M
    DiskInfo = models.PositiveIntegerField()#硬盘信息
    Bandwidth = models.PositiveSmallIntegerField()#带宽
    Price = models.PositiveIntegerField()#价格
    TimeLeft = models.PositiveSmallIntegerField()#剩余天数
