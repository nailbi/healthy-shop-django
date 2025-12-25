# 🥗 Интернет-магазин здорового питания (Django)

Данный проект представляет собой веб-приложение — интернет-магазин товаров здорового образа жизни, разработанный с использованием фреймворка **Django**.  
Сайт поддерживает регистрацию и авторизацию пользователей, корзину, избранные товары, поиск, а также простую рекомендательную систему на основе истории покупок и рейтингов.

Проект может быть использован в учебных целях (курсовая/практическая работа).

---

## 🚀 Функциональные возможности

### 👤 Пользователи
- Регистрация аккаунта
- Вход и выход из аккаунта
- Хранение истории покупок

### 🛒 Товары
- Просмотр списка товаров
- Категории товаров
- Поиск товаров
- Просмотр описания и изображения товара
- Рейтинг товаров

### ❤️ Избранное
- Добавление товара в избранное
- Удаление товара из избранного
- Просмотр списка избранных товаров

### 🧺 Корзина
- Добавление товаров в корзину
- Удаление товаров из корзины
- Изменение количества товаров
- Оформление заказа

### 🤖 Рекомендательная система
- Персонализированные рекомендации
- Основаны на:
  - истории покупок
  - рейтингах товаров
  - популярных товарах в категории

---

## 🛠 Используемые технологии

- **Python 3**
- **Django**
- SQLite (база данных)
- HTML5
- CSS3
- Git / GitHub

---

## 📁 Структура проекта

healthy_shop/
│
├── healthy_shop/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── shop/
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── recommendations.py
│ ├── templates/
│ │ └── shop/
│ │ ├── products.html
│ │ ├── cart.html
│ │ ├── favorites.html
│ │ ├── login.html
│ │ └── register.html
│ └── static/
│ └── shop/
│ └── css/
│ └── style.css
│
├── manage.py
├── db.sqlite3
├── .gitignore
└── README.md


---

## ⚙️ Установка и запуск проекта

### 1️⃣ Клонировать репозиторий

```bash
git clone https://github.com/username/healthy-shop-django.git
cd healthy-shop-django

python -m venv venv

Windows
venv\Scripts\activate

MacOS/Linux
source venv/bin/activate

source venv/bin/activate

pip install django

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

python manage.py createsuperuser
