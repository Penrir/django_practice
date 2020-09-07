from django.db import models

# Create your models here.

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.IntegerField(null=False)
    user = models.IntegerField(null=False)
    score = models.IntegerField(null=False)
    content = models.CharField(max_length=600, null=False)
    reg_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Review"