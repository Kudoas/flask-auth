# flask-jwt-extendを使った認証機能の実装

- frontendから受け取ったpasswordのハッシュ化
- login時にjwtを発行し、セッション管理
- ユーザーフォームのエラーハンドリング
- jwt tokenのバリデーションによるAPI endpointの保護

## library

- Flask
- Flask-JWT-extended
- hashlib

## enviroment

- python 3.8.5
- poetroy

## reference

- [Flask-JWT-Extended’s Documentation](https://flask-jwt-extended.readthedocs.io/en/stable/)
