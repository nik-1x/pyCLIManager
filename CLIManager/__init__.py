import asyncio


class CommandRegisterManager:

    def __init__(self):
        self.commands = {}

    def register(self, command, func):
        self.commands[command.lower()] = func

    def get(self, command):
        if command not in self.commands:
            return None
        return self.commands[command]

    def get_all(self):
        return self.commands
    

class CommandManager:

    def __init__(self, cmd_register: CommandRegisterManager):
        self.commands = cmd_register

    async def main(self):
        while True:
            command = input('MultiSig DEVDAO ~ ')
            runner = command.split(' ')[0]
            args = command[(len(runner)+1):].split(" ")
            executor = self.commands.get(runner.lower())
            if executor is not None:
                print(await executor(args))

    def run(self):
        asyncio.run(self.main())
    