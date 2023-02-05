from django.db import models

class Compare(models.Model):
    id_name = models.CharField(max_length=30)
    Platform = models.CharField(max_length=30)
    Category = models.CharField(max_length=30)
    Cookie_or_Data_Key_name = models.CharField(max_length=30)
    Domain = models.CharField(max_length=30)
    Description	= models.CharField(max_length=30)		
    Retention_period = models.CharField(max_length=30)
    Data_Controller= models.CharField(max_length=30)
    User_Privacy_and_GDPR_Rights_Portals	= models.CharField(max_length=30)
    Wildcard_match = models.CharField(max_length=30)
    
    def __str__(self):
        return self.id_name	

class CookieDbTest(models.Model):
    id_name = models.CharField(max_length=30)
    Platform = models.CharField(max_length=30)
    Category = models.CharField(max_length=30)
    Cookie_or_Data_Key_name = models.CharField(max_length=30)
    Domain = models.CharField(max_length=30)
    Description	= models.CharField(max_length=30)		
    Retention_period = models.CharField(max_length=30)
    Data_Controller= models.CharField(max_length=30)
    User_Privacy_and_GDPR_Rights_Portals	= models.CharField(max_length=30)
    Wildcard_match = models.CharField(max_length=30)
    
    def __str__(self):
        return self.id_name	

class CookieDbTest1(models.Model):
    id_name = models.CharField(max_length=30)
    Platform = models.CharField(max_length=30)
    Category = models.CharField(max_length=30)
    Cookie_or_Data_Key_name = models.CharField(max_length=30)
    Domain = models.CharField(max_length=30)
    Description	= models.CharField(max_length=30)		
    Retention_period = models.CharField(max_length=30)
    Data_Controller= models.CharField(max_length=30)
    User_Privacy_and_GDPR_Rights_Portals	= models.CharField(max_length=30)
    Wildcard_match = models.CharField(max_length=30)
    
    def __str__(self):
        return self.id_name

class CookieDbTest2(models.Model):
    id_name = models.CharField(max_length=30)
    Platform = models.CharField(max_length=30)
    Category = models.CharField(max_length=30)
    Cookie_or_Data_Key_name = models.CharField(max_length=30)
    Domain = models.CharField(max_length=30)
    Description	= models.CharField(max_length=30)		
    Retention_period = models.CharField(max_length=30)
    Data_Controller= models.CharField(max_length=30)
    User_Privacy_and_GDPR_Rights_Portals	= models.CharField(max_length=30)
    Wildcard_match = models.CharField(max_length=30)
    
    def __str__(self):
        return self.id_name

class CookieDbTest3(models.Model):
    id_name = models.CharField(max_length=30)
    Platform = models.CharField(max_length=30)
    Category = models.CharField(max_length=30)
    Cookie_or_Data_Key_name = models.CharField(max_length=30)
    Domain = models.CharField(max_length=30)
    Description	= models.CharField(max_length=30)		
    Retention_period = models.CharField(max_length=30)
    Data_Controller= models.CharField(max_length=30)
    User_Privacy_and_GDPR_Rights_Portals	= models.CharField(max_length=30)
    Wildcard_match = models.CharField(max_length=30)
    
    def __str__(self):
        return self.id_name

class CookieDbTest4(models.Model):
    id_name = models.CharField(max_length=30)
    Platform = models.CharField(max_length=30)
    Category = models.CharField(max_length=30)
    Cookie_or_Data_Key_name = models.CharField(max_length=30)
    Domain = models.CharField(max_length=30)
    Description	= models.CharField(max_length=30)		
    Retention_period = models.CharField(max_length=30)
    Data_Controller= models.CharField(max_length=30)
    User_Privacy_and_GDPR_Rights_Portals	= models.CharField(max_length=30)
    Wildcard_match = models.CharField(max_length=30)
    
    def __str__(self):
        return self.id_name



