# 📘 API Specification (Viral Marketing Backend)

> **프로젝트 개요:**  
> Django REST Framework 기반의 가계부 시스템 API 명세서  
> (회원, 계좌, 거래내역, 알림 관리 기능 포함)

---

## 🧩 ERD 개요

| 테이블 | 설명 | 주요 키 |
|--------|-------|----------|
| **User** | 사용자 정보 (회원가입, 로그인, 역할) | `user_id (PK)` |
| **Accounts** | 사용자의 계좌 정보 | `account_id (PK)` |
| **Transaction_History** | 거래 내역 기록 | `transaction_id (PK)` |
| **Notifications** | 사용자 알림 관리 | `id (PK)` |

---

## 👤 User API

### 1️⃣ 회원가입 (Sign Up)
**`POST /api/users/signup/`**

#### Request Body
```json
{
  "name": "가나다",
  "email": "test@example.com",
  "password": "test1234!",
  "nickname": "가나다",
  "role": "user"
}


{
  "id": 1,
  "email": "test@example.com",
  "nickname": "가나다",
  "role": "user",
  "created_at": "2025-10-14T12:00:00Z"
}
Status: 201 Created

2️⃣ 로그인 (Login)
POST /api/users/login/



{
  "email": "test@example.com",
  "password": "test1234!"
}


{
  "access": "<JWT Access Token>",
  "refresh": "<JWT Refresh Token>"
}
Status: 200 OK

3️⃣ 로그아웃 (Logout)
POST /api/users/logout/



{
  "refresh": "<JWT Refresh Token>"
}
Response
json

{
  "message": "Successfully logged out"
}
Status: 200 OK

4️⃣ 프로필 조회 (Get Profile)
GET /api/users/me/



{
  "id": 1,
  "name": "가나다",
  "email": "test@example.com",
  "nickname": "가나다",
  "role": "user",
  "last_login": "2025-10-13T09:00:00Z",
  "created_at": "2025-09-30T10:30:00Z"
}
Status: 200 OK

🏦 Account API
1️⃣ 계좌 생성 (Create Account)
POST /api/accounts/



{
  "bank_code": "004",
  "account_number": "123-456-7890",
  "account_type": "saving",
  "balance": 1000000
}


{
  "account_id": 1,
  "bank_code": "004",
  "account_number": "123-456-7890",
  "account_type": "saving",
  "balance": 1000000,
  "created_at": "2025-10-14T12:00:00Z"
}
Status: 201 Created

2️⃣ 계좌 목록 조회 (List Accounts)
GET /api/accounts/



[
  {
    "account_id": 1,
    "bank_code": "004",
    "account_number": "123-456-7890",
    "balance": 1000000
  },
  {
    "account_id": 2,
    "bank_code": "020",
    "account_number": "222-111-3333",
    "balance": 245000
  }
]
Status: 200 OK

3️⃣ 계좌 삭제 (Delete Account)
DELETE /api/accounts/{account_id}/


{
  "message": "Account deleted successfully"
}
Status: 204 No Content

💸 Transaction API
1️⃣ 거래 내역 생성 (Create Transaction)
POST /api/transactions/


{
  "account_id": 1,
  "payment_method": "card",
  "amount": 30000,
  "category": "식비",
  "date": "2025-10-14T09:30:00Z"
}

{
  "transaction_id": 10,
  "account_id": 1,
  "payment_method": "card",
  "amount": 30000,
  "category": "식비",
  "date": "2025-10-14T09:30:00Z"
}
Status: 201 Created

2️⃣ 거래 내역 조회 (List Transactions)
GET /api/transactions/?account_id=1


[
  {
    "transaction_id": 10,
    "account_id": 1,
    "category": "식비",
    "payment_method": "card",
    "date": "2025-10-14T09:30:00Z"
  }
]
Status: 200 OK

3️⃣ 거래 내역 수정 (Update Transaction)
PUT /api/transactions/{transaction_id}/


{
  "category": "교통비",
  "payment_method": "cash"
}

{
  "transaction_id": 10,
  "category": "교통비",
  "payment_method": "cash"
}
Status: 200 OK

4️⃣ 거래 내역 삭제 (Delete Transaction)
DELETE /api/transactions/{transaction_id}/


{
  "message": "Transaction deleted successfully"
}
Status: 204 No Content

🔔 Notification API
1️⃣ 알림 목록 조회 (List Notifications)
GET /api/notifications/


[
  {
    "id": 1,
    "type": "low_balance",
    "title": "잔액 부족 경고",
    "message": "계좌 잔액이 1만원 이하입니다.",
    "is_read": false,
    "created_at": "2025-10-14T10:00:00Z"
  }
]
Status: 200 OK

2️⃣ 알림 읽음 처리 (Mark as Read)
PATCH /api/notifications/{id}/read/


{
  "message": "Notification marked as read"
}
Status: 200 OK

⚙️ 관계 요약 (ERD 기준)
관계	설명
User (1) → Accounts (N)	한 명의 사용자는 여러 계좌를 가짐
Accounts (1) → Transaction_History (N)	계좌당 여러 거래 가능
User (1) → Transaction_History (N)	한 사용자는 여러 거래내역을 가짐
User (1) → Notifications (N)	한 사용자는 여러 알림을 가짐

📎 상태 코드 요약
코드	의미
200	요청 성공 (조회/수정)
201	데이터 생성 성공
204	삭제 성공 (내용 없음)
400	잘못된 요청
401	인증 실패
403	권한 없음
404	리소스 없음
500	서버 내부 오류

📚 참고
Framework: Django REST Framework

Auth: JWT (djangorestframework-simplejwt)

Schema: drf-spectacular (Swagger UI 지원)

DB: PostgreSQL