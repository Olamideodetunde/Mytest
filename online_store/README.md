Online Store Inventory and Supplier Management API

This project is an API for managing inventory items and suppliers for an online store. It uses Django and Django Rest Framework (DRF) to provide endpoints for CRUD operations on inventory items and suppliers.

Table of Contents

1. Project Setup
2. Models
3. Serializers
4. Views
5. API Endpoints
6. Running Tests

Project Setup
    Clone the Repository
      git clone https://github.com/your-repository/online-store.git
      cd online-store
    Install Dependencies
      pip install -r requirements.txt
    Apply Migrations
      python manage.py makemigrations
      python manage.py migrate
    Run the Server
      python manage.py runserver
Models
    The application has two main models: 'Supplier' and 'InventoryItem'.
    inventory/models.py
    Supplier: Represents a supplier that provides inventory items.
    InventoryItem: Represents an item in the inventory.
Serializers
    Serializers are used to convert model instances to JSON and vice versa.
    inventory/serializers.py
Views
    The API views handle the CRUD operations for inventory items and suppliers.
    inventory/views.py
API Endpoints
    The API provides the following endpoints:
        Inventory Items
        GET /api/inventory/: List all inventory items
        GET /api/inventory/{id}: List single inventory item
        POST /api/inventory/create: Create a new inventory item
        PUT /api/inventory/{id}/update: Update a specific inventory item
        DELETE /api/inventory/{id}/delete: Delete a specific inventory item
        Suppliers
        GET /api/suppliers/: List all suppliers
        GET /api/suppliers/{id}: List single supplier
        POST /api/suppliers/create: Create a new supplier
        PUT /api/suppliers/{id}/update: Update a specific supplier
        DELETE /api/suppliers/{id}/delete: Delete a specific supplier
URL Configuration
    Add the URL patterns to online_store/urls.py
Running Tests
    Create a test file inventory/tests.py with basic tests


