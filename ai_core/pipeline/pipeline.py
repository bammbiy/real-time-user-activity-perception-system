
from ai_core.detection.detector import Detector
from ai_core.tracking.tracker import Tracker
from ai_core.activity.classifier import ActivityClassifier

class ActivityPipeline:
    def __init__(self):
        self.detector = Detector()
        self.tracker = Tracker()
        self.classifier = ActivityClassifier()

    def process_frame(self, frame):
        detections = self.detector.detect(frame)
        tracks = self.tracker.update(detections)
        activity = self.classifier.predict(tracks)

        return {"activity": activity, "tracks": tracks}
