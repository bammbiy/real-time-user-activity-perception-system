
from ai_core.pipeline.pipeline import ActivityPipeline

class InferenceService:
    def __init__(self):
        self.pipeline = ActivityPipeline()

    def run(self, frame):
        return self.pipeline.process_frame(frame)
