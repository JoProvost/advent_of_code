from util import count


def one(_):
    return 1


def process_instruction_at(pointer, memory, inc=one):
    jump = memory[pointer]
    memory[pointer] += inc(jump)
    return pointer + jump


def run(pointer, memory, incr=one):
    while len(memory) > pointer >= 0:
        pointer = process_instruction_at(
            pointer=pointer,
            memory=memory,
            inc=incr)
        yield pointer


def steps(pointer, memory, incr=one):
    return count(run(pointer=pointer, memory=memory, incr=incr))


def steps_v2(pointer, memory):
    return count(run(pointer=pointer, memory=memory,
                     incr=lambda jump: -1 if jump >= 3 else 1))
