import asyncio
import sys

if __name__ == "__main__":
    sys.path.append(".")

    from core.commands import func_registry

    asyncio.run(func_registry.execute_command(sys.argv))
