def run():
    words = input('write a reverse word l`ll give you the right one: ')
    words = words.upper()
    words = words.strip()
    words = words[::-1]     
    words = words.split(sep=' ')
    words = words[::-1]
    print(words)


if __name__ == '__main__':
    run()