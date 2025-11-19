import unittest
from unittest.mock import patch
import client

class TestClient(unittest.TestCase):

    @patch("client.requests.post")
    def test_get_menu(self, mock_post):
        mock_post.return_value.json.return_value = {
            "result": {"pizza": 80, "kola": 20}
        }

        result = client.menu_response["result"]
        self.assertEqual(result["pizza"], 80)

    @patch("client.requests.post")
    def test_order(self, mock_post):
        mock_post.return_value.json.return_value = {
            "result": "Sipariş alındı! Toplam tutar: 100 TL"
        }

        result = client.order_response["result"]
        self.assertIn("100", result)

if __name__ == "__main__":
    unittest.main()
