def process_instruction_at(pointer, memory, incr=lambda jump: 1):
    jump = memory[pointer]
    memory[pointer] += incr(jump)
    return pointer + jump


def run(pointer, memory):
    while len(memory) > pointer >= 0:
        pointer = process_instruction_at(pointer=pointer, memory=memory)
        yield pointer


def steps(pointer, memory):
    return sum(1 for _ in run(pointer=pointer, memory=memory))


def run_v2(pointer, memory):
    while len(memory) > pointer >= 0:
        pointer = process_instruction_at(
            pointer=pointer, memory=memory,
            incr=lambda jump: -1 if jump >= 3 else 1)
        yield pointer


def steps_v2(pointer, memory):
    return sum(1 for _ in run_v2(pointer=pointer, memory=memory))
