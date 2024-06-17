from django.urls import path
from .views import getSuppliers,getSupplier,updateSupplier,deleteSupplier,createSupplier,getInventories,getInventory,createInventory,updateInventory,deleteInventory

urlpatterns = [
    path('suppliers/', getSuppliers,name='suppliers-list'),
    path('suppliers/create/', createSupplier,name='create-supplier'),
    path('supplier/<int:pk>', getSupplier,name='single-supplier'),
    path('supplier/<int:pk>/update', updateSupplier,name='update-supplier'),
    path('supplier/<int:pk>/delete', deleteSupplier,name='delete-supplier'),
    path('inventories/', getInventories,name='inventories-list'),
    path('inventory/create/', createInventory,name='create-inventory'),
    path('inventory/<int:pk>', getInventory,name='single-inventory'),
    path('inventory/<int:pk>/update', updateInventory,name='update-inventory'),
    path('inventory/<int:pk>/delete', deleteInventory,name='delete-inventory'),

]
