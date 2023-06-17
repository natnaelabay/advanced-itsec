from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from review.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'user', 'woreda', 'comments', 'pdf_file', 'created_at')
    list_display = ('id', 'user', 'woreda', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('user__email', 'woreda')
    list_editable = ("is_approved",)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('is_approved',)
        return self.readonly_fields

    def has_change_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            print("=========== has change permission =======")
            return True
        print("=========== NOPE change permission =====")
        return super().has_change_permission(request, obj)
    
    def has_add_permission(self, request):
        return False

admin.site.register(Feedback, FeedbackAdmin)