from django.db import models
from django.forms import ValidationError

def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError("Only PDF files are allowed.")

class UploadedFile(models.Model):
    file = models.FileField(upload_to='pdfs/',validators=[validate_file_extension])
    name = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
