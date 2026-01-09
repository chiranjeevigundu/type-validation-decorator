
from typing import Callable, Any, Dict
import functools

def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that enforces type validation on all arguments passed to the wrapped function.
    Args:
        function (Callable): The function to wrap.
    Returns:
        Callable: The wrapped function with argument validation logic.
    Raises:
        TypeError: If any argument is not a dict[str, int].
    """
    @functools.wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Validate positional arguments
        for i, arg in enumerate(args):
            validate_dict_str_int(arg, f"Argument {i}")
        
        # Validate keyword arguments
        for name, arg in kwargs.items():
            validate_dict_str_int(arg, f"Argument '{name}'")
            
        return function(*args, **kwargs)
    return wrapper

def validate_dict_str_int(arg: Any, arg_name: str) -> None:
    """
    Helper function to validate that a single argument is a dict[str, int].
    """
    if not isinstance(arg, dict):
        raise TypeError(f"{arg_name}: expected dict[str, int], got {type(arg).__name__}")
    
    for key, value in arg.items():
        # bool is a subclass of int, so we explicitly check for bool to exclude it.
        is_string_key = isinstance(key, str)
        is_int_value = isinstance(value, int) and not isinstance(value, bool)
        
        if not is_string_key or not is_int_value:
            raise TypeError(
                f"{arg_name}: invalid item ({type(key).__name__}: {type(value).__name__})"
            )
