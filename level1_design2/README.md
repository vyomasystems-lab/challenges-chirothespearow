# Level 1 - Sequence Detector (1011 with Overlap) Design Verification

## Verification Environment
A [CoCoTb](https://www.cocotb.org/) based Python test is implemented to carry out verification. The test drives inputs to the Design Under Test (sequence detector module here) which takes three 1-bit inputs *inp_bit, clk and reset*, and produces a 1-bit output *seq_seen*.

The values of the input are assigned using
```
dut.inp_bit.value = i
dut.reset.value = 0
dut.reset.value = 1
```
The clock is set using ```clock = Clock(dut.clk, 10, units="us")```.
The input bit was given both a random and pre-selected sequence, tested under different test modules.
The assert statement is used for comparing the Sequence Detector's output to the expected value.

The following error is seen:
```
assert dut.seq_seen.value == ou[count], f"Sequence output is incorrect: {dut.seq_seen.value} != {ou[count]}"
                     AssertionError: Sequence output is incorrect: 0 != 1
```
## Test Scenarios
- Test Inputs: inp_bit = 101110110111011
- Expected Output = 000100010010001
- Observed Output in the DUT dut.seq_seen = 0001000      //Sequence broken off due to mismatch

Output mismatch for the above input proves that there is a design bug.

## Design Bug
Based on the above test input and analysing the design, we see the following

### Bug 1
```
   SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;              ==> BUG
        else
          next_state = SEQ_10;
      end
```
According to the state diagram the next state when input is 1 should be SEQ_1, not IDLE

### Bug 2
```
   SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;             ==> BUG
      end
```
According to the state diagram the next state when input is 0 should be SEQ_10, not IDLE

### Bug 3 
```
   SEQ_1011:
      begin
        next_state = IDLE;                ==> BUG
      end
```
According to the state diagram the next state when input is 0 should be SEQ_10, not IDLE, and similarily when the input is 1, the next state should be SEQ_1.

## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/44639543/180658245-28dc4b56-75c0-4e08-89ae-6119ed3ea9ae.png)

The updated design is checked in as seq_detect_1011_corrected.v
## Verification Strategy
