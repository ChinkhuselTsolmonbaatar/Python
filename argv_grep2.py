import sys

if len(sys.argv) != 3:
   sys.exit(f"Error:unappropriate number of arguments")
script = sys.argv[0]
f = sys.argv[2]
with open(f, 'r') as file:
    content = file.readlines()


def print_usage():
    print(f'Usage: python {script} pattern')
def main(argv):
    if not len(argv) ==1:
        print_usage()
    pattern = argv[0]
    for line in content:
        if pattern in line:
            print(line.strip())
if __name__ == "__main__":
    main(sys.argv[1:])