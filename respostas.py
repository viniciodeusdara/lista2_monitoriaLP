import doctest

def exercicio1(vetor: tuple) -> float:
    """
    Função que calcula a norma euclidiana de um vetor.

    Args:
        vetor (tuple): Tupla em que cada elemento representa um componente do vetor

    Returns:
        float: Norma euclidiana do vetor fornecido
        
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
        TypeError: O argumento fornecido deve ser uma tupla com ints ou floats.
        >>> exercicio1((1,"a"))
        Traceback (most recent call last):
        ...
        TypeError: O argumento fornecido deve ser uma tupla com ints ou floats.
    """
    try:
        sum = 0
        for num in vetor:
            sum += num**2
        return sum**(1/2)
    except TypeError:
        raise TypeError("O argumento fornecido deve ser uma tupla com ints ou floats.")
    


def exercicio2(ponto_1: tuple, ponto_2: tuple) -> tuple:
    """
    Função que retorna o coeficiente angular e o termo independente da equação de uma reta a partir de dois pontos na mesma.

    Args:
        ponto_1 (tuple): Ponto representado por tupla que pertence à reta.
        ponto_2 (tuple): Ponto representado por tupla que pertence à reta.

    Returns:
        tuple: Tupla contendo o coeficiente angular e o termo independente.

        Examples:
        >>> exercicio2((2, 3), (5.5, 6.5))
        (1.0, 1.0)
        >>> exercicio2((0, 0), (3, 6))
        (2.0, 0.0)
        >>> exercicio2((0, 0), ("", 6))
        Traceback (most recent call last):
        ...
        TypeError: O argumento fornecido deve ser duas tuplas com ints ou floats.
        >>> exercicio2((3, 4), (3,1))
        Traceback (most recent call last):
        ...
        ZeroDivisionError: Insira valores para o eixo x diferentes.
    """
    try:
        a = (ponto_2[1] - ponto_1[1])/(ponto_2[0] - ponto_1[0])
        b = ponto_1[1] - a*ponto_1[0]
        return a, b
    except TypeError:
        raise TypeError("O argumento fornecido deve ser duas tuplas com dois ints ou floats.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Insira valores para o eixo x diferentes.")


if __name__ == "__main__":
    doctest.testmod(verbose=True)