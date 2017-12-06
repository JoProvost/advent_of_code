def one(_):
    return 1


def process_instruction_at(pointer, memory, incr=one):
    jump = memory[pointer]
    memory[pointer] += incr(jump)
    return pointer + jump


def run(pointer, memory, incr=one):
    while len(memory) > pointer >= 0:
        pointer = process_instruction_at(
            pointer=pointer,
            memory=memory,
            incr=incr)
        yield pointer


def steps(pointer, memory, incr=one):
    return sum(1 for _ in run(pointer=pointer, memory=memory, incr=incr))


def steps_v2(pointer, memory):
    return sum(1 for _ in run(pointer=pointer, memory=memory,
                              incr=lambda jump: -1 if jump >= 3 else 1))
