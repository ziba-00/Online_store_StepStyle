from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="news/images/", null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
        verbose_name = "News"





