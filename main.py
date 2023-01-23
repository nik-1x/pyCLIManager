import asyncio
from CLIManager import CommandManager, CommandRegisterManager


# You can use Classes for registering commands
async def test(args):
    # return - that will be printed
    return "test"



commands = CommandRegisterManager()
commands.register('test', test)

CommandManager(commands).run()
