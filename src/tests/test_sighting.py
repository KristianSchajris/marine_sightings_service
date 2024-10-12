# tests/unit/test_sighting.py

import unittest
from fastapi.testclient import TestClient
from main import app

class TestSighting(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_sighting(self):
        response = self.client.post("/sightings/", json={
            "latitude": 36.6002,
            "longitude": -121.9030,
            "image_sighting": "https://example.com/image.jpg",
            "notes": "Avistamiento de tiburón blanco.",
            "place_id": 1,
            "specie_id": 1,
            "user_id": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

    def test_get_sighting(self):
        response = self.client.post("/sightings/", json={
            "latitude": 36.6002,
            "longitude": -121.9030,
            "image_sighting": "https://example.com/image.jpg",
            "notes": "Avistamiento de tiburón blanco.",
            "place_id": 1,
            "specie_id": 1,
            "user_id": 1
        })
        sighting_id = response.json()["id"]
        response = self.client.get(f"/sightings/{sighting_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["notes"], "Avistamiento de tiburón blanco.")

    def test_update_sighting(self):
        response = self.client.post("/sightings/", json={
            "latitude": 36.6002,
            "longitude": -121.9030,
            "image_sighting": "https://example.com/image.jpg",
            "notes": "Avistamiento de tiburón blanco.",
            "place_id": 1,
            "specie_id": 1,
            "user_id": 1
        })
        sighting_id = response.json()["id"]
        response = self.client.put(f"/sightings/{sighting_id}", json={
            "latitude": 36.6002,
            "longitude": -121.9030,
            "image_sighting": "https://example.com/image_updated.jpg",
            "notes": "Avistamiento de tiburón blanco actualizado."
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["notes"], "Avistamiento de tiburón blanco actualizado.")

    def test_delete_sighting(self):
        response = self.client.post("/sightings/", json={
            "latitude": 36.6002,
            "longitude": -121.9030,
            "image_sighting": "https://example.com/image.jpg",
            "notes": "Avistamiento de tiburón blanco.",
            "place_id": 1,
            "specie_id": 1,
            "user_id": 1
        })
        sighting_id = response.json()["id"]
        response = self.client.delete(f"/sightings/{sighting_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["detail"], "Sighting deleted")

if __name__ == "__main__":
    unittest.main()
