import logging
from fastapi import FastAPI

from src.routes.home_router import router as home_router
from src.routes.place_routes import router as place_router
from src.routes.sighting_routes import router as sighting_router
from src.routes.specie_routes import router as species_router
from src.routes.taxonomic_category_routes import router as taxonomic_category_router

# config logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# Include the routers
app.include_router(home_router, prefix="/home", tags=["home"])
app.include_router(place_router, prefix="/places", tags=["places"])
app.include_router(sighting_router, prefix="/sightings", tags=["sightings"])
app.include_router(species_router, prefix="/species", tags=["species"])
app.include_router(taxonomic_category_router, prefix="/taxonomy-categories", tags=["taxonomy-categories"])

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
