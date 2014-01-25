from django.contrib.auth.models import User, Group
from rest_framework import serializers

from betterweb_app.models import Tip

# django rest framework quickstart code 
class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ('url', 'name')
# end of quickstart code

class TipSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tip

