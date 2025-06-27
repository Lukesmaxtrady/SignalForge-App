class CustomSignalPlugin:
    def __init__(self, name, handler):
        self.name = name
        self.handler = handler  # handler: function(payload) -> dict

    def process(self, payload):
        return self.handler(payload)

    def status(self):
        return {"integration": self.name, "status": "custom/ready"}
