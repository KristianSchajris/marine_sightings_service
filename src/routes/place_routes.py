from fastapi import APIRouter, HTTPException
from src.controllers.place_controller import PlaceController
from src.models.place import Place
from src.request.place_request import PlaceRequest

router = APIRouter()
place_controller = PlaceController()

@router.post("/", response_model=Place, summary="Create a new place")
def create_place(place_request: PlaceRequest):
    return place_controller.create_place(place_request.name_place, place_request.country, place_request.state)

@router.get("/", response_model=list[Place], summary="Get all places")
def read_all_places():
    return place_controller.get_all_places()

@router.get("/{place_id}", response_model=Place, summary="Get a place by ID")
def read_place(place_id: int):
    place = place_controller.get_place(place_id)
    if place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return place

@router.put("/{place_id}", response_model=Place, summary="Update a place by ID")
def update_place(place_id: int, place_request: PlaceRequest):
    place = place_controller.update_place(place_id, place_request.name_place, place_request.country, place_request.state)
    if place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return place

@router.delete("/{place_id}", summary="Delete a place by ID")
def delete_place(place_id: int):
    success = place_controller.delete_place(place_id)
    if not success:
        raise HTTPException(status_code=404, detail="Place not found")
    return {"detail": "Place deleted"}
