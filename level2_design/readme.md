# challenges-chirothespearow
![image](https://user-images.githubusercontent.com/44639543/180612307-01ec01e2-e672-4a59-aae8-53be6d120422.png)

# Level 2 - Bitmanipulation Co-processor Design Verification

## Verification Environment
A [CoCoTb](https://www.cocotb.org/) based Python test is implemented to carry out verification. The test drives inputs to the Design Under Test (bitmanip co-processor module here) which takes
three 32-bit inputs *(mav_putvalue_src1,mav_putvalue_src2 and mav_putvalue_src3)* which act as the operands for the operation to be performed, a 32-bit input *mav_putvalue_instr* which specifies which operation is to be carried out, and it gives a 33-bit output *mav_putvalue*.
The Least Significant Bit of the output signifies whether the output is valid (where a 0 means that it is invalid).

The values of the input are assigned using:
```
        mav_putvalue_src1 = random.randint(0,4294967295)      #2^32=4294967296
        mav_putvalue_src2 = random.randint(0,4294967295)
        mav_putvalue_src3 = random.randint(0,4294967295)
        mav_putvalue_instr = 0b01000001101000000111101000110011     #changed according to opcode
```

*SRC1, SRC2* and *SRC3* were given random values between 0 and 2^32. The *instr* input was changed according to each opcode's specification. 
The assert statement is used for comparing the processor's output to the expected value.

The following error is seen:
```
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x28180411 does not match MODEL = 0x42004189
```
## Test Scenario
- Test Inputs: *mav_putvalue_src1* = 889987788, *mav_putvalue_src2* = 383524667, *mav_putvalue_src3* = 4234271493, *mav_putvalue_instr*=0x41A07A33
- Expected Output: out = 0x42004189
- Observed Output in the DUT dut.mav_putvalue = 0x28180411

The output mismatch was found in the *ANDN* operation of the processor.
## Verification Strategy
Each of the three src inputs were given random 32-bit values, while the instr input was manually given inputs according to each opcode. The assert statement was used to compare the python-generated output to that of the DUT, and an error was thrown in case of a mismatch.
