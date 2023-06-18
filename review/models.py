import uuid
from django.db import models
from user.models import User

class Feedback(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    woreda = models.CharField(max_length=500)
    comments = models.TextField()
    pdf_file = models.FileField(upload_to='feedbacks/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.full_name

        # a@a.com
        # 123123qweqweasdasd