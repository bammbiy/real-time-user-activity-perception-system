
from fastapi import APIRouter, UploadFile, File
import numpy as np
import cv2
from app.services.inference_service import InferenceService

router = APIRouter()
service = InferenceService()

@router.post("/infer")
async def infer(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    result = service.run(frame)
    return result
