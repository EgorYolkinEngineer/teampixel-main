import importlib
import inspect
import os
import sys
from typing import Callable

from pydantic import BaseModel


class FunctionRegistry:
    def __init__(self):
        self.__registry: dict[str, FunctionInfo] = {}
        self.__allowed_kwargs: list[str] = ["description"]

    def __call__(self, func: Callable | None = None, **kwargs):
        if func:
            self.__registry[func.__name__] = FunctionInfo(
                function=func,
            )
            return func

        def wrapper(function: Callable):
            for kwarg in kwargs:
                assert (
                    kwarg in self.__allowed_kwargs
                ), f"Passed not supported keyword {kwarg} for function {function.__name__}"
            self.__registry[function.__name__] = FunctionInfo(function=function, **kwargs)
            return function

        return wrapper

    def update_registry(self):
        current_directory = os.path.dirname(__file__)

        for file in os.listdir(current_directory):
            if file.endswith(".py") and file != "__init__.py":
                module_name = file[:-3]
                importlib.import_module(f".{module_name}", package=__package__)

    async def execute_command(self, args: list[str]):
        if len(args) < 2:
            sys.stdout.write("Please pass command name.\n")
            return

        function_name = args[1]
        try:
            function_info = self.__registry[function_name]
        except KeyError:
            sys.stdout.write(f"Command {function_name} not exists.\n\n")
            return self.print_commands()

        registry_function = function_info.function

        if inspect.iscoroutinefunction(registry_function):
            return (
                await registry_function(*args[2:]) if len(args) > 2 else await registry_function()
            )
        else:
            return registry_function(*args[2:]) if len(args) > 2 else registry_function()

    def print_commands(self):
        output = "\033[94mList of available commands:\033[0m\n\n"
        for name, function_info in self.__registry.items():
            output += f"{name}"
            if function_info.description:
                output += f" - {function_info.description}"
            output += "\n"
        sys.stdout.write(output)


class FunctionInfo(BaseModel):
    function: Callable
    description: str = ""
