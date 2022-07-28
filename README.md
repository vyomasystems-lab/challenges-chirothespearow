# challenges-chirothespearow
![image](https://user-images.githubusercontent.com/44639543/180612307-01ec01e2-e672-4a59-aae8-53be6d120422.png)

# Level 1 - Multiplexer Design Verification

## Verification Environment
A [CoCoTb](https://www.cocotb.org/) based Python test is implemented to carry out verification. The test drives inputs to the Design Under Test (mux module here) which takes
31 2-bit inputs *(inp0,inp1 ... inp30)*, a 5-bit input *sel*, and gives a 2-bit output *out*.

The values of the input are assigned using

```
i0=randint(0,3)
dut.inp0.val = i0

i1=randint(0,3)
dut.inp1.val = i1
.
..
...

i30=randint(0,3)
dut.inp30.val=i30

dut.sel.val=randint(0,30)
```
All inputs were given a random value between 0 and 3. The *sel* input was given a random value between 0 and 30.

The assert statement is used for comparing the Multiplexer's output to the expected value.

The following errors are seen:

Error 1:
```
assert dut.out.value == mux_out, f"Randomised Test failed; Expected:{mux_out}, Returned: {dut.out.value} for select:{select}"
                     AssertionError: Randomised Test failed; Expected:3, Returned: 00 for select:30
```

Error 2:
```
assert dut.out.value == mux_out, f"Randomised Test failed; Expected:{mux_out}, Returned: {dut.out.value} for select:{select}"
                     AssertionError: Randomised Test failed; Expected:0, Returned: 01 for select:13
```

Error 3:
```
assert dut.out.value == mux_out, f"Randomised Test failed; Expected:{mux_out}, Returned: {dut.out.value} for select:{select}"
                     AssertionError: Randomised Test failed; Expected:2, Returned: 00 for select:12
```
## Test Scenarios
Test 1
- Test Inputs: inp30 = 3, sel = 30
- Expected Output: out = 3 (binary--> 11)
- Observed Output in the DUT dut.sel = 00

Test 2
- Test Inputs: inp13 = 0, sel = 13
- Expected Output: out = 0 (binary--> 00)
- Observed Output in the DUT dut.sel = 01

Test 3
- Test Inputs: inp12 = 2, sel = 12
- Expected Output: out = 2 (binary--> 10)
- Observed Output in the DUT dut.sel = 00

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

### Bug 1
```
      .
      ..
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      //BUG; Missing Statement
      default: out = 0;
```
The code is missing the statement ```5'b11110: out = inp30;```, so when *sel* = 30 , the wrong output is obtained.

### Bug 2
```   
      .
      ..
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;  ==> BUG
      5'b01101: out = inp13;

```

The binary value of *inp12* is incorrectly specified as 01101 , which is actually the binary value of 13. This causes the design to provide the wrong outputs when *sel* = 12 or 13. The correct binary value of 12 is 01100.

## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/44639543/180617469-3946cd01-b3f7-47b6-a5ac-fe8c0958aa62.png)

The updated design is checked in as mux_corrected.v
## Verification Strategy
Two test modules were created, one piped in predefined inputs while the other gave random test inputs. The output of the multiplexer was simulated in python by creeating a list of all the inputs, and comparing the index value of each element to the select input in order to obtain the correct result. The assert statement was used to compare the python-generated output to that of the DUT, and an error was thrown in case of a mismatch. This error was investigated and the source code was thoroughly combed through to find the bug. 

