# Dict[str, int] Validation Decorator

A robust Python 3.11+ decorator that enforces argument type validation for functions. It ensures that all positional and keyword arguments passed to the wrapped function are dictionaries mapping strings to integers (`dict[str, int]`).

## Features
- Strict Validation: 
  - Keys must be `str`.
  - Values must be `int`.
  - Strictly rejects `bool` values (even though `bool` is a subclass of `int` in Python).
- Comprehensive coverage: Validates both `*args` and `**kwargs`.
- Concise Error Messages: Provides clear feedback on exactly which argument failed and why.
- Zero Dependencies: Uses only standard library `functools`.

## Usage
Simply import the decorator and apply it to any function where you need to guarantee input types.

```python
from decorator import decorator

@decorator
def process_metrics(data):
    print(f"Processing: {data}")

# Valid usage
process_metrics({"cpu": 80, "memory": 2048})
# Invalid usage - Raises TypeError
process_metrics({"cpu": "high"})    # TypeError: Argument 'data': invalid item (str: str)
process_metrics({"valid": True})    # TypeError: Argument 'data': invalid item (str: bool)
process_metrics([1, 2, 3])          # TypeError: Argument 'data': expected dict[str, int], got list
```

## Running Tests
The repository includes a comprehensive `unittest` suite covering edge cases.

To run the tests:
```bash
python test_decorator.py
```