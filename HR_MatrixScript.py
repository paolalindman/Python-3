# Matrix Script (Hakerrank)

#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
frase=""
for x in range(m):
    for y in range(n):
        frase += matrix [y][x]
frase = re.sub(r'(\w)\W+(\w)',r'\1 \2',frase)
print(frase)
