from django.db import models

# Create your models here.
class BookReview(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title