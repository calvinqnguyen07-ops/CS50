def main():
    items = {}
    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            break
        if item:
            items[item] = items.get(item, 0) + 1

    print()
    for item in sorted(items):
        print(items[item], item)


if __name__ == "__main__":
    main()
