# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0
from cocotb.triggers import Timer
import os
from random import randint
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await RisingEdge(dut.clk)  
    dut.reset.value = 0
    await Timer(12, units='us')

    cocotb.log.info('#### CTB: Develop your test here! ######')
    sequence=[1,0,1,1,1,0,1,1,0,1,1,1,0,1,1]                #Input Sequence
    ou=      [0,0,0,1,0,0,0,1,0,0,1,0,0,0,1]                #Expected output
    count=0
    print('Input:\n101110110111011\n')
    print("Output: ")
    for i in sequence:                                      # Traversing through the sequence and comparing model output with expected output
        dut.inp_bit.value = i 
        #await RisingEdge(dut.clk)
        await Timer(10, units='us')
        assert dut.seq_seen.value == ou[count], f"Sequence output is incorrect: {dut.seq_seen.value} != {ou[count]}"
        count+=1
        print(dut.seq_seen.value, end= '')
    print('\n')
    
#Similiar to above but using a random sequence
@cocotb.test()
async def test_seq_bug1_random(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.inp_bit.value=0
    dut.reset.value = 1
    await RisingEdge(dut.clk)  
    dut.reset.value = 0
    await RisingEdge(dut.clk)  
    await Timer(12, units='us')

    cocotb.log.info('#### CTB: Develop your test here! ######')
    # Code to detect sequence in python
    sequence=[randint(0,1) for x in range(15)]
    stack=[]
    ou=      []
    #When the stack contains the sequence 1011, an output 1 is broadcasted
    for iterat in sequence:
        if len(stack)<4:
            stack.append(iterat)
            if stack==[1,0,1,1]:
                ou.append(1)
                continue
        elif len(stack)==4:
            stack.pop(0)
            stack.append(iterat)
            if stack==[1,0,1,1]:
                ou.append(1)
                continue
            else:
                
                ou.append(0)
                continue
        ou.append(0)    
    count=0
    print("Input:\n")
    for j in sequence:
        print(j,end='')
    print('\n')
    print("Output: ")
    for i in sequence:
        dut.inp_bit.value = i 
        #await RisingEdge(dut.clk)
        await Timer(10, units='us')
        assert dut.seq_seen.value == ou[count], f"Sequence output is incorrect: {dut.seq_seen.value} != {ou[count]}"
        count+=1
        print(dut.seq_seen.value, end= '')
    print('\n')
