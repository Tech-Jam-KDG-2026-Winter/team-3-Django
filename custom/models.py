from django.db import models
from django.conf import settings

class WeekDay(models.Model):
    DAY_CHOICES = [
        (0, '月'),
        (1, '火'),
        (2, '水'),
        (3, '木'),
        (4, '金'),
        (5, '土'),
        (6, '日'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    day = models.IntegerField(choices=DAY_CHOICES)

class Level(models.TextChoices):
    NONE = "-", "-"
    WEAK = "weak", "弱"
    NORMAL = "normal", "中"
    STRONG = "strong", "強"

class SetMenu(models.Model):
    weekday = models.ForeignKey(
        WeekDay,
        on_delete=models.CASCADE,
        related_name='menus'
    )
    menu = models.CharField(max_length=200)
    level = models.CharField(
        max_length=20,
        choices=Level.choices,
        default=Level.NONE
    )
    starttime = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

