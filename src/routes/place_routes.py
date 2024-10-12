from fastapi import APIRouter, HTTPException, Query
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
    places = place_controller.get_all_places()
    if places is None:
        raise HTTPException(status_code=404, detail="Places not found")
    return places

@router.get("/json/{place_id}", response_model=Place, summary="Get a place by ID in JSON format")
def read_place(place_id: int):
    place = place_controller.get_place(place_id)
    if place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return place

@router.get("/xml/{place_id}", summary="Get a place by ID in XML format")
def read_place_xml(place_id: int):
    place_xml = place_controller.get_place_xml(place_id)
    if place_xml is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return place_xml

@router.get("/pagination", summary="Get all places with pagination")
def read_all_places_with_pagination(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1)):
    places = place_controller.get_all_with_pagination(page, page_size)
    if places is None:
        raise HTTPException(status_code=404, detail="Places not found")
    return places

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
