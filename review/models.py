import uuid
from django.db import models
from user.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic

ext_validator = FileExtensionValidator(["pdf"])


def validate_fil_mimetype(file):
    accept = ["application/pdf", "pdf", ".pdf"]
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mime_type not in accept:
        raise ValidationError("Unsupported filetype")
    return file

class Feedback(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    woreda = models.CharField(max_length=500)
    comments = models.TextField()
    pdf_file = models.FileField(
        upload_to="feedbacks/",
        blank=True,
        null=True,
        validators=[ext_validator, validate_fil_mimetype],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.full_name
