def main():
    try:
            with open('/home/devill/passwd') as f:
                for no,line in enumerate(f,1):
                    if '/bin/bash' in line:
                        line = line.strip()
                        print(f'{no} {line}')
    except IOError as e:
            print(e)
if __name__ == '__main__': main()