from django.db import models

# Create your models here.

class Board(models.Model):
    # TYPE_CHOICES = (('1', 'FreeBoard'), ('2', 'review'))
    id = models.AutoField(primary_key=True)
    type = models.IntegerField(null=False)
    author = models.IntegerField(null=False)
    title = models.CharField(max_length=300, null=False)
    content = models.CharField(max_length=1500, null=False)
    reg_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(null=True)

    class Meta:
        db_table = "Board"