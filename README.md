プロジェクトの作成
==============================

## 事前条件
Djangoのインストール
```sh
$ pip install "Django>=1.9.0,<=1.9.9"
```

## プロジェクト作成
```sh
$ django-admin.py startproject --template=DJANGO_TEMPLATES_DIR/basic/ --extension=py,html PROJECT_NAME
```


ライブラリのインストール
==============================

## 開発環境
```sh
$ pip install --upgrade pip
$ pip install --upgrade setuptools
$ pip install -r requirements/dev.txt
```

## ステージング環境
```sh
$ pip install --upgrade pip
$ pip install --upgrade setuptools
$ pip install -r requirements/stg.txt
```

## 本番環境
```sh
$ pip install --upgrade pip
$ pip install --upgrade setuptools
$ pip install -r requirements/prd.txt
```


アプリケーションの作成
==============================
```sh
$ mkdir apps/APP_NAME
$ python manage.py startapp APP_NAME apps/APP_NAME/
```


プロジェクトごとの設定
==============================

- データベース
    - デフォルトでは以下の設定になっているので適宜修正してください。
        - 開発環境: SQLite
        - ステージング環境: 未設定
        - 本番環境: 未設定
- ユーザ
    - 簡単な独自ユーザモデルを用意しています。
    - 不要な場合は削除してください。
- ロギング


管理者ユーザの作成
==============================
```sh
$ python manage.py createsuperuser
```


テーブルの作成
==============================
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```


サーバの起動
==============================
```sh
$ python manage.py runserver
```
