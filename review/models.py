from django.db import models
from user.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    woreda = models.CharField(max_length=500)
    comments = models.TextField()
    pdf_file = models.FileField(upload_to='feedbacks/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name