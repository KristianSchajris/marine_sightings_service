from fastapi import APIRouter, HTTPException
from src.controllers.specie_controller import SpecieController
from src.models.specie import Specie
from src.request.specie_request import SpecieRequest

router = APIRouter()
specie_controller = SpecieController()

@router.post("/", response_model=Specie, summary="Create a new specie")
def create_specie(specie_request: SpecieRequest):
    return specie_controller.create_specie(specie_request.common_name, specie_request.scientific_name)

@router.get("/{specie_id}", response_model=Specie, summary="Get a specie by ID")
def read_specie(specie_id: int):
    specie = specie_controller.get_specie(specie_id)
    if specie is None:
        raise HTTPException(status_code=404, detail="Specie not found")
    return specie

@router.put("/{specie_id}", response_model=Specie, summary="Update a specie by ID")
def update_specie(specie_id: int, specie_request: SpecieRequest):
    specie = specie_controller.update_specie(specie_id, specie_request.common_name, specie_request.scientific_name)
    if specie is None:
        raise HTTPException(status_code=404, detail="Specie not found")
    return specie

@router.delete("/{specie_id}", summary="Delete a specie by ID")
def delete_specie(specie_id: int):
    success = specie_controller.delete_specie(specie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Specie not found")
    return {"detail": "Specie deleted"}
