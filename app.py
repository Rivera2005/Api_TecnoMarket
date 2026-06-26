from flask import Flask, jsonify, request

app = Flask(__name__)

catalogo = {
    201: {"ID": 201, "Nombre": "Teclado mecanico RGB", "Precio": 45.00, "Stock": 12},
    202: {"ID": 202, "Nombre": "Mouse inalambrico", "Precio": 18.50, "Stock": 25},
    203: {"ID": 203, "Nombre": "Monitor LED 24", "Precio": 165.00, "Stock": 8}
}

@app.get("/")
def inicio():
    return jsonify(
        {
            "mensaje": "Bienvenido a la API de catalogo. By. HiGuys",
            "version": "1.0",
            "endpoints": ["/catalogo", "/catalogo/<id>"]
        }
    )
    
    
@app.get("/catalogo")
def obtener_productos():                                                                                                                                                                                                                                                                         
    return jsonify(list(catalogo.values()))

@app.get("/catalogo/<int:id>")
def obtener_cliente(id):
    
    producto = catalogo.get(id)
    
    if producto:
        return jsonify(producto) 
    
    return jsonify({"Error": "Producto no encontrado"}), 404


@app.post("/catalogo")
def agregar_productos():
    nuevo_producto = request.get_json()
    if not nuevo_producto or "producto" not in nuevo_producto:
        return jsonify({"Error": "El campo nombre es obligatorio"}), 400
    
    id_producto = max(catalogo.keys(), default=100) + 1
    if id_producto in catalogo:
        return jsonify({"Error": "Producto ya existe"}), 400
    
    nuevo_producto["id"] = id_producto
    catalogo[id_producto] = nuevo_producto
    return jsonify(nuevo_producto), 201


if __name__ == "__main__":
    app.run(debug=True)