import unittest
from server import app

class TestRPCServer(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_menu(self):
        response = self.client.post("/rpc", json={
            "jsonrpc": "2.0",
            "method": "getMenu",
            "id": 1
        })
        data = response.get_json()
        self.assertIn("result", data)
        self.assertEqual(data["result"]["pizza"], 80)

    def test_order(self):
        response = self.client.post("/rpc", json={
            "jsonrpc": "2.0",
            "method": "order",
            "params": {"items": ["pizza", "kola"]},
            "id": 2
        })
        data = response.get_json()
        self.assertIn("Sipariş alındı", data["result"])
        self.assertIn("100", data["result"])

    def test_wrong_method(self):
        response = self.client.post("/rpc", json={
            "jsonrpc": "2.0",
            "method": "notExist",
            "id": 3
        })
        data = response.get_json()
        self.assertIn("error", data)
        self.assertEqual(data["error"]["code"], -32601)

    # Ek test: boş sipariş
    def test_empty_order(self):
        response = self.client.post("/rpc", json={
            "jsonrpc": "2.0",
            "method": "order",
            "params": {"items": []},
            "id": 4
        })
        data = response.get_json()
        self.assertIn("error", data)
        self.assertEqual(data["error"]["message"], "Boş sipariş gönderilemez")

if __name__ == "__main__":
    unittest.main()

