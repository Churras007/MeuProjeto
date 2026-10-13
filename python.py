import math

A = float(input("Dê um valor para A"))
B = float(input("Dê um valor para B"))
C = float(input("Dê um valor para C"))

Formula_delta = B**2 - 4*A*C

if Formula_delta > 0:
    Bhaskara1 = (-B + math.sqrt(Formula_delta) / 2 * A)
    Bhaskara2 = (-B - math.sqrt(Formula_delta) / 2 * A)
    print(f"Seu x1 é {Bhaskara1:.3f} e seu x2 é {Bhaskara2:.3f}")
elif Formula_delta == 0:
    Delta = -B / (2*A)
    print(f"Seu delta é 0, então x1 e x2 são {Delta:}")
else:
    print("Seu delta deu negativo")
