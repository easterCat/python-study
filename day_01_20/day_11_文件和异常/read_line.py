import time


def main():
    with open("./abc.txt", 'r', encoding="utf-8") as f:
        print(f.read())
    print("")
    print("")
    with open("abc.txt", mode='r') as f:
        for line in f:
            print(line, end="**结尾**")
            time.sleep(0.5)
        print()
    print("")
    print("")
    with open("abc.txt") as f:
        lines = f.readlines()
    print(lines)


if __name__ == "__main__":
    main()
