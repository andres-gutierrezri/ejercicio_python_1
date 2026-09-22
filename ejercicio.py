def tipo_triangulo(a, b, c):
    """
    Determina si tres lados pueden formar un triángulo y, de ser así, 
    identifica el tipo de triángulo.
    
    Parámetros:
    a, b, c: Lados del triángulo (números positivos).

    Retorna:
    - Un mensaje indicando si los lados forman un triángulo.
    - Si forman un triángulo, el tipo de triángulo (equilátero, isósceles o escaleno).
    """
    # Verificar si los lados forman un triángulo
    if a + b > c and a + c > b and b + c > a:
        # Determinar el tipo de triángulo
        if a == b == c:
            return "Es un triángulo equilátero."
        elif a == b or a == c or b == c:
            return "Es un triángulo isósceles."
        else:
            return "Es un triángulo escaleno."
    else:
        return "Los lados dados no forman un triángulo."

# Ejemplo de uso
if __name__ == "__main__":
    lado1 = float(input("Ingrese el primer lado: "))
    lado2 = float(input("Ingrese el segundo lado: "))
    lado3 = float(input("Ingrese el tercer lado: "))
    
    resultado = tipo_triangulo(lado1, lado2, lado3)
    print(resultado)