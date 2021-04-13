from django.db import models

# 데이터베이스 상속
class PostModel(models.Model):

    title = models.TextField(default="")
    contents = models.TextField(default="")
    thumbnali = models.ImageField(default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "게시글 관리"

    # method
    def __str__(self):
        return self.title
