"""
two-branch
"""
import sys
import os

def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

def main() -> None:
  a = int(input().strip())
  print(fibonacci(a))

if __name__ == "__main__":
  main()
