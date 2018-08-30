from django.db import models
from django.core.validators import FileExtensionValidator

class Uploader(models.Model):
    title = models.CharField(max_length=100)
    attach = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='添付ファイル',
        validators=[FileExtensionValidator(['pdf', ])],
    )
