class AutoRefresh:
    def __init__(self, widget, callback, interval=30000):
        self.widget = widget
        self.callback = callback
        self.interval = interval

    def start(self):
        self.callback()
        self.widget.after(self.interval, self.start)
