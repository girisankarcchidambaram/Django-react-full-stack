from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        # Here, {"password": {"write_only": True}} is used to make the password field write-only, meaning
        # it can be provided during object creation (e.g., user registration), but it won't be included in the 
        # serialized output when retrieving the user data. This is important for security, as you don't want to 
        #expose passwords in the API responses.

    def create(self, validated_data):
       
        user = User.objects.create_user(**validated_data)
                                    # The create_user method is a Django built-in method that properly handles password hashing and other related tasks. 
                                    # This is crucial because it ensures that the password is stored securely (hashed) in the database, rather than in plain text.
       
        return user
                  #This return value is typically used in views to respond with the created 
                              #user’s data (without the password, because of the extra_kwargs setting).

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=["id","title","content","created_at","author"]
        extra_kwargs={"author":{"read_only":True}}#readonly not give input automaticaly take
