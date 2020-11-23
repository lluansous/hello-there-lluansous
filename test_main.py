"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_main(self):
        """Função que testa se a saída do programa corresponde ao que foi especificado."""
        with patch('builtins.print') as mock_print:
            main.main()
            mock_print.assert_called_with('Hello There!')


if __name__ == '__main__':
    unittest.main()
