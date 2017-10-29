import sys
import csv

class BSTNode:
 def __init__ (self, key, value, left="", right="", parent=""):
     self.key=key;
     self.value=value;
     self.left=left;
     self.right=right;
     self.parent=parent;

def main():
    arguments=[]

    # read cmd args & print them
    for i in range(len(sys.argv)):
        print(sys.argv[i])
        arguments.append(sys.argv[i])

    (x,y) = (arguments[1], arguments[2])
    print("x={}, y={}".format(x, y))

    # swap them
    (x, y) = (y, x)
    print("x={}, y={}".format(x, y))

    # print("Hello World")
    root = BSTNode(key=1,value="a");

    # open/create file
    file = open("coordinates.csv", "w")
    writer = csv.writer(file)

    # write coordinates to file
    writer.writerow((x,y))

    file.close()

if __name__ == "__main__":
    main()
