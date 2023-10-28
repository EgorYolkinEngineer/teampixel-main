import sys

from core.commands import func_registry
from core.exceptions import AlreadyExistError
from core.service import generic_service
from src.users.models import User
from src.users.service import user_service
from tests.fixtures.db_data import FIXTURES


@func_registry(description="Load data in DB")
async def loaddata():
    loaded_models = await add_models()

    if loaded_models == len(FIXTURES.keys()):
        message = "All data successfully loaded.\n"
    elif loaded_models != 0:
        message = f"{loaded_models} models successfully loaded.\n"
    else:
        message = "No data loaded.\n"
    sys.stdout.write(message)


async def add_models() -> int:
    loaded_models = 0
    for model, values in FIXTURES.items():
        try:
            if model == User:
                await user_service.bulk_add(values)
            else:
                service = await generic_service(model)
                await service.bulk_add(values)
        except AlreadyExistError as e:
            sys.stdout.write(f"{e}\n")
            continue
        loaded_models += 1
    return loaded_models
