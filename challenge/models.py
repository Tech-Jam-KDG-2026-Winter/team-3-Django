
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Performance(models.Model):
    class Result(models.TextChoices):
        PERFECT = "PERFECT", "完遂"
        GOOD = "GOOD", "5割"
        FAILED = "FAILED", "失敗"
    class Level(models.TextChoices):
        STORONG = "STORONG", "強"
        MIDIUM = "MIDIUN", "中"
        SOFT = "SOFT", "弱"
        CUSTOM = "CUSTOM", "カスタム"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    result = models.CharField(
        max_length=10,
        choices=Result.choices,
        default=Result.FAILED,
    )
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    menu = models.CharField(max_length=20)
    time = models.DecimalField(
        max_digits=4,        # 全体の桁数（整数+小数）
        decimal_places=1     # 小数点以下1桁
    )
    level = models.CharField(
        max_length=10,
        choices=Level.choices,
        default=Level.MIDIUM,
    )

    def __str__(self):
        return self.menu + " : " + str(self.time) + "秒"
