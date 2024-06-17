# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Supplier,InventoryItem
# from .serializers import SupplierSerializer,InventoryItemSerializer

# # Supplier views

# @api_view(['GET'])
# def getSuppliers(request):
#   suppliers=Supplier.objects.all()
#   serializer= SupplierSerializer(suppliers)
#   return Response(serializer.data)

# @api_view(['GET'])
# def getSupplier(request,pk):
#   suppliers=Supplier.objects.get(id=pk)
#   serializer= SupplierSerializer(suppliers,many=False)
#   return Response(serializer.data)

# @api_view(['POST'])
# def createSupplier(request):
#   data=request.data
#   supplier=Supplier.objects.create(name=data['name'],contact_info=data['contact_info'])
#   serializer= SupplierSerializer(supplier,many=False)
#   return Response(serializer.data)

# @api_view(['PUT'])
# def updateSupplier(request,pk):
#   data=request.data
#   suppliers=Supplier.objects.get(id=pk)
#   serializer= SupplierSerializer(suppliers,many=False)
#   if serializer.is_valid():
#     serializer.save() 
#   return Response(serializer.data)
# @api_view(['DELETE'])
# def deleteSupplier(request,pk):
#   supplier= Supplier.objects.get(id=pk)
#   supplier.delete()
#   return Response('Supplier was deleted')

# # Inventory views

# @api_view(['GET'])
# def getInventories(request):
#   inventory=InventoryItem.objects.all()
#   serializer= InventoryItemSerializer(inventory)
#   return Response(serializer.data)

# @api_view(['GET'])
# def getInventory(request,pk):
#   inventory=InventoryItem.objects.get(id=pk)
#   serializer= InventoryItemSerializer(inventory,many=False)
#   return Response(serializer.data)

# @api_view(['POST'])
# def createInventory(request):
#   data=request.data
#   inventory=InventoryItem.objects.create(name=data['name'],description=data['description'],price=data['price'],suppliers=['suppliers'])
#   serializer= InventoryItemSerializer(inventory,many=False)
#   return Response(serializer.data)

# @api_view(['PUT'])
# def updateInventory(request,pk):
#   data=request.data
#   inventory=InventoryItem.objects.get(id=pk)
#   serializer= InventoryItemSerializer(inventory,many=False)
#   if serializer.is_valid():
#     serializer.save() 
#   return Response(serializer.data)
# @api_view(['DELETE'])
# def deleteInventory(request,pk):
#   inventory= InventoryItem.objects.get(id=pk)
#   inventory.delete()
#   return Response('Inventory was deleted')
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Supplier, InventoryItem
from .serializers import SupplierSerializer, InventoryItemSerializer

# Supplier views

@api_view(['GET'])
def getSuppliers(request):
    suppliers = Supplier.objects.all()
    serializer = SupplierSerializer(suppliers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSupplier(request, pk):
    supplier = Supplier.objects.get(id=pk)
    serializer = SupplierSerializer(supplier, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createSupplier(request):
    data = request.data
    supplier = Supplier.objects.create(name=data['name'], contact_info=data['contact_info'])
    serializer = SupplierSerializer(supplier, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def updateSupplier(request, pk):
    data = request.data
    supplier = Supplier.objects.get(id=pk)
    serializer = SupplierSerializer(supplier, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteSupplier(request, pk):
    supplier = Supplier.objects.get(id=pk)
    supplier.delete()
    return Response('Supplier was deleted', status=status.HTTP_204_NO_CONTENT)

# Inventory views

@api_view(['GET'])
def getInventories(request):
    inventory = InventoryItem.objects.all()
    serializer = InventoryItemSerializer(inventory, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getInventory(request, pk):
    inventory = InventoryItem.objects.get(id=pk)
    serializer = InventoryItemSerializer(inventory, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createInventory(request):
    data = request.data
    inventory = InventoryItem.objects.create(
        name=data['name'],
        description=data['description'],
        price=data['price']
    )
    for supplier_id in data.get('suppliers', []):
        supplier = Supplier.objects.get(id=supplier_id)
        inventory.suppliers.add(supplier)
    serializer = InventoryItemSerializer(inventory, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def updateInventory(request, pk):
    data = request.data
    inventory = InventoryItem.objects.get(id=pk)
    serializer = InventoryItemSerializer(inventory, data=data)
    if serializer.is_valid():
        serializer.save()
        inventory.suppliers.clear()
        for supplier_id in data.get('suppliers', []):
            supplier = Supplier.objects.get(id=supplier_id)
            inventory.suppliers.add(supplier)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteInventory(request, pk):
    inventory = InventoryItem.objects.get(id=pk)
    inventory.delete()
    return Response('Inventory was deleted', status=status.HTTP_204_NO_CONTENT)
