from rest_framework import serializers
import PyPDF2
from .models import UploadedFile

  
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
        print(text)      
    return text

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'name', 'uploaded_at', 'text']
        read_only_fields = ['id', 'uploaded_at', 'text']  

    def create(self, validated_data):
        file_obj = UploadedFile.objects.create(**validated_data)
        text = extract_text_from_pdf(file_obj.file.path)  # Function to extract text
        file_obj.text = text
        file_obj.save()
        return file_obj
    
