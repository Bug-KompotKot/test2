from typing import Any, List

def foo(a: str) -> str:
    return '(' + a.split() + ')'

def main():
    print(
        "The AWS CLI stores sensitive credential information that you specify with aws configure in a local file..."
    )

