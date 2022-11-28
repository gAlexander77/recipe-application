# Gilbert Martinez
scale = 3
F = 14 * scale
CAF = 0.65 + (0.01 * F)
UFP_TABLE = [4,5,4,10,7]
Outputs = [50,40,35,6,4]
UPF = 0
for i in range(len(UFP_TABLE)):
    UPF += UFP_TABLE[i]*Outputs[i]
FP = UPF * CAF
print("FP =",FP)