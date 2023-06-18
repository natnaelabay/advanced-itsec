from django.core.files.storage import FileSystemStorage
import os
import uuid

class MyStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        # Generate a unique filename using a UUID
        filename = f"{uuid.uuid4().hex}{os.path.splitext(name)[1]}"
        return super().get_available_name(filename, max_length)