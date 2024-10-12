from fastapi import APIRouter, HTTPException
from src.controllers.sighting_controller import SightingController
from src.models.sighting import Sighting
from src.request.sighting_request import SightingRequest
from src.utilities.pagination.paginated_collection import PaginatedCollection
router = APIRouter()
sighting_controller = SightingController()

@router.post("/", response_model=Sighting, summary="Create a new sighting")
def create_sighting(sighting_request: SightingRequest):
    return sighting_controller.create_sighting(
        sighting_request.latitude,
        sighting_request.longitude,
        sighting_request.image_sighting,
        sighting_request.notes,
        sighting_request.place_id,
        sighting_request.specie_id,
        sighting_request.user_id
    )

@router.get("/json/{sighting_id}", response_model=Sighting, summary="Get a sighting by ID")
def read_sighting(sighting_id: int):
    sighting = sighting_controller.get_sighting(sighting_id)
    if sighting is None:
        raise HTTPException(status_code=404, detail="Sighting not found")
    return sighting

@router.put("/{sighting_id}", response_model=Sighting, summary="Update a sighting by ID")
def update_sighting(sighting_id: int, sighting_request: SightingRequest):
    sighting = sighting_controller.update_sighting(
        sighting_id,
        sighting_request.latitude,
        sighting_request.longitude,
        sighting_request.image_sighting,
        sighting_request.notes
    )
    if sighting is None:
        raise HTTPException(status_code=404, detail="Sighting not found")
    return sighting

@router.delete("/{sighting_id}", summary="Delete a sighting by ID")
def delete_sighting(sighting_id: int):
    success = sighting_controller.delete_sighting(sighting_id)
    if not success:
        raise HTTPException(status_code=404, detail="Sighting not found")
    return {"detail": "Sighting deleted"}

@router.get("/xml/{sighting_id}", summary="Get a sighting by ID in XML format")
def read_sighting_xml(sighting_id: int):
    return sighting_controller.get_sighting_xml(sighting_id)

@router.get("/user/{user_id}", response_model=list[Sighting], summary="Get all sightings by user ID")
def get_sightings_by_user(user_id: int):
    return sighting_controller.get_sightings_by_user(user_id)

@router.get("/paginated", response_model=list[Sighting], summary="Get paginated sightings")
def get_paginated_sightings(page: int = 1, page_size: int = 10):
    paginated_result = sighting_controller.get_paginated_sightings(page, page_size)
    return paginated_result.items  # Asegúrate de devolver solo los elementos de la colección paginada
