def main():
    try:
        with open("test.png", "rb") as f:
            data = f.read()
            print(type(data))
        with open("test_new.png", "wb") as f2:
            f2.write(data)

    except FileNotFoundError as e:
        print("this file is can not open")
    except IOError as e:
        print("have a error when read file")
    print("read file finish")


if __name__ == "__main__":
    main()
