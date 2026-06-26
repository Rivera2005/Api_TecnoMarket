from flask import Flask, jsonify, request

app = Flask(__name__)

catalogo = {
    "201": {"ID": 201, "Nombre": "Teclado mecanico RGB", "Precio": 45.00, "Stock": 12},
    "202": {"ID": 202, "Nombre": "Mouse inalambrico", "Precio": 18.50, "Stock": 25},
    "203": {"ID": 203, "Nombre": "Monitor LED 24", "Precio": 165.00, "Stock": 8}
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

if __name__ == "__main__":
    app.run(debug=True)