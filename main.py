# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    nombres = [x+1 for x in range(30)if x%2 !=0]
    print(nombres)

if __name__ == '__main__':
    main()