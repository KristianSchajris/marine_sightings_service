from fastapi import APIRouter, HTTPException
from src.controllers.sighting_controller import SightingController
from src.models.sighting import Sighting
from src.request.sighting_request import SightingRequest

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

@router.get("/{sighting_id}", response_model=Sighting, summary="Get a sighting by ID")
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
