from django.db import models

class Cookie(models.Model):
    cookie_name = models.CharField(max_length=30)
    cookie_id = models.CharField(max_length=30)
    cookie_value = models.CharField(max_length=30)
    cookie_expiry_date = models.CharField(max_length=30)
    cookie_domain = models.CharField(max_length=30)
   
    def __str__(self):
        return self.cookie_name