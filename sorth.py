import sys
from enum import Enum, auto

class Instrs(Enum):
    Halt = auto()
    Push = auto()
    Pop = auto()
    Add = auto()
    Sub = auto()
    Print = auto()

type Args = None | int
type Program = list[tuple[Instrs, Args]]

def emulate(program: Program):
    stack = []
    cmp_flg = 0
    pc = 0 # Program Counter
    halt = False

    while pc < len(program) and not halt:
        instr = program[pc]
        pc += 1

        assert len(Instrs) == 6, "Exhaustive Reminder in `emulate`"
        match instr:
            case Instrs.Halt, _:
                halt = True
            case Instrs.Push, num:
                stack.append(num)
            case Instrs.Pop:
                stack.pop()
            case Instrs.Add, _:
                stack.append(stack.pop() + stack.pop())
            case Instrs.Sub, _:
                stack.append(stack.pop() - stack.pop())
            case Instrs.Print, _:
                print(stack[-1])

def parse_program_from_file(file_name: str) -> Program:
    program = []
    with open(file_name, "r") as file:
        assert len(Instrs) == 6, "Exhaustive Reminder in `parse_program_from_file`"

        for token in file.read().split():
            if token.isdigit():
                program.append((Instrs.Push, int(token)))
            else:
                match token:
                    case "del": program.append((Instrs.Pop, None))
                    case "+": program.append((Instrs.Add, None))
                    case "-": program.append((Instrs.Sub, None))
                    case ".": program.append((Instrs.Print, None))
                    case tk:
                        print("Invalid token:", tk)
                        exit(-1)

    return program

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <program>")
        sys.exit(-1)

    program = parse_program_from_file(sys.argv[1])
    emulate(program)

if __name__ == "__main__":
    main()
