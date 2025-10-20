from rest_framework import serializers
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import get_user_model

User = get_user_model()

class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'name',
            'nickname',
            'role',
            'last_login',
            'created_at',
        ]
        read_only_fields = ('user_id', 'role', 'last_login', 'created_at')

class UserPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, trim_whitespace=False)
    new_password1 = serializers.CharField(write_only=True, trim_whitespace=False)
    new_password2 = serializers.CharField(write_only=True, trim_whitespace=False)

    def validate(self, attrs):
        if attrs['new_password1'] != attrs['new_password2']:
            raise serializers.ValidationError({'new_password2': '비밀번호가 일치하지 않습니다.'})
        if len(attrs['new_password1']) < 8:
            raise serializers.ValidationError({'new_password1': '8자 이상 입력해주세요'})
        return attrs

    def save(self, **kwargs):
        user: User = self.context['request'].user
        if not check_password(self.validated_data['old_password'], user.password):
            raise serializers.ValidationError({'old_password': '비밀번호가 올바르지 않습니다.'})
        user.password = make_password(self.validated_data['new_password1'])
        user.save(update_fields=['password'])
        return user

