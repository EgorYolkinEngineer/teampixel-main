from fastapi import Request
from fastapi.responses import RedirectResponse, Response
from sqladmin import Admin

from core.config.templates import templates
from core.exceptions import NoRowsFoundError, ValidationError


class CustomAdmin(Admin):
    async def login(self, request: Request) -> Response:
        assert self.authentication_backend is not None

        context = {"request": request, "error": ""}

        if request.method == "GET":
            return templates.TemplateResponse("admin_login.html", context)

        try:
            tokens = await self.authentication_backend.login(request)
        except (ValidationError, NoRowsFoundError):
            context["error"] = "Invalid credentials."
            return templates.TemplateResponse("admin_login.html", context, status_code=400)
        response = RedirectResponse("/dashboard/admin", status_code=302)
        response.set_cookie("access_token", tokens.access_token)
        response.set_cookie("refresh_token", tokens.refresh_token)
        return response

    async def logout(self, request: Request) -> Response:
        response = RedirectResponse("/auth", status_code=302)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response


class CustomHR(Admin):
    async def login(self, request: Request) -> Response:
        assert self.authentication_backend is not None

        context = {"request": request, "error": ""}

        if request.method == "GET":
            return templates.TemplateResponse("admin_login.html", context)

        try:
            tokens = await self.authentication_backend.login(request)
        except (ValidationError, NoRowsFoundError):
            context["error"] = "Invalid credentials."
            return templates.TemplateResponse("admin_login.html", context, status_code=400)
        response = RedirectResponse("/dashboard/hr", status_code=302)
        response.set_cookie("access_token", tokens.access_token)
        response.set_cookie("refresh_token", tokens.refresh_token)
        return response

    async def logout(self, request: Request) -> Response:
        response = RedirectResponse("/auth", status_code=302)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response
