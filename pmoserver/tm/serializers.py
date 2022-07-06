from rest_framework import routers,serializers,viewsets
from .models import Tm
class TmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tm
        fields = ['id','staff_name', 'tm_date', 'application', 'activity', 'duration','public_id','public_comment']