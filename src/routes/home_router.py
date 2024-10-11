from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    home_message = {
        "author": "Ing. Cristian Camilo Charris Pérez",
        "description": """
            API para el registro de avistamientos de especies marinas en Colombia,
            desarrollada para el proyecto final de la asignatura diseño orientado a objetos y patrones
            de la especialización en desarrollo de software de la universidad del Magdalena.
        """,
        "university": "Universidad del Magdalena",
        "program": "Especialización en desarrollo de software",
        "teacher": "Ing. Miguel Polo",
        "year": "2024",
        "technology": [
            "Python",
            "FastAPI",
            "SQLite",
            "Swagger",
            "SQLModel",
            "Uvicorn",
            "Docker",
            "Git"
        ],
        "repository": "https://github.com/kristianschajris/sightings-marine-species",
        "version": "1.0.0",
        "endpoints": [
            "/places",
            "/species",
            "/taxonomic_categories",
            "/sightings"
        ]
    }

    return home_message