# 🛍️ Mini-Rozetka (Django + HTMX) — Luxe Theme  
Маркетплейс з **покупцями та продавцями**, де продавці можуть створювати магазини, публікувати товари, а покупці — переглядати, фільтрувати й купувати їх.  
Є **кошик і оформлення замовлення**, **відгуки та рейтинги**, а також **темний “люксовий” дизайн** (чорний + зелений + трохи синього).

Marketplace with **buyers and sellers**, where sellers can create shops, publish products, and buyers can browse, filter, and purchase them.  
Includes **cart & checkout**, **reviews & ratings**, and a **dark “luxury” design** (black + green + blue).

---

## 🚀 Features / Можливості

- **Accounts & Roles / Акаунти та ролі**  
  Buyers register to shop, sellers register to open and manage their shop.  
  Покупці реєструються для покупок, продавці — щоб відкрити і керувати магазином.  

- **Shops / Магазини**  
  Sellers customize banner, avatar, description, payment info.  
  Продавці налаштовують банер, аватар, опис, платіжну інформацію.  

- **Catalog / Каталог**  
  Categories, search, filters (price, category).  
  Категорії, пошук, фільтри (ціна, категорія).  

- **Cart & Checkout / Кошик і замовлення**  
  Add items dynamically with HTMX, place order.  
  Додавання товарів без перезавантаження (HTMX), оформлення замовлення.  

- **Reviews & Ratings / Відгуки та рейтинги**  
  One review per completed order.  
  Один відгук за виконане замовлення.  

- **Design / Дизайн**  
  Bootstrap 5 + custom `theme.css` → dark, premium UI.  
  Bootstrap 5 + власна тема `theme.css` → темний, “люксовий” вигляд.  

---

## ⚡ Quick Start / Швидкий старт

```bash
# Install dependencies / Встановлення залежностей
poetry install

# Apply database migrations / Міграції
poetry run python manage.py migrate

# Create superuser for /admin/ / Створення адміністратора
poetry run python manage.py createsuperuser

# Load demo data (categories, 12 products, demo shop) / Завантаження демо-даних
poetry run python manage.py loaddata catalog/fixtures/initial_data.json

# Run server / Запуск сервера
poetry run python manage.py runserver
➡️ Open / Відкрити: http://127.0.0.1:8000

🖼️ Product Images / Зображення товарів
Demo products include placeholders.

У демо-товарів спочатку стоять плейсхолдери.

Fetch real product photos from Unsplash/Pexels:
Отримати реальні фото товарів з Unsplash/Pexels:

bash
Копировать код
poetry run python manage.py fetch_product_images
Images saved to media/products/ and linked to products.

Фото збережуться у media/products/ та прив’яжуться до товарів.

See CREDITS.md for sources & licenses.
Див. CREDITS.md для джерел і ліцензій.

🛠️ Stack / Технології
Backend: Django 5 + HTMX

Filtering/Search: django-filter, django-render-block

Frontend: Bootstrap 5 + custom dark theme (static/css/theme.css)

Dev Tools: Poetry, ruff, isort, black (PEP8)

Database: SQLite by default (PostgreSQL ready)

🔑 Key URLs / Основні адреси
/ — Catalog / Каталог

/product/<slug>/ — Product detail / Товар

/cart/ — Shopping cart / Кошик

/orders/checkout/ — Checkout / Замовлення

/shops/me/ — Seller’s shop / Мій магазин

/admin/ — Django admin
