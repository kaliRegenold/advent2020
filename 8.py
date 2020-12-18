# Author: Kali Regenold
inst = []


def has_loop(print_acc=True):
    acc = 0             # Accumulater
    pc = 0              # Program Counter
    past_inst = [-1] * len(inst)    # List of previously visted program counters
    found_loop = False
    finished = False

    while(not finished and not found_loop):
        op = inst[pc][0]
        val = inst[pc][1]

        # acc
        if op == 'a':
            acc += val
            pc += 1
        # jump
        elif op == 'j':
            pc += val
        # nop
        elif op == 'n':
            pc += 1
        else:
            print('GOT 99 PROBLEMS AND THIS CODE IS 1')

        # If program counter passes length of instruction list, we're done
        if pc >= len(inst):
            finished = True
        # If the program counter reaches a spot where it's already been, it's a loop
        elif past_inst[pc] == 1:
            found_loop = True
        # Add the current program counter to the list of spots we've already been
        else:
            past_inst[pc] = 1

    if print_acc:
        print(acc)
    return found_loop, acc


def fun1(print_acc=True):
    has_loop()


def fun2():
    for i in range(0, len(inst)):
        # Switch nop to jmp and see if it finishes
        if(inst[i][0] == 'n'):
            inst[i][0] = 'j'
            found_loop, acc = has_loop(print_acc=False)
            # If we found a loop, switch back to nop
            if found_loop:
                inst[i][0] = 'n'
            else:
                print(acc)
                return
        # Switch jmp to nop and see if it finishes
        if(inst[i][0] == 'j'):
            inst[i][0] = 'n'
            found_loop, acc = has_loop(print_acc=False)
            # If we found a loop, switch back to jmp
            if found_loop:
                inst[i][0] = 'j'
            else:
                print(acc)
                return


# TODO: Clean this up
if __name__ == '__main__':
    # Read in the instructions, split on newline
    with open('8.in', 'r') as f:
        inst_list = f.readlines()
    inst_list = [x.strip() for x in inst_list]
    inst = [['',0]]*len(inst_list)
    for i in range(0, len(inst_list)):
        # Fill inst with 2 element arrays of the first letter of the instruction and the instruction value
        inst[i] = [inst_list[i].split(' ')[0][0], int(inst_list[i].split(' ')[1])]
    fun1()
    fun2()
