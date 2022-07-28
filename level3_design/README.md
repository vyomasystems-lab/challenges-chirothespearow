# challenges-chirothespearow
![image](https://user-images.githubusercontent.com/44639543/181307506-b5fca863-1439-4b02-b7f1-34283b273eaf.png)

# Level 3 - Vedic 8-bit Multiplier Design Verification

## Verification Environment
A [CoCoTb](https://www.cocotb.org/) based Python test is implemented to carry out verification. The test drives inputs to the Design Under Test (mux module here) which takes
2 8-bit inputs *a* and *b*, and gives a 16-bit output *prod*.

The values of the input are assigned using
```
dut.a.value = 5
dut.b.value = 10
```
Fixed values were given to both inputs for this test

For the random test module:
```
A = random.randint(0, 15)
B = random.randint(0, 15)
dut.a.value = A
dut.b.value = B
```
The inputs were given a random value between 0 and 15.
The assert statement is used for comparing the Multiplier's output to the expected value.

The following errors are seen:

Error 1
```
assert dut.prod.value == 5*10, f"Multiplier result is incorrect: {dut.prod.value} != 50"
                     AssertionError: Multiplier result is incorrect: 2 != 50
```
Error 2
```
assert dut.prod.value == A*B, "Randomised test failed with: {A} * {B} = {PROD}".format(
                     AssertionError: Randomised test failed with: 00000100 * 00000110 = 0000000000001000
```
## Test Scenarios
Test 1
- Test Inputs: a = 5, b=10
- Expected Output: out = 50
- Observed Output in the DUT dut.prod = 2

Test 2
- Test Inputs: a = random.randint(0, 15), b = random.randint(0, 15)
- Expected Output: out = 0 (binary--> 00)
- Observed Output in the DUT dut.sel = 01

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

### Bug 
```
assign prod = {sum1,mult0[3:0]};
```
Instead of sum2, sum1 has been assigned to the product, resulting in an incorrect output.

## Design Fix
Updating the design and re-running the test makes the test pass.
![image](https://user-images.githubusercontent.com/44639543/181319134-c51713b4-91da-43a8-a9b5-128320a9f1fe.png)

The updated design is checked in as vedic8x8_corrected.v
## Verification Strategy
Each of the three *src* inputs were given random 32-bit values, while the *instr* input was manually given inputs according to each opcode. The assert statement was used to compare the python-generated output to that of the DUT, and an error was thrown in case of a mismatch. 
