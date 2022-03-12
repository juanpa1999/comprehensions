def run():
    for i in range (0, 1000):
        if i % 4 == 0 and i % 6 == 0 and i % 9 == 0:
            print(i)
    

if __name__ == '__main__':
    run()