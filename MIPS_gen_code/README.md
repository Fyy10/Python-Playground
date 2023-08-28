# MIPS machine code generator

Generate machine code from MIPS assembly.

## Rules

```python
op = inst[31:26]
func = inst[25:20]
shift = inst[19:15]
rd = inst[14:10]
rs = inst[9:5]
rt = inst[4:0]
imm = offset = inst[25:10]
addr = inst[25:0]
```

## Supported Instructions

```plain
add/and/or/xor rd rs rt
sll/srl rd rt shift
addi rt rs imm
andi/ori/xori rt rs imm
load rt offset rs
store rt offset rs
beq/bne rs rt offset
jump target
```

## Usage

```bash
python MIPS_gen_code.py
```

Type `exit` to quit the program.

### Example

```plain
$ python MIPS_gen_code.py 
add r5, r1, r2
0x00101422
addi r6, r1, 0x0003
0x14000c26
store r6, 0x0002(r5)
0x380008a6
load r7, 0x0001(r4)
0x34000487
sll r8, r7, 1
0x0830a007
beq r8, r3, 0x0002
0x3c000903
jump 0x00000001
0x48000001
exit
```
