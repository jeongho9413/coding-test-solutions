import sys

def is_palindrome(s: str) -> bool:
  a = [c.lower() for c in s if c.isalnum()]
  n = len(a)
  stack = list()

  for i in range(n // 2):
    stack.append(a[i])

  start = n // 2 if n % 2 == 0 else n // 2 + 1

  for i in range(start, n):
    if not stack or stack.pop() != a[i]:
      return False

  return True

def main() -> None:
  s = str(input().strip())
  print(is_palindrome(s))

if __name__ == "__main__":
  main()
