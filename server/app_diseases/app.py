from fastapi import APIRouter
from firebase_admin.exceptions import NotFoundError

from ..lib_firebase import fb_fstore
from ..lib_utils.response import Response
from .models import Disease

router = APIRouter(prefix="/diseases")
disease_collection = fb_fstore.collection("diseases")


@router.get("/{disease_slug}", tags=["Diseases"])
async def get_disease_detail(disease_slug: str) -> Response[Disease]:
    doc_ref = disease_collection.document(disease_slug)
    doc = await doc_ref.get()
    if not doc.exists:
        raise NotFoundError("disease not found")
    disease = doc.to_dict()
    print(disease)
    disease = Disease.model_validate(disease, strict=False)

    return Response(success=True, data=disease)


{
    "description": "Xanthomonas oryzae adalah bakteri patogen yang menyebabkan penyakit serius pada tanaman padi, dikenal dengan penyakit Hawar Daun Bakteri (HDB) atau Bacterial Leaf Blight (BLB).",
    "classification": {
        "disease_class": "Gammaproteobacteria",
        "kingdom": "Bacteria",
        "species": "Xanthomonas oryzae",
        "order": "Xanthomonadales",
        "phylum": "Proteobacteria",
        "family": "Xanthomonadaceae",
        "genus": "Xanthomonas",
    },
    "name": {
        "scientific": "Xanthomonas oryzae",
        "local": "Hawar Daun",
        "national": "Hawar Daun",
    },
}
