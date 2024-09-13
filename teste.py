import unittest
from unittest.mock import patch
import io
from respostas import exercicio1, exercicio2
from math import sqrt

def norma(vetor):
    return sqrt(sum(map(lambda m: m ** 2, vetor )))

class TestExercicio1(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_input(self, mock_stdout):
        self.assertEqual(exercicio1((1, 4, 6, 2)), norma([1, 4, 6, 2]))
        self.assertEqual(exercicio1((5, -5, 5)), norma([5, -5, 5]))
        self.assertEqual(exercicio1((1, 13)), norma([1, 13]))
        self.assertEqual(exercicio1((12, 2, -4, -8)), norma((12, 2, -4, -8)))
        self.assertEqual(exercicio1((-9, -1, 0, 0, 0, 0)), norma([-9, -1, 0, 0, 0, 0]))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input(self, mock_stdout):
        with self.assertRaises(TypeError):
            exercicio1(2)
        with self.assertRaises(TypeError):
            exercicio1(range(20))
        with self.assertRaises(TypeError):
            exercicio1({2, "99", 3})
        with self.assertRaises(ValueError):
            exercicio1((99, 2, "t"))
        with self.assertRaises(ValueError):
            exercicio1(("2",))
        with self.assertRaises(ValueError):
            exercicio1(("9", 2))

class TestExercicio2(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_input(self, mock_stdout):
        self.assertEqual(exercicio2((0, 0), (3, 6)), (2.0, 0.0))
        self.assertEqual(exercicio2((5.5, 6.5), (2, 3)), (1.0, 1.0))
        self.assertEqual(exercicio2((0.0, 3.5), (1, 12.5)), (9.0, 3.5))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input(self, mock_stdout):
        with self.assertRaises(TypeError):
            exercicio2([-1, 3], [2, 4])
        with self.assertRaises(TypeError):
            exercicio2([-1, False], 20)
        with self.assertRaises(TypeError):
            exercicio2("[-1, 3]", [2, 4])
        with self.assertRaises(TypeError):
            exercicio2((-1, 3, 9), (2, 4))
        with self.assertRaises(ValueError):
            exercicio2((-1, 3), (2, "4"))
        with self.assertRaises(ValueError):
            exercicio2((-1, 3), ("False", 4))
        with self.assertRaises(ZeroDivisionError):
            exercicio2((12, 2), (12, 8))

if __name__ == '__main__':
    unittest.main()