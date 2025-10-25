"""
Burda call stack-lərə aid funksiyalar veriləcək.

Author: Rafael Alikhanli
Date: 25.10.2025
Python version: 3.11 +

Python kodunun işləmə ardıcıllığı
Your Python Code (.py file)
        ↓
    [Parser]
        ↓
    Abstract Syntax Tree (AST)
        ↓
    [Compiler]
        ↓
    Bytecode (.pyc file)
        ↓
    [Python Virtual Machine]
        ↓
    CPython Interpreter (C code)
        ↓
    System Calls
        ↓
    Operating System Kernel
        ↓
    CPU Execution
"""


def add(a: int, b: int) -> int:
    """
    Bytcode analiz etmək üçün bəsit funksiya .

    Args:
        a (int): Birinci rəqəm.
        b (int): İkinci rəqəm.
    Returns:
        int: Cəmi.
    """

    c = a + b
    return c


code = add.__code__

print("\nFunction Name:", add.__name__)
print("\nFunction module: ", add.__module__)
print("\nFunction docstring: ", add.__doc__)
print("\nFunction Annotations: ", add.__annotations__)
print("=" * 80)
print("\nArgument variables:", code.co_argcount)
print("\nLocal variables:", code.co_nlocals)
print("\nVariable names:", code.co_varnames)
