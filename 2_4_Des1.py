# Clasificar tres numeros en orden ascendente

# PSe pide al usuario los tres números
a = int(input("Ingrese el primer número (a): "))
b = int(input("Ingrese el segundo número (b): "))
c = int(input("Ingrese el tercer número (c): "))

# Comparar los números y ordenarlos
if a <= b and b <= c:
    print("Números en orden ascendente:", a, b, c)
elif a <= c and c <= b:
    print("Números en orden ascendente:", a, c, b)
elif b <= a and a <= c:
    print("Números en orden ascendente:", b, a, c)
elif b <= c and c <= a:
    print("Números en orden ascendente:", b, c, a)
elif c <= a and a <= b:
    print("Números en orden ascendente:", c, a, b)
else:
    print("Números en orden ascendente:", c, b, a)
