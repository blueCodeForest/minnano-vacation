from django.db import models

from users.models import User


# class Genre(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name
    
class MinnanoVacation(models.Model):
    WITH_LIST = (
        ('0', 'ひとりで'),
        ('1', '恋人と'),
        ('2', '友達と'),
        ('3', '家族と'),
        ('4', '見知らぬ誰かと'),
    )

    TIME_REQUIRED_LIST = (
        ('0', '1時間以内'),
        ('1', '2~3時間'),
        ('2', '半日'),
        ('3', '1日'),
        ('4', '1泊以上'),
    )

    title = models.CharField('やりたいこと', max_length=200)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    with_who = models.CharField('誰と', max_length=30, choices=WITH_LIST)
    cost = models.IntegerField('およその金額')
    time_required = models.CharField('所要時間', max_length=30, choices=TIME_REQUIRED_LIST)
    published = models.BooleanField('公開', default=True)
    yaritai = models.IntegerField('やってみたい', default=0)
    copied = models.IntegerField('コピーされた数', default=0)
    original_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField('登録日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.title