
import unittest
import json

from tdd_server import app 

class TestRestaurantAPI(unittest.TestCase):

    def setUp(self):
        """Her testten önce çalışacak hazırlık metodu."""
        self.app = app.test_client()
        self.app.testing = True

   
    def test_get_menu_success(self):
      
        menu_request = {
            "jsonrpc": "2.0",
            "method": "getMenu",
            "id": 1
        }
        
       
        response = self.app.post(
            '/rpc',
            data=json.dumps(menu_request),
            content_type='application/json'
        )
        
       
        data = json.loads(response.data.decode('utf-8'))
        
      
        self.assertEqual(response.status_code, 200)
        self.assertIn("result", data)
        self.assertNotIn("error", data)
        self.assertEqual(data["result"]["pizza"], 80) 

    
    def test_empty_order_failure(self):
       
        empty_order_request = {
            "jsonrpc": "2.0",
            "method": "order",
            "params": {"items": []}, 
            "id": 2
        }
        
        response = self.app.post(
            '/rpc',
            data=json.dumps(empty_order_request),
            content_type='application/json'
        )
        
        data = json.loads(response.data.decode('utf-8'))
        
      
        self.assertEqual(response.status_code, 200)
       
        self.assertIn("error", data) 
        self.assertNotIn("result", data)
        self.assertEqual(data["error"]["code"], -32602)


if __name__ == '__main__':
    unittest.main()