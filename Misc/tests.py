# Unit Tests for MIPS_gen_code.py
# usage: python -m unittest tests

import unittest

from MIPS_gen_code import gen_code


class MipsGenCodeTest(unittest.TestCase):
    def compareMultipleCode(self, mips_code: str, binary_code: str):
        # test multiple codes
        mips_code_list = mips_code.strip().split('\n')
        binary_code_list = binary_code.strip().split('\n')
        self.assertEqual(len(mips_code_list), len(binary_code_list))
        for i in range(len(mips_code_list)):
            mips = mips_code_list[i].strip()
            binary = binary_code_list[i].strip()
            self.assertEqual(gen_code(mips), binary)

    def test1(self):
        mips_code = \
            """
            add     r1 r2 r3
            add     r4 r1 r2
            and     r6 r5 r1
            load    r1 0xfffe r7
            sll     r8 r1 1
            store   r8 0x5c r2
            beq     r1 r1 4
            addi    r1 r1 1
            addi    r3 r1 2
            """
        binary_code = \
            """
            0x00100443
            0x00101022
            0x041018a1
            0x37fff8e1
            0x0830a001
            0x38017048
            0x3c001021
            0x14000421
            0x14000823
            """
        self.compareMultipleCode(mips_code, binary_code)

    def test_for_removing_brackets_and_commas_in_mips(self):
        mips_code = \
            """
            add     r1, r2, r3
            add     r4, r1, r2
            and     r6, r5, r1
            load    r1, 0xfffe(r7)
            sll     r8, r1, 1
            store   r8, 0x5c(r2)
            beq     r1, r1, 4
            addi    r1, r1, 1
            addi    r3, r1, 2
            """
        binary_code = \
            """
            0x00100443
            0x00101022
            0x041018a1
            0x37fff8e1
            0x0830a001
            0x38017048
            0x3c001021
            0x14000421
            0x14000823
            """
        self.compareMultipleCode(mips_code, binary_code)


if __name__ == '__main__':
    unittest.main()
