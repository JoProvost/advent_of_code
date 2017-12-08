def run(registers, reg, op, value, _, checked_reg, cond, checked_value):

    def inc(r, v):
        registers[r] += int(v)

    def dec(r, v):
        registers[r] -= int(v)

    operators = {
        '!=': lambda x, y: x != int(y),
        '==': lambda x, y: x == int(y),
        '>': lambda x, y: x > int(y),
        '<': lambda x, y: x < int(y),
        '>=': lambda x, y: x >= int(y),
        '<=': lambda x, y: x <= int(y),
        'inc': inc,
        'dec': dec,
    }

    if operators[cond](registers[checked_reg], checked_value):
        operators[op](reg, value)

    registers["highest"] = max(registers.values())