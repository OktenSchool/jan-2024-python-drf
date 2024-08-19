from unittest import TestCase
from unittest.mock import MagicMock, patch

from apps.cars.services import calc, math


class CalcTestCase(TestCase):
    @patch.object(math, 'cos')
    def test_plus(self, mock_math: MagicMock):
        mock_math.return_value = 25
        res = calc(1, 2, '+')
        self.assertEqual(res, 28)
        self.assertEqual(mock_math.call_count, 1)
    @patch('apps.cars.services.sqrt')
    def test_multi(self, mock_sqrt: MagicMock):
        mock_sqrt.return_value = 2
        res = calc(1, 2, '*')
        self.assertEqual(res, 4)
        self.assertEqual(mock_sqrt.call_count, 1)

    def test_divide(self):
        res = calc(1, 2, '/')
        self.assertEqual(res, 0.5)
