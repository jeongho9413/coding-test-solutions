import sys

def main() -> None:
  n, h, w = map(int, sys.stdin.readline().split())
  sy, sx = map(int, sys.stdin.readline().split())
  s = sys.stdin.readline().split()
  table = list()
  for i in range(h):
    table.append(list(map(int, sys.stdin.readline().split())))
  
  cy, cx = sy - 1, sx - 1
  res = list()
  for ch in s:
    if ch == "F":
      cy -= 1
    elif ch == "B":
      cy += 1
    elif ch == "L":
      cx -= 1
    elif ch == "R":
      cx += 1
    res.append(str(table[cy][cx]))
  sys.stdout.write("\n".join(res))

if __name__ == "__main__":
  main()
