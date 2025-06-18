# import sys
# import os

def factorial(n):
  if n <= 1:
    return 1
  return n * factorial(n - 1)

def main() -> None:
  a = int(input().strip())
  result = factorial(a)
  print(result)

if __name__ == "__name__":
  main()
