from rest_framework import serializers
from .models import (BulkClassifyResponse, Attendance,
                     Citizen, Routers, File,
                     Recipient, Channel, Skill, ChannelSkill, Service)


class BulkClassifyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkClassifyResponse
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kargs = {
            'token': {'write_only': True},
        }
        model = Attendance
        fields = "__all__"


class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class RoutersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routers
        fields = "__all__"


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = "__all__"


class SetSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = "__all__"


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ChannelSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelSkill
        fields = "__all__"


