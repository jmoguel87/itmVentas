from django.conf import settings

class Config():

    def __init__(self) -> None:
        self.url = settings.AWS_URL_PATH
        self.connect_path = "/goControl"