from fastapi.templating import Jinja2Templates


# TemplateResponse
templates = Jinja2Templates(directory="html")

# Static
STATIC_PATH = "/static"
STATIC_DIR = "static"

# Media
MEDIA_PATH = "/media"
MEDIA_DIR = "media"
