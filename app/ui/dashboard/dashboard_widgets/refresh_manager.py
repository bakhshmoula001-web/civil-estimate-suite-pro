class DashboardRefreshManager:
    def __init__(self):
        self.callbacks = []

    def register(self, callback):
        self.callbacks.append(callback)

    def refresh(self):
        for callback in self.callbacks:
            callback()
