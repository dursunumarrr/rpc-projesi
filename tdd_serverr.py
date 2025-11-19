from flask import Flask, request, jsonify

app = Flask(__name__)

menu = {
    "pizza": 80,
    "hamburger": 60,
    "kola": 20
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

        if not items:
            response = {
                "jsonrpc": "2.0",
                "error": {"code": -32602, "message": "Boş sipariş gönderilemez"},
                "id": req_id
            }
        else:
            total = sum(menu.get(i, 0) for i in items)
            response = {
                "jsonrpc": "2.0",
                "result": f"Sipariş alındı! Toplam tutar: {total} TL",
                "id": req_id
            }

    else:
        response = {
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": "Yöntem bulunamadı"},
            "id": req_id
        }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
