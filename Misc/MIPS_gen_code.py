# generate machine code from MIPS source code
# Rules:
# op = inst[31:26]
# func = inst[25:20]
# shift = inst[19:15]
# rd = inst[14:10]
# rs = inst[9:5]
# rt = inst[4:0]
# imm = offset = inst[25:10]
# addr = inst[25:0]

# supported instructions:
# add/and/or/xor rd rs rt
# sll/srl rd rt shift
# addi rt rs imm
# andi/ori/xori rt rs imm
# load rt offset rs
# store rt offset rs
# beq/bne rs rt offset
# jump target

# convert hex to bin of a certain length (with 0 extend)
def convert(data, length):
    data_bin = bin(int(data, 16))[2:]
    result = data_bin.rjust(length, '0')
    return result


R_type = ['add', 'and', 'or', 'xor', 'srl', 'sll']
I_type = ['addi', 'andi', 'ori', 'xori', 'load', 'store', 'beq', 'bne']
J_type = 'jump'
op_map = {
    'add': '000000',
    'and': '000001',
    'or': '000001',
    'xor': '000001',
    'srl': '000010',
    'sll': '000010',
    'addi': '000101',
    'andi': '001001',
    'ori': '001010',
    'xori': '001100',
    'load': '001101',
    'store': '001110',
    'beq': '001111',
    'bne': '010000',
    'jump': '010010'
}
func_map = {
    'add': '000001',
    'and': '000001',
    'or': '000010',
    'xor': '000100',
    'srl': '000010',
    'sll': '000011'
}


def gen_code(code: str):
    code = code.split()
    # print(code)
    op = op_map[code[0]]
    if code[0] in R_type:
        func = func_map[code[0]]
        if code[0] in ['srl', 'sll']:
            shift = convert(code[3], 5)
            rd = convert(code[1][1:], 5)
            rs = '00000'
            rt = convert(code[2][1:], 5)
        else:
            shift = '00000'
            rd = convert(code[1][1:], 5)
            rs = convert(code[2][1:], 5)
            rt = convert(code[3][1:], 5)
        machine_code = op + func + shift + rd + rs + rt
    elif code[0] in I_type:
        # addi
        if code[0][-1] == 'i':
            imm = convert(code[3], 16)
            rt = convert(code[1][1:], 5)
            rs = convert(code[2][1:], 5)
            machine_code = op + imm + rs + rt
        # beq, bne
        elif code[0][0] == 'b':
            offset = convert(code[3], 16)
            rs = convert(code[1][1:], 5)
            rt = convert(code[2][1:], 5)
            machine_code = op + offset + rs + rt
        # load, store
        else:
            offset = convert(code[2], 16)
            rt = convert(code[1][1:], 5)
            rs = convert(code[3][1:], 5)
            machine_code = op + offset + rs + rt
    elif code[0] == J_type:
        addr = convert(code[1], 26)
        machine_code = op + addr
    else:
        raise ValueError('Invalid Instruction')
    # print(machine_code)
    machine_code = hex(int(machine_code, 2))[2:]
    machine_code = machine_code.rjust(8, '0')
    return '0x' + machine_code


if __name__ == '__main__':
    while True:
        code = input()
        if code == 'exit':
            break
        print(gen_code(code))
