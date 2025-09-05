# Mini-Rozetka (Django + HTMX) — Luxe Theme

Маркетплейс із ролями покупця/продавця, публікацією товарів, кошиком, замовленнями, рейтингами продавців, каталогом з фільтрами і пошуком. Дизайн — темний, «люксовий» (чорний + зелений + трохи синього).

## Швидкий старт
```bash
poetry install
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
poetry run python manage.py loaddata catalog/fixtures/initial_data.json
poetry run python manage.py runserver
```

## Запуск у PyCharm
1. Відкрити папку проекту **rozetka_mini** як проєкт.
2. Project Interpreter → додати **Poetry** env.
3. Run Configuration: `manage.py` + параметр `runserver` (Working directory — корінь проєкту).

## Імпорт реальних зображень
Можна автоматично скачати фото з Unsplash/Pexels для 12 товарів:
```bash
poetry run python manage.py fetch_product_images
```
Фото збережуться у `media/products/`, товари отримають повʼязані зображення.

## Стек
- Django 5, HTMX
- django-filter, django-render-block
- Bootstrap 5 + кастомна тема `static/css/theme.css`
- Poetry, PEP8 (black/ruff/isort)


## Зображення: джерела та ліцензії
Див. файл **CREDITS.md**. Реальні фото підтягнуться командою:
```bash
poetry run python manage.py fetch_product_images
```
