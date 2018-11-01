from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE) # 다른 모델에 대한 링크를 의미한다.
    title = models.CharField(max_length=200) # 글자 수가 제한된 텍스트를 정의할떄 사용한다. 글제목같이 짧은 문자열 정보를 저장할때 사용.
    text = models.TextField() # 글자수에 제한이 없는 긴 텍스트를 정의 할때 사용한다. 본문
    created_date = models.DateTimeField(default=timezone.now) # 날짜와 시간을 의미
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
