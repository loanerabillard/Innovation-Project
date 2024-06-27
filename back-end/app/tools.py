from functools import wraps
import time

# def timeit(func):
#     @wraps(func)
#     def timeit_wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         total_time = end_time - start_time
#         print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
#         return result
#     return timeit_wrapper


# def timeit(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         print(f"Starting {func.__name__} with args: {args} and kwargs: {kwargs}")
        
#         result = func(*args, **kwargs)
        
#         end_time = time.time()
#         total_time = end_time - start_time
#         print(f"Finished {func.__name__} with args: {args} and kwargs: {kwargs}")
#         print(f"Total time taken by {func.__name__}: {total_time:.4f} seconds")
        
#         return result
#     return wrapper


import time
import inspect
from functools import wraps

def is_simple_type(value):
    return isinstance(value, (int, float, str, bool))

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Getting the function's argument names
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Preparing the args and kwargs with their names and values or types
        all_args = ', '.join(f"{name}={value}" if is_simple_type(value) else f"{name}={type(value).__name__}"
                             for name, value in bound_args.arguments.items())
        
        print(f"\nStarting : {func.__name__}({all_args})")
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        total_time = end_time - start_time
        
        print(f"Finished : {func.__name__}({all_args}) : {total_time:.4f} seconds\n")
        
        return result
    return wrapper

