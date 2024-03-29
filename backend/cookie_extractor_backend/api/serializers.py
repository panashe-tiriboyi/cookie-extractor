from dataclasses import field
from rest_framework import serializers
from .models import Cookie
from .models import ClientDomains
from .models import Domain


class DataBaseCookieSerializer(serializers.ModelSerializer):

    class Meta :
        model=Cookie
        fields = ["cookie_name","cookie_id","cookie_value","cookie_expiry_date","cookie_domain"]



class CookieSerializer(serializers.Serializer):
    cookie_name = serializers.CharField(max_length=200)
    cookie_id = serializers.CharField(max_length=200)
    cookie_value = serializers.CharField(max_length=200)
    cookie_expiration_date = serializers.CharField(max_length=200)
    cookie_domain = serializers.CharField(max_length=200)
    cookie_id = serializers.CharField(max_length=200)
    cookie_secure_flag =serializers.CharField(max_length=200)
    cookie_http_only_flag =serializers.CharField(max_length=200)

class ClientDomainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientDomains
        fields = ["username", "domain"]

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ["cookie_domain", " date_last_added"]
    


    