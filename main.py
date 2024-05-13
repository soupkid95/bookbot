def main():
    with open('/root/workspace/github.com/bookbot/books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)

main()