import sys

def main():
    s = str(sys.stdin.readline().strip())
    n = len(s)
    res = list()
    
    temp = "+" * (n + 2)
    res.append(temp)
    temp_2 = "+" + s + "+"
    res.append(temp_2)
    res.append(temp)
    
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
