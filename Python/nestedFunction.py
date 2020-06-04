def main():
    a = [0]
    def modify():
        e = a
        e = 5
    modify()
    print(a)

main()