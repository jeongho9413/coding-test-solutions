import sys

def main() -> None:
  n = int(sys.stdin.readline())
  arr = list(map(int, sys.stdin.readline().strip().split()))
  
  cnt = 0
  res = 0
  for i in range(n - 1):
    if arr[i] >= arr[i + 1]:
      cnt += 1
      res = max(res, cnt)
    else:
      cnt = 0
  
  print(res)
  return

if __name__ == "__main__":
  main()
