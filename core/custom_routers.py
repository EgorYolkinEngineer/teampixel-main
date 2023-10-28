from fastapi import APIRouter


class TemplateRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.include_in_schema: bool = False
