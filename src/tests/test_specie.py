# tests/unit/test_specie.py

import unittest
from fastapi.testclient import TestClient
from main import app

class TestSpecie(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_specie(self):
        response = self.client.post("/species/", json={
            "common_name": "Tiburón Blanco",
            "scientific_name": "Carcharodon carcharias"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

    def test_get_specie(self):
        response = self.client.post("/species/", json={
            "common_name": "Tiburón Martillo",
            "scientific_name": "Sphyrna"
        })
        specie_id = response.json()["id"]
        response = self.client.get(f"/species/{specie_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["common_name"], "Tiburón Martillo")

    def test_update_specie(self):
        response = self.client.post("/species/", json={
            "common_name": "Tiburón Tigre",
            "scientific_name": "Galeocerdo cuvier"
        })
        specie_id = response.json()["id"]
        response = self.client.put(f"/species/{specie_id}", json={
            "common_name": "Tiburón Tigre Actualizado",
            "scientific_name": "Galeocerdo cuvier"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["common_name"], "Tiburón Tigre Actualizado")

    def test_delete_specie(self):
        response = self.client.post("/species/", json={
            "common_name": "Tiburón de Punta Negra",
            "scientific_name": "Carcharhinus limbatus"
        })
        specie_id = response.json()["id"]
        response = self.client.delete(f"/species/{specie_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["detail"], "Specie deleted")

if __name__ == "__main__":
    unittest.main()
