def redistribution(memory_state):
    blocks = max(memory_state)
    memory_bank = memory_state.index(blocks)

    new_state = list(memory_state)
    new_state[memory_bank] = 0

    for i in range(1, blocks + 1):
        new_state[(i + memory_bank) % len(new_state)] += 1

    return tuple(new_state)


def loop(memory_state):
    known_states = set()
    while memory_state not in known_states:
        known_states.add(memory_state)
        yield memory_state
        memory_state = redistribution(memory_state)
