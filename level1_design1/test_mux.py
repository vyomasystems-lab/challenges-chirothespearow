# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
from random import randint

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    #Manually assigning variables to each input
    i0=00
    i1=00
    i2=00
    i3=00
    i4=00
    i5=00
    i6=00
    i7=00
    i8=00
    i9=00
    i10=00
    i11=00
    i12=00
    i13=00
    i14=00
    i15=00
    i16=00
    i17=00
    i18=00
    i19=00
    i20=00
    i21=00
    i22=00
    i23=00
    i24=00
    i25=00
    i26=00
    i27=00
    i28=00
    i29=00
    i30=3
    select=30
    #input driving
    dut.inp0.value=i0
    dut.inp1.value=i1
    dut.inp2.value=i2
    dut.inp3.value=i3
    dut.inp4.value=i4
    dut.inp5.value=i5 
    dut.inp6.value=i6 
    dut.inp7.value=i7 
    dut.inp8.value=i8 
    dut.inp9.value=i9 
    dut.inp10.value=i10
    dut.inp11.value=i11
    dut.inp12.value=i12
    dut.inp13.value=i13 
    dut.inp14.value=i14 
    dut.inp15.value=i15
    dut.inp16.value=i16
    dut.inp17.value=i17 
    dut.inp18.value=i18
    dut.inp19.value=i19 
    dut.inp20.value=i20 
    dut.inp21.value=i21 
    dut.inp22.value=i22
    dut.inp23.value=i23 
    dut.inp24.value=i24
    dut.inp25.value=i25 
    dut.inp26.value=i26 
    dut.inp27.value=i27 
    dut.inp28.value=i28
    dut.inp29.value=i29 
    dut.inp30.value=i30
    dut.sel.value=select
    await Timer(2, units='ns')
    inps=[i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30]
    mux_out=False
    for i in range(len(inps)):          #Traversing through list inps in order to get correct output
        if i==select:
            mux_out=inps[i]
    assert dut.out.value == mux_out, f"MUX result is incorrect: {dut.out.value} != 11"
    cocotb.log.info('##### CTB: Develop your test here ########')

#Same as above but with random values
@cocotb.test()
async def test_mux_random(dut):
    """Test for mux2"""
    for i in range(5):
        i0=randint(0,3)
        i1=randint(0,3)
        i2=randint(0,3)
        i3=randint(0,3)
        i4=randint(0,3)
        i5=randint(0,3)
        i6=randint(0,3)
        i7=randint(0,3)
        i8=randint(0,3)
        i9=randint(0,3)
        i10=randint(0,3)
        i11=randint(0,3)
        i12=randint(0,3)
        i13=randint(0,3)
        i14=randint(0,3)
        i15=randint(0,3)
        i16=randint(0,3)
        i17=randint(0,3)
        i18=randint(0,3)
        i19=randint(0,3)
        i20=randint(0,3)
        i21=randint(0,3)
        i22=randint(0,3)
        i23=randint(0,3)
        i24=randint(0,3)
        i25=randint(0,3)
        i26=randint(0,3)
        i27=randint(0,3)
        i28=randint(0,3)
        i29=randint(0,3)
        i30=randint(0,3)
        select=randint(0,30)
        #input driving
        dut.inp0.value=i0
        dut.inp1.value=i1
        dut.inp2.value=i2
        dut.inp3.value=i3
        dut.inp4.value=i4
        dut.inp5.value=i5 
        dut.inp6.value=i6 
        dut.inp7.value=i7 
        dut.inp8.value=i8 
        dut.inp9.value=i9 
        dut.inp10.value=i10
        dut.inp11.value=i11
        dut.inp12.value=i12
        dut.inp13.value=i13 
        dut.inp14.value=i14 
        dut.inp15.value=i15
        dut.inp16.value=i16
        dut.inp17.value=i17 
        dut.inp18.value=i18
        dut.inp19.value=i19 
        dut.inp20.value=i20 
        dut.inp21.value=i21 
        dut.inp22.value=i22
        dut.inp23.value=i23 
        dut.inp24.value=i24
        dut.inp25.value=i25 
        dut.inp26.value=i26 
        dut.inp27.value=i27 
        dut.inp28.value=i28
        dut.inp29.value=i29 
        dut.inp30.value=i30
        dut.sel.value=select
        await Timer(2, units='ns')
        inps=[i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30]
        mux_out=False
        for i in range(len(inps)):
            if i==select:
                mux_out=inps[i]
        assert dut.out.value == mux_out, f"Randomised Test failed; Expected:{mux_out}, Returned: {dut.out.value}"
