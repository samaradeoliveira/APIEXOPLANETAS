from flask import Flask, jsonify, request
#importar as bibliotecas request e jsonify para enviar os dados para o navegador
from data import data
#importando o arquivo data de data.py

#configurando a API:
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200
# a instrução return significa que queremos enviar os dados no navegador para exibi-los
# 200 indica execução bem sucedida

if __name__ == "__main__":
    app.run()
