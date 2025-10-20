from django.contrib import admin
from .models import Users

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    # 검색 기능 (이메일, 닉네임)
    search_fields = ('email', 'nickname')

    # 필터링 (is_staff, is_active)
    list_filter = ('is_staff', 'is_active')

    # 관리자 목록에 표시될 필드
    list_display = ('email', 'nickname', 'is_staff', 'is_active')

    # 어드민 여부를 읽기 전용으로
    readonly_fields = ('is_staff',)
