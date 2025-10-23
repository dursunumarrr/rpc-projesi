from flask import Flask, request, jsonify

app = Flask(__name__)


menu = {
    "pizza": 150,
    "hamburger": 200,
    "kola": 80
}

@app.route("/rpc", methods=["POST"])
def rpc():
    data = request.get_json()

    method = data.get("method")
    params = data.get("params", {})
    req_id = data.get("id")

    if method == "getMenu":
        response = {"jsonrpc": "2.0", "result": menu, "id": req_id}

    elif method == "order":
        items = params.get("items", [])
        total = sum(menu.get(i, 0) for i in items)
        response = {
            "jsonrpc": "2.0",
            "result": f"Sipariş alındı! Toplam tutar: {total} TL",
            "id": req_id
        }

    else:
        response = {
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": " bulunamadı"},
            "id": req_id
        }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
