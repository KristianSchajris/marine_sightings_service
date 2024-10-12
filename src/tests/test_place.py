# tests//test_place.py

import unittest
from fastapi.testclient import TestClient
from main import app

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_place(self):
        response = self.client.post("/places/", json={
            "name_place": "Playa del Carmen",
            "country": "México",
            "state": "Quintana Roo"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

    def test_get_all_places(self):
        response = self.client.get("/places/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_place(self):
        response = self.client.post("/places/", json={
            "name_place": "Cancún",
            "country": "México",
            "state": "Quintana Roo"
        })
        place_id = response.json()["id"]
        response = self.client.get(f"/places/{place_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name_place"], "Cancún")

    def test_update_place(self):
        response = self.client.post("/places/", json={
            "name_place": "Tulum",
            "country": "México",
            "state": "Quintana Roo"
        })
        place_id = response.json()["id"]
        response = self.client.put(f"/places/{place_id}", json={
            "name_place": "Tulum Updated",
            "country": "México",
            "state": "Quintana Roo"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name_place"], "Tulum Updated")

    def test_delete_place(self):
        response = self.client.post("/places/", json={
            "name_place": "Cozumel",
            "country": "México",
            "state": "Quintana Roo"
        })
        place_id = response.json()["id"]
        response = self.client.delete(f"/places/{place_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["detail"], "Place deleted")

if __name__ == "__main__":
    unittest.main()
