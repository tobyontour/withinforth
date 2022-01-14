from math import radians, cos, sin, asin, sqrt

def x() -> float:
    return 10.0

class Interpreter:

    def __init__(self):
        self.words = []
        self.stack = []
        self.commands = {
            '.': PopAndPrint()
        }

    def run(self, code: str) -> str:
        self.words + self.line_to_words(code)

        try:
            for word in self.words:
                if word in self.commands:
                    self.commands.execute(self.stack)
                else:
                    try:
                        self.stack.append(int(word))
                    except:
                        print("Got here")
        except CommandException as cmd:
            return cmd

        return "ok"

    def line_to_words(self, line: str) -> list:
        return line.split()

class Command:
    def execute(self, stack: list):
        return

class PopAndPrint(Command):
    def execute(self, stack: list):
        if len(stack) == 0:
            raise CommandException(':1: Stack underflow')
        return(stack.pop())

class CommandException(Exception):
    pass