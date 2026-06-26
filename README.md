- Desarrollo de una API REST con Flask 

Creación de API básica para la empresa TecnoMarket 

- Instalación
python -m venv .venv .venv\Scripts\Activate.ps1 python -m pip install -r requirements.txt

- Ejecutar servidor
python app.py

- Probar endpoints
GET http://127.0.0.1:5000/clientes GET http://127.0.0.1:5000/clientes/101 POST http://127.0.0.1:5000/clientes

- Consumir desde Python
python cliente.py