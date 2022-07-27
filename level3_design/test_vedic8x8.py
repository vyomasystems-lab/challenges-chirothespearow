# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def vedic_basic_test(dut):
    """Test for 5 * 10"""

    # input driving
    dut.a.value = 5
    dut.b.value = 10

    await Timer(2, units='ns')

    assert dut.prod.value == 5*10, f"Multiplier result is incorrect: {int(dut.prod.value)} != 50"


@cocotb.test()
async def vedic_randomised_test(dut):

    for i in range(5):

        A = random.randint(0, 15)
        B = random.randint(0, 15)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A*B:05} DUT={int(dut.prod.value):05}')
        assert dut.prod.value == A*B, "Randomised test failed with: {A} * {B} = {PROD}".format(
            A=dut.a.value, B=dut.b.value, PROD=dut.prod.value)
