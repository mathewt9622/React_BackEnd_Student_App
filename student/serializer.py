from rest_framework import serializers

from student.models import StudentModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields=(
            'name',
            'rollno',
            'admno',
            'college'
        )