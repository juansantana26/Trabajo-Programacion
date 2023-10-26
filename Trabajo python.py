'''
Nombre: Juan D Santana
C.I:32.178.985
_____Sistema de tienda online_____
'''
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    '''
La clase producto utiliza las variables: nombre, precio y cantidad para que
el usuario del codigo pueda darle valores al "Producto" que quiera crear.
'''

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad


class Inventario:
    def __init__(self):
        self.productos = []
    """
    La clase Inventario utiliza los productos creados en la clase "Producto"
    y las guarda posteriormente en una lista
    """

    def agregar_producto(self, producto):
        self.productos.append(producto)
    # La funcion "agregar productos" utiliza el .append para guardar en la lista los productos.

    def actualizar_cantidad(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.obtener_nombre() == nombre_producto:
                producto.establecer_cantidad(cantidad)
    #La funcion alctualizar_producto usa la funcion de la clase "Producto" "establecer_cantidad" para
    #para cambiar la cantidad de un producto seleccionado.
    def buscar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.obtener_nombre() == nombre_producto:
                print('Si hay',nombre_producto)
            else:
                print('No hay',nombre_producto)
    #buscar_productos utiliza un ciclo for para buscar en la lista de los productos y dar un mensaje 
    #por pantalla si el producto está o no en la lista.
    def generar_informe(self):
        informe = "Inventario:\n"
        for producto in self.productos:
            informe += f"Producto: {producto.obtener_nombre()}, Precio: {producto.obtener_precio()}, Cantidad: {producto.obtener_cantidad()}\n"
        print(informe)
    #generar_informe por cada producto en la lista, muestra cada uno, con su precio y cantidad.

class Cliente:
    def __init__(self, nombre, direccion, correo_electronico):
        self.nombre = nombre
        self.direccion = direccion
        self.correo_electronico = correo_electronico
        '''
        La clase Cliente guarda los valores de: nombre,
        direccion y correo electronico de cada uno de los clientes
        es sus respectivas variables.
        '''

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_direccion(self):
        return self.direccion

    def establecer_direccion(self, direccion):
        self.direccion = direccion

    def obtener_correo_electronico(self):
        return self.correo_electronico

    def establecer_correo_electronico(self, correo_electronico):
        self.correo_electronico = correo_electronico


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.total = 0.0
        '''
        La clase Pedido agrega productos previamente creados a una lista y
        utilizando una variable inicializada se le suman los precios de los 
        productos usando la variable "obtener_precio".
        '''

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.obtener_precio()
        print('Fue añadido', producto.nombre)

    def calcular_total(self):
        print("el total es",self.total)

    def generar_resumen(self):
        resumen = f"Pedido para {self.cliente.obtener_nombre()}:\n"
        for producto in self.productos:
            resumen += f"Producto: {producto.obtener_nombre()}, Precio: {producto.obtener_precio()}\n"
        resumen += f"Total: {self.calcular_total()}"
        return resumen


class Tienda:
    def __init__(self):
        self.inventario = Inventario()
        self.clientes = []
        '''
        la clase "Tienda" utiliza las clases creadas anteriormente con la finalidad de 
        de agruparlas en una misma clase y usarlas mejor.

        '''

    def agregar_producto(self, producto):
        self.inventario.agregar_producto(producto)
        print('Fue agregado', producto.nombre)
        

    def actualizar_cantidad(self, nombre_producto, cantidad):
        self.inventario.actualizar_cantidad(nombre_producto, cantidad)

    def buscar_producto(self, nombre_producto):
        print(self.inventario.buscar_producto(nombre_producto))

    def generar_informe_inventario(self):
        self.inventario.generar_informe()

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(cliente,"fue registrado como cliente")

    def buscar_cliente(self, nombre_cliente):
        for cliente in self.clientes:
            if cliente == nombre_cliente:
                print(cliente) 
            else:
                print('Cliente no registrado...')
if __name__ == '__main__':
    
    harina = Producto('Harina', 5, 50)    
    cliente1 = Cliente('Juan', 'mi casa', 'jd26@gmail.com')
    cliente1 = Tienda()
    cliente1.registrar_cliente('juan')
    cliente1.agregar_producto(harina)
    cliente1.generar_informe_inventario()
    cliente1 = Pedido('juan')
    cliente1.agregar_producto(harina)
    cliente1.calcular_total()
    
