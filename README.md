![Image](https://github.com/user-attachments/assets/df0bc6f5-b2a5-48ac-ae0e-5232ce7107f0)

# 가계부 시스템

5팀의 가계부 시스템은 🔐사용자 로그인, 회원가입, 게스트 접근🔑을 통해 가계부 기능을 사용할 수 있는 웹 서비스입니다. <br />
본 프로젝트는 Django + PostgreSQL 기반으로 개발되며, 팀 모두가 팀장이 되는 마음가짐으로 제작되었습니다.

---

## 🌟 주요 기능 🌟

- **회원 로그인**
  - ID / PW 확인
  - 로그인 실패 시 에러 메시지 반환
- **회원가입**
  - ID 중복 확인
  - PW 유효성 검사 (8자리 이상, 숫자 포함 등)
  - 닉네임 중복 확인
- **게스트 접속**
  - 별도의 회원가입 없이 조회는 가능
  - 단, 개인의 정보가 들어있는 만큼 상당히 제한된 기능만을 제공 ( 선택 사항 )
- **메인 화면**
  - 사이트 접속시 보여지는 첫 화면
  - 로그인 사용자 및 게스트 모두 접근 가능
  - 게스트는 제한된 기능만 사용 가능

---

## 📊 플로우차트 📈

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/18b33ff0-e6d0-426a-97fe-4d529d90e077" />

> 젊은이들의 감성을 대단히 자극하는 디자인으로 제작해보았다.

---

## 👩‍💻 기술 스택 👨‍💻

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Frontend**: Bootstrap
- **환경 관리**: Poetry + venv
- **협업 툴**: GitHub

---

## ⚙ 설치 및 실행 방법 🔧

### 1. 저장소 클론
```bash
git clone https://github.com/oz-viral-marketing-be-13-team6/viral-marketing.git
