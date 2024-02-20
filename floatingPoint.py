import numpy as np

number = 2

print(np.binary_repr(np.float32(number).view(np.int32), width=32))

sign = '1' if np.signbit(number) else '0'
exponent = np.binary_repr(np.float32(number).view(np.int32) >> 23 & 0xff, width=8)
mantissa = np.binary_repr(np.float32(number).view(np.int32) & 0x7fffff, width=23)

print(f"Sign: {sign}, Exponent: {exponent}, Mantissa: {mantissa}")