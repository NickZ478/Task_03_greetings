from django.db import models

class UserName(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя пользователя")
    created_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Имя пользователя"
        verbose_name_plural = "Имена пользователей"