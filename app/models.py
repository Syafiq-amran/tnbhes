from django.db import models

# Create your models here.

class tblLogs(models.Model):
    eventdatetime = models.DateTimeField(blank=True, null=False, verbose_name='Event Date Time')
    eventname = models.CharField(max_length = 50, blank=True, null=False, verbose_name='Status')
    description = models.CharField(max_length = 190, blank=True, null=False, verbose_name='Desc')
    transfduration = models.FloatField( verbose_name='Trasfer Duration')
    fromhost = models.CharField(max_length = 50, blank=True, null=False, verbose_name='From Host')
    tohost = models.CharField(max_length = 50, blank=True, null=False, verbose_name='To Host')
    comments = models.CharField(max_length = 190, blank=True, null=False, verbose_name='Comments')
    filepathname = models.CharField(max_length = 190, verbose_name='File Path Name')

    class Meta:
        managed = False
        db_table = 'tblLogs'

class tblFeederPillars(models.Model):
    id = models.AutoField(primary_key=True)
    sn = models.CharField(max_length=50 ,blank=True, null=True)
    name = models.CharField(max_length=50 ,blank=True, null=True)
    desc = models.CharField(max_length=50 ,blank=True, null=True)
    location = models.CharField(max_length=25 ,blank=True, null=True)
    coordinate = models.CharField(max_length=10 ,blank=True, null=True)
    longitude = models.CharField(max_length=50 ,blank=True, null=True)
    latitude = models.CharField(max_length=50 ,blank=True, null=True)
    capacity = models.FloatField(max_length=50 ,blank=True, null=True)
    incomingct = models.FloatField(max_length=50 ,blank=True, null=True)
    outgoingct = models.FloatField(max_length=50 ,blank=True, null=True)
    ipaddr = models.CharField(max_length=50 ,blank=True, null=True)
    macaddr = models.CharField(max_length=50 ,blank=True, null=True)
    comments = models.CharField(max_length=50 ,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblFeederPillars'

class tblfpsummary(models.Model):
    rowid = models.AutoField(primary_key=True)
    fpsn = models.CharField(max_length = 50)
    fpstatus = models.CharField(max_length = 50)
    fpipaddr = models.CharField(max_length = 50)
    fplocation = models.CharField(max_length = 50)
    fprating = models.CharField(max_length = 50)
    fpremarks = models.CharField(max_length = 50)
    
    class Meta:
        managed = False
        db_table = 'tblfpsummary'