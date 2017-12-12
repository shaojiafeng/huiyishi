from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # 用户表
    username=models.CharField(max_length=16,null=True)
    password=models.CharField(max_length=64)
    def __str__(self):
        return self.username
class MettingRom(models.Model):
    # 会议室表
    caption=models.CharField(max_length=16)

    def __str__(self):
        return self.caption
class Meeting_scheduled(models.Model):
    # 会议预定表
    user=models.ForeignKey(to=UserInfo)
    metting=models.ForeignKey(to=MettingRom)
    date=models.DateField()
    time_choice=(
        (1,"8:00"),
        (2, "9:00"),
        (3, "10:00"),
        (4, "11:00"),
        (5, "12:00"),
        (6, "13:00"),
        (7, "14:00"),
        (8, "15:00"),
        (9, "16:00"),
        (10, "17:00")
    )
    time_quantum=models.IntegerField(choices=time_choice)
    class Meta:
        unique_together = (
            ('metting', 'date', 'time_quantum')
        )
