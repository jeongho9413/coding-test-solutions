import sys

def main() -> None:
  a, b = map(int, sys.stdin.readline().strip().split())
  
  if b == 1:
    print("0")
    return
  
  cur = 0
  res = 0
  while cur < b:
    if res == 0:
      cur = a
    else:
      cur += (a - 1)
    res += 1
  print(str(res))
  return
      

if __name__ == "__main__":
  main()
