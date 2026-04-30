
import torch

class Detector:
    def __init__(self):
        self.model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

    def detect(self, frame):
        results = self.model(frame)
        dets = []

        for *box, conf, cls in results.xyxy[0]:
            dets.append({
                "bbox": [float(x) for x in box],
                "conf": float(conf)
            })

        return dets
