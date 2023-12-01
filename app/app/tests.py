"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class TestCalculator(SimpleTestCase):
    """Test the calc module"""
    
    def test_addition(self):
        """Test adding numbers together"""
        res = calc.add(7,3)
        
        self.assertEqual(res, 10)
        
    def test_substraction(self):
        """Test substracting numbers"""
        res = calc.sub(9,6)

        self.assertEqual(res, 3)
        