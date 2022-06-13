from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Popularmodel, Recommendedmodel, cartmodel, favmodel, usermodel


class PopularSerializer(ModelSerializer):
    class Meta:
        model = Popularmodel
        fields = '__all__'


class RecommendedSerializer(ModelSerializer):
    class Meta:
        model = Recommendedmodel
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model=usermodel
        fields='__all__'

class cartSerializer(ModelSerializer):
    class Meta:
        model=cartmodel
        fields='__all__'


class favSerializer(ModelSerializer):
    class Meta:
        model=favmodel
        fields='__all__'
       
