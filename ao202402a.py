def main():
    with open("aoc202402.txt", 'r') as f:
        print([all([x-y in range(1,4) for (x,y) in zip(L,L[1:])]) or all([x-y in range(-3,0) for (x,y) in zip(L,L[1:])]) for L in [[int(num) for num in line.split()] for line in f]].count(True))

if __name__ == "__main__":
    main()
