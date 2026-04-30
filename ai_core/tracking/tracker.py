
def iou(a, b):
    x1 = max(a[0], b[0])
    y1 = max(a[1], b[1])
    x2 = min(a[2], b[2])
    y2 = min(a[3], b[3])

    inter = max(0, x2-x1) * max(0, y2-y1)
    area1 = (a[2]-a[0])*(a[3]-a[1])
    area2 = (b[2]-b[0])*(b[3]-b[1])

    return inter/(area1+area2-inter+1e-6)

class Tracker:
    def __init__(self):
        self.tracks = []
        self.next_id = 0

    def update(self, detections):
        updated = []

        for det in detections:
            matched = None
            for t in self.tracks:
                if iou(det["bbox"], t["bbox"]) > 0.3:
                    matched = t
                    break

            if matched:
                matched["bbox"] = det["bbox"]
                updated.append(matched)
            else:
                updated.append({"id": self.next_id, "bbox": det["bbox"]})
                self.next_id += 1

        self.tracks = updated
        return self.tracks
