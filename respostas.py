import doctest
 
def exercicio1(vetor: tuple) -> float:
    """
    Função que calcula a norma euclidiana de um vetor.

    Args:
        vetor (tuple): Tupla em que cada elemento representa um componente do vetor.

    Returns:
        float: Norma euclidiana do vetor fornecido.

    Raises:
        TypeError: Se o argumento fornecido não for uma tupla.
        ValueError: Se algum elemento da tupla não for um número (int ou float).

    Examples:
        >>> exercicio1((3,4))
        5.0
        >>> exercicio1((3,-4))
        5.0
        >>> exercicio1((3,3,3,3))
        6.0
        >>> exercicio1(1)
        Traceback (most recent call last):
        ...
        TypeError: O argumento fornecido deve ser uma tupla.
        >>> exercicio1((1,"a"))
        Traceback (most recent call last):
        ...
        ValueError: Algum valor da tupla não é um número.
    """
    if not isinstance(vetor, tuple):
        raise TypeError("O argumento fornecido deve ser uma tupla.")
    
    for num in vetor:
        if not isinstance(num, (int, float)):
            raise ValueError("Algum valor da tupla não é um número.")
    
    return (sum(num**2 for num in vetor))**(1/2)


def exercicio2(ponto_1: tuple, ponto_2: tuple) -> tuple:
    """
    Função que retorna o coeficiente angular e o termo independente da equação de uma reta a partir de dois pontos na mesma.

    Args:
        ponto_1 (tuple): Ponto representado por tupla que pertence à reta.
        ponto_2 (tuple): Ponto representado por tupla que pertence à reta.

    Returns:
        tuple: Tupla contendo o coeficiente angular e o termo independente.

    Raises:
        TypeError: Se os argumentos fornecidos não forem tuplas.
        ValueError: Se algum valor da tupla não for um número válido.
        ZeroDivisionError: Se os pontos tiverem o mesmo valor de x.

    Examples:
        >>> exercicio2((2, 3), (5.5, 6.5))
        (1.0, 1.0)
        >>> exercicio2((0, 0), (3, 6))
        (2.0, 0.0)
        >>> exercicio2((0, 0), ("", 6))
        Traceback (most recent call last):
        ...
        ValueError: O argumento fornecido deve ser duas tuplas com dois números (int ou float).
        >>> exercicio2((3, 4), (3, 1))
        Traceback (most recent call last):
        ...
        ZeroDivisionError: Insira valores para o eixo x diferentes.
    """
    if (not isinstance(ponto_1, tuple) or not isinstance(ponto_2, tuple) or
        len(ponto_1) != 2 or len(ponto_2) != 2):
        raise TypeError("O argumento fornecido deve ser duas tuplas com dois números (int ou float).")
    
    for ponto in ponto_1 + ponto_2:  
        if not isinstance(ponto, (int, float)):
            raise ValueError("O argumento fornecido deve ser duas tuplas com dois números (int ou float).")
    
    try:
        a = (ponto_2[1] - ponto_1[1]) / (ponto_2[0] - ponto_1[0])
        b = ponto_1[1] - a * ponto_1[0]
        return a, b
    except ZeroDivisionError:
        raise ZeroDivisionError("Insira valores para o eixo x diferentes.")

if __name__ == "__main__":
    doctest.testmod()