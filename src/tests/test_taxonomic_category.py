# tests/unit/test_taxonomic_category.py

import unittest
from fastapi.testclient import TestClient
from src.main import app

class TestTaxonomicCategory(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_taxonomic_category(self):
        response = self.client.post("/taxonomic_categories/", json={
            "kingdom": "Animalia",
            "phylum": "Chordata",
            "t_class": "Mammalia",
            "t_order": "Carnivora",
            "family": "Felidae",
            "genus": "Panthera",
            "specie_id": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

    def test_get_taxonomic_category(self):
        response = self.client.post("/taxonomic_categories/", json={
            "kingdom": "Plantae",
            "phylum": "Angiosperms",
            "t_class": "Eudicots",
            "t_order": "Rosales",
            "family": "Rosaceae",
            "genus": "Rosa",
            "specie_id": 1
        })
        category_id = response.json()["id"]
        response = self.client.get(f"/taxonomic_categories/{category_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["genus"], "Rosa")

    def test_update_taxonomic_category(self):
        response = self.client.post("/taxonomic_categories/", json={
            "kingdom": "Fungi",
            "phylum": "Ascomycota",
            "t_class": "Saccharomycetes",
            "t_order": "Saccharomycetales",
            "family": "Saccharomycetaceae",
            "genus": "Saccharomyces",
            "specie_id": 1
        })
        category_id = response.json()["id"]
        response = self.client.put(f"/taxonomic_categories/{category_id}", json={
            "kingdom": "Fungi",
            "phylum": "Ascomycota",
            "t_class": "Saccharomycetes",
            "t_order": "Saccharomycetales",
            "family": "Saccharomycetaceae",
            "genus": "Saccharomyces Updated"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["genus"], "Saccharomyces Updated")

    def test_delete_taxonomic_category(self):
        response = self.client.post("/taxonomic_categories/", json={
            "kingdom": "Animalia",
            "phylum": "Chordata",
            "t_class": "Aves",
            "t_order": "Passeriformes",
            "family": "Corvidae",
            "genus": "Corvus",
            "specie_id": 1
        })
        category_id = response.json()["id"]
        response = self.client.delete(f"/taxonomic_categories/{category_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["detail"], "Taxonomic Category deleted")

if __name__ == "__main__":
    unittest.main()
