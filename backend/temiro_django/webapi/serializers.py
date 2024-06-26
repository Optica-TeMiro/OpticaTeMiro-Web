from rest_framework import serializers

from .models import *


# ---- Serializadores referidos a la dirección postal

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('idprovincia', 'nombre')

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('iddepartamento', 'nombre', 'idprovincia')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('idciudad', 'nombre', 'iddedepartamento')


# ---- Serializadores referidos a los clientes

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('idusuario', 'tipousuario', 'usuario', 'password',
                  'email', 'aceptatc')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('idcliente', 'idusuario', 'apellido', 'nombre', 'dni', 'direccion', 'email',
                  'idciudad', 'telefono', 'celular', 'fechanac')


# ---- Serializadores referidos a los productos

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = ('idtipoproducto', 'descripcion')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('idproducto', 'descripcion', 'idtipoproducto', 'preciocosto',
                  'precio', 'fechaingreso', 'detalle', 'especificaciones', 'imagen')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('idproducto', 'cantidad')


# ---- Serializadores referidos a las ventas

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ('idvendedor', 'apellido', 'nombre', 'dni', 'telefono', 'celular', 'email')

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('idfactura', 'tipo', 'cuit', 'total', 'fechaapertura', 'fechacierre',
                  'direccionenvio', 'idciudad')

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ('idventa', 'idvendedor', 'idcliente', 'idfactura', 'fecha',
                  'descripcion', 'estado')

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ('iddetalleventa', 'idventa', 'idproducto', 'cantidad', 'descuento')


# ---- Serializadores referidos a servicios adicionales

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('iddoctor', 'apellido', 'nombre')

class AbonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abono
        fields = ('idabono', 'idfactura', 'descripcion', 'estado', 'valor', 'fecha')

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('idservicio', 'idfactura', 'descripcion', 'estado', 'valor', 'fecha')

