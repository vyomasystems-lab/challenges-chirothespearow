# challenges-chirothespearow
![image](https://user-images.githubusercontent.com/44639543/180612307-01ec01e2-e672-4a59-aae8-53be6d120422.png)

# Level 1 - Multiplexer Design Verification

## Verification Environment
A [CoCoTb](https://www.cocotb.org/) based Python test is implemented to carry out verification. The test drives inputs to the Design Under Test (mux module here) which takes
31 2-bit inputs *(inp0,inp1 ... inp30)*, a 5-bit input *sel*, and gives a 2-bit output *out*.
