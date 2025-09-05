Mini-Rozetka (Django + HTMX) — Luxe Theme

Marketplace with buyers and sellers, where sellers can create shops, publish products, and buyers can browse, filter, and purchase them. Includes cart & checkout, reviews & ratings, and a dark “luxury” design (black + green + blue).

Features

Accounts & Roles: buyers register to shop, sellers register to open their shop and manage products.

Shops: seller can customize shop banner, avatar, description, and payment info.

Catalog: products grouped by categories, with text search and filters (price, category) for quick discovery.

Cart & Checkout: add items dynamically with HTMX (no full page reload), then place an order.

Reviews & Ratings: buyers can leave one review per completed order, building seller reputation.

Design: Bootstrap 5 + custom theme.css → modern dark UI, premium look and feel.

Quick Start

Steps to get the project running locally:

# Install dependencies with Poetry
poetry install

# Apply database migrations
poetry run python manage.py migrate

# Create an admin user for /admin/
poetry run python manage.py createsuperuser

# Load demo data: categories, 12 fishing products, demo shop
poetry run python manage.py loaddata catalog/fixtures/initial_data.json

# Start development server
poetry run python manage.py runserver


Open: http://127.0.0.1:8000

Product Images

By default, demo products come with placeholder images so everything works out of the box.

To get real product photos (Unsplash / Pexels, free license):

poetry run python manage.py fetch_product_images


This downloads images into media/products/ and links them to the 12 demo products.

See CREDITS.md for image sources and licenses.

Stack

Backend: Django 5 with HTMX for interactive UI without heavy JS.

Filtering/Search: django-filter and django-render-block for dynamic catalog updates.

Frontend: Bootstrap 5 + custom dark theme (static/css/theme.css) with green/blue accents.

Dev Tools: Poetry for dependency management, ruff/isort/black for PEP8 compliance.

Database: SQLite by default (PostgreSQL ready).

Key URLs

/ — Catalog with filters and search.

/product/<slug>/ — Product detail page.

/cart/ — Shopping cart (HTMX updates).

/orders/checkout/ — Checkout form.

/shops/me/ — Seller’s own shop (customize profile, view products).

/admin/ — Django admin panel.
Див. файл **CREDITS.md**. Реальні фото підтягнуться командою:
```bash
poetry run python manage.py fetch_product_images
```
