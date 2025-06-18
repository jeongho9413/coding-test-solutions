"""
inspired by Flying Pan :)
this is the easiest way to solve it
"""
import sys

def is_palindrome(s: str) -> bool:
  a = [c.lower() for c in s if c.isalnum()]
  return a == a[::-1]

def main() -> None:
  a = str(input())
  print(is_palindrome(a))

if __name__ == "__main__":
  main()
