from django.db import models
from django.contrib.auth import get_user_model
class UserClickCount(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    type = models.CharField(verbose_name=('Joke Type'), max_length=100, blank=True, null=True)
    joke = models.TextField(verbose_name=('Joke'), blank=True, null=True)

    count = models.IntegerField(verbose_name=('Joke Click Count'), blank=True, null=True)

    class Meta:
        db_table = 'userclickcount'

