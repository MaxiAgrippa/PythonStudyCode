def main():
    f = open('lines.txt')
    for line in f:
        print(line.rstrip())

    infile = open('lines.txt', 'rt')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

    infile = open('berlin.jpg', 'rb')
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else:
            break
    outfile.close()
    print('\ndone.')


if __name__ == '__main__':
    main()
