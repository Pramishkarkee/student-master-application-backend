from rest_framework import serializers

from apps.consultancy.models import Consultancy


class ConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultancy
        fields = '__all__'


class RegisterConsultancySerializer(ConsultancySerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta(ConsultancySerializer.Meta):
        fields = (
            'name',
            'email',
            'password',
            'contact',
            'country',
            'city',
            'state',
            'street_address',
            'latitude',
            'longitude',
            'website',
            'logo',
            'cover_image',
            'about',
        )
