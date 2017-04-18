from rest_framework import serializers
from .models import Persona


class PersonaSerializer(serializers.Serializer):
    class Meta:
        model = Persona
        fields = ('id', 'name', 'release_date', 'rating', 'category')
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    release_date = serializers.DateField()
    rating = serializers.IntegerField()
    category = serializers.ChoiceField(choices=Persona.CATEGORIES_CHOICES)

    def create(self, validated_data):
        """
        Create and return a new `Persona` instance, given the validated data.
        """
        return Persona.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Persona` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
