from rest_framework import serializers
from countries.models import Countries

class CountriesSerializer(serializers.ModelSerializer):
    """
    Class in charge of serialize all data from clients requests and process it

    :param serializers: super class serializers.ModelSerializer
    :type serializers: class
    """
    class Meta:
        """
        Subclass to map the clients requests
        """
        model = Countries
        fields = ('id', 'name', 'capital')