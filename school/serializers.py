from rest_framework import serializers
from django.contrib.auth.models import User
from .models import studentsdetail,yearclass,months,teacherdetail,teachpaymonths,marks,subjects,schoolclasses,enroll_student,fees

class studentsdetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = studentsdetail
        #fields=['s_name',]
        fields = '__all__'

class yearsSerializer(serializers.ModelSerializer):

    class Meta:
        model = yearclass
        fields = '__all__'

class enrollSerializer(serializers.ModelSerializer):

    class Meta:
        model = enroll_student
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['year'] = yearsSerializer(instance.years).data
        rep['student'] = studentsdetailSerializer(instance.student).data
        rep['standard'] = standardSerializer(instance.standard).data
        return rep

class feesSerializer(serializers.ModelSerializer):

    class Meta:
        model = fees
        fields = '__all__'
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['enrollstudent'] = enrollSerializer(instance.enrollstudent).data
        rep['months'] = monthsSerializer(instance.months).data
        return rep

class monthsSerializer(serializers.ModelSerializer):

    class Meta:
        model = months
        fields = '__all__'

class teacherdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacherdetail
        fields = '__all__'

class t_paymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = teachpaymonths
        fields = '__all__'

class studentsresultSerializer(serializers.ModelSerializer):

    class Meta: 
        model = marks
        fields = '__all__'
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['enrollstudent'] = enrollSerializer(instance.enrollstudent).data
        rep['subjectname'] = subjectsSerializer(instance.subjectname).data
        return rep
    

class subjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = subjects
        fields = '__all__'

class standardSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolclasses
        fields = '__all__'
