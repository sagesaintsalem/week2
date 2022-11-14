class Engine:
    def __init__(self, volume):
        self.volume = volume

    def ignite(self):
        return "Engine started"

    def engine_failure(self):
        return 'Engine failing!'