from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id', 'title', 'user', 'text')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        about_django = 'django' in data['title'].lower()
        data['is_about_django'] = about_django
        return data


"""
Rapidly protyping and testing with Django Shell:

from notes.models import Notes
from notes.serializers import NotesSerializer
from rest_framework.renderer import JSONRenderer

serializer = NotesSerializer()
renderer = JSONRenderer()

note = Notes.objects.all()[0]
data = serializer.to_representation(note)
json_data = renderer.render(data)

"""
