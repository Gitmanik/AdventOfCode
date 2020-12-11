file = open('data.txt', 'r')
program = [line.rstrip('\n').split(' ') for line in file]
acc = 0
pc = 0

def _acc(arg):
    global acc
    global pc
    acc += int(arg)
    pc +=1

def _nop(arg):
    global pc
    pc +=1

done_jumps = set()

def _jmp(arg):
    global pc
    pc += int(arg)

op = {
    "acc": _acc,
    "nop": _nop,
    "jmp": _jmp
}

def run():
    global pc
    global acc
    pc = 0
    acc = 0
    done_pcs = set()
    while pc < len(program):
        # print(f'{pc} ({acc}): {line}')
        code = program[pc]
        op[code[0]](code[1])
        if pc in done_pcs:
            return False

        done_pcs.add(pc)

    return True

run()
print(f"Part 1: {acc}")


def swap(pc):
    if program[pc][0] == 'jmp':
        program[pc][0] = 'nop'
    else:
        program[pc][0] = 'jmp'

ctr = 0
for inner_pc in range(len(program)):

    if program[inner_pc][0] == 'acc':
        continue

    if program[inner_pc][1] == 0:
        continue
    swap(inner_pc)

    if run():
        print(f'Part 2: {acc}')
        break
    else:
        swap(inner_pc)

