"""
Sample tests
"""

from django.tests import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(selfish):
        """"Test adding numbers together"""
        res=calc.add(2,3)
        selfish.assertEqual(res,5)