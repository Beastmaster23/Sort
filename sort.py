import argparse

parser = argparse.ArgumentParser(prog="Sort", description="Sorts files: ")

parser.add_argument("-s", "--sort", help="sorts csv Files")
parser.add_argument("-o", "--output", help="Output File name", default="output.txt")
parser.add_argument("-l", help="Sort line instead", action="store_true")

args = parser.parse_args()

'''print(args)'''

def sortCsv(csvLines, output):
    print("Opening file...")
    outFile =open(output, "w")
    print("Sorting file...")
    for i in range(len(csvLines)):
        csv=csvLines[i][0:len(csvLines[i])-1].split(",")
        csv.sort()
        '''print(csv)'''
        for element in csv:
            outFile.write(element+",")
        if i<len(csvLines)-1:
            outFile.write("\n")
    print("Closing file...")
    outFile.close()

def sortLines(lines, output):
    print("Opening file...")
    outFile =open(output, "w")
    print("Sorting file...")
    lines.sort()
    for i in range(len(lines)):
        lines[i]=lines[i].strip("\n")

        if i<len(lines)-1:
            outFile.write(lines[i]+"\n")
        else:
            outFile.write(lines[i])
        '''print(lines[i])'''
    print("Closing file...")
    outFile.close()



if args.sort != None :
    file = open(args.sort, "r")
    flines =file.readlines()
    if not args.l:
        sortCsv(flines, args.output)
    else:
        sortLines(flines, args.output)
    file.close()
