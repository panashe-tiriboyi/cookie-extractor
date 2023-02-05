from django.db import models

class Cookie(models.Model):
    cookie_name = models.CharField(max_length=30)
    cookie_id = models.CharField(max_length=30)
    cookie_value = models.CharField(max_length=30)
    cookie_expiry_date = models.CharField(max_length=30)
    cookie_domain = models.CharField(max_length=30)
   
    def __str__(self):
        return self.cookie_name

class CookieDbTest(models.Model):
    id_name = models.CharField(max_length=30)
    Platform = models.CharField(max_length=30)
    Category = models.CharField(max_length=30)
    Cookie_or_Data_Key_name_Domain_Description	= models.CharField(max_length=30)		
    Retention_period = models.CharField(max_length=30)
    Data_ControllerUser_Privacy_and_GDPR_Rights_Portals	= models.CharField(max_length=30)
    Wildcard_match = models.CharField(max_length=30)
    
    def __str__(self):
        return self.ID	

class ClientDomains(models.Model):
    username = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    domain= models.ForeignKey(Cookie, on_delete=models.CASCADE)

class Domain(models.Model):
   cookie_domain = models.CharField(max_length=30, unique=True, db_index=True)
   date_last_added = models.DateField(auto_now=True)
   def __str__(self) :
       return self.cookie_domain