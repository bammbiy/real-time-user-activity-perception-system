
class ActivityClassifier:
    def predict(self, tracks):
        if len(tracks) == 0:
            return "IDLE"
        elif len(tracks) > 3:
            return "GAMING"
        return "READING"
