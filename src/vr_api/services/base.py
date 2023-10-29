class BaseVRService:
    headers = {"ngrok-skip-browser-warning": "69420"}

    def __init__(self, token: str | None = None):
        if token:
            self.headers.update({"Authorization": token})
