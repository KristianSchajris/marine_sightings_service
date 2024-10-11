from fastapi import APIRouter, HTTPException
from src.controllers.taxonomic_category_controller import TaxonomicCategoryController
from src.models.taxonomic_category import TaxonomicCategory
from src.request.taxonomic_category_request import TaxonomicCategoryRequest

router = APIRouter()
taxonomic_category_controller = TaxonomicCategoryController()

@router.post("/", response_model=TaxonomicCategory, summary="Create a new taxonomic category")
def create_taxonomic_category(category_request: TaxonomicCategoryRequest):
    return taxonomic_category_controller.create_taxonomic_category(
        category_request.kingdom,
        category_request.phylum,
        category_request.t_class,
        category_request.t_order,
        category_request.family,
        category_request.genus,
        category_request.specie_id
    )

@router.get("/{category_id}", response_model=TaxonomicCategory, summary="Get a taxonomic category by ID")
def read_taxonomic_category(category_id: int):
    category = taxonomic_category_controller.get_taxonomic_category(category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Taxonomic Category not found")
    return category

@router.put("/{category_id}", response_model=TaxonomicCategory, summary="Update a taxonomic category by ID")
def update_taxonomic_category(category_id: int, category_request: TaxonomicCategoryRequest):
    category = taxonomic_category_controller.update_taxonomic_category(
        category_id,
        category_request.kingdom,
        category_request.phylum,
        category_request.t_class,
        category_request.t_order,
        category_request.family,
        category_request.genus
    )
    if category is None:
        raise HTTPException(status_code=404, detail="Taxonomic Category not found")
    return category

@router.delete("/{category_id}", summary="Delete a taxonomic category by ID")
def delete_taxonomic_category(category_id: int):
    success = taxonomic_category_controller.delete_taxonomic_category(category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Taxonomic Category not found")
    return {"detail": "Taxonomic Category deleted"}
