from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/", methods = ["GET"])
def hello():
    return "webhook on"

@app.route("/enviar", methods = ["POST"])
def enviar():
    dados = request.json
    nome = dados.get("nome")
    idade = dados.get("idade")

    info = {"nome": nome, "idade":idade}


    return jsonify({
        "status" : 200,
        "response" : info
    })

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)
