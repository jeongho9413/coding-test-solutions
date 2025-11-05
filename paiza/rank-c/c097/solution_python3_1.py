import sys

def main() -> None:
  input = sys.stdin.readline
  n, x, y = map(int, input().split())
  
  output = list()
  for i in range(1, n + 1):
    a = (i % x == 0)
    b = (i % y == 0)
    output.append("AB" if a and b else "A" if a else "B" if b else "N")
  sys.stdout.write("\n".join(output))

if __name__ == "__main__":
  main()
