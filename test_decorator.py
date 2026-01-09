
import unittest
from decorator import decorator

@decorator
def func(*args, **kwargs):
    pass

class TestDecorator(unittest.TestCase):
    def test_basic_dict(self):
        func({"a": 1})
        func(x={"a": 1})
        
    def test_empty_dict(self):
        func({}) 
        
    def test_bool_value(self):
        # Booleans are subclasses of int, so we need to explicitly disallow them
        with self.assertRaisesRegex(TypeError, "invalid item"):
            func({"a": True})

    def test_non_dict_arg(self):
        with self.assertRaisesRegex(TypeError, "expected dict"):
            func(1)
            
    def test_mixed_types_key(self):
        with self.assertRaisesRegex(TypeError, "invalid item"):
            func({1: 1})

    def test_mixed_types_value(self):
        with self.assertRaisesRegex(TypeError, "invalid item"):
            func({"a": "string"})

if __name__ == "__main__":
    unittest.main()
