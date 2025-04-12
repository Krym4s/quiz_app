# QuizApp: Платформа для создания и прохождения тестов

![Django](https://img.shields.io/badge/Django-3.2-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)

**QuizMaster** - это веб-приложение для создания образовательных тестов с поддержкой мультимедийного контента и аналитики результатов.

## 🌟 Основные возможности

- Поддержка различных аккаунтов:
  - Возможность создавать и редактировать различные профили
  - Возможность добавлять публичные и приватные тесты
- Создание тестов с различными типами вопросов:
  - Один правильный ответ
  - Текстовый ответ
  - Вопросы с изображениями в качестве вопросов
- Ограничение времени прохождения
- Система оценивания и аналитика

## 🚀 Быстрый старт

### Требования
- Python 3.8+
- Django 3.2

### Установка
```bash
git clone https://github.com/ваш-репозиторий/quizmaster.git
cd quizmaster
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver