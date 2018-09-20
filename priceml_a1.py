"""

@author Mia Price
@since 2018-20-2018
@version 1
"""

import sys

def readFASTQ(fileName):
    """

    @param fileName:
    @type fileName:
    @return:
    @rtype:
    """
    file = open(fileName, "r")

    defLine = file.readline()
    sequence = file.readline()
    file.readline()
    qualASCII = file.readline()

    file.close()

    return defLine, sequence, qualASCII

def getPhredQual(quality):
    """

    @param quality:
    @type quality:
    @return:
    @rtype:
    """
    ASCII_to_Phred = {"!": 0, '"': 1, '#': 2, "$": 3, "%": 4, "&": 5, "'": 6, "(": 7, ")": 8, "*": 9, "+": 10, ",": 11,
                      "-": 12, ".": 13, "/": 14, "0": 15, "1": 16, "2": 17, "3": 18, "4": 19, "5": 20, "6": 21, "7": 22,
                      "8": 23, "9": 24, ":": 25, ";": 26, "<": 27, "=": 28, ">": 29, "?": 30, "@": 31, "A": 32, "B": 33,
                      "C": 34, "D": 35, "E": 36, "F": 37, "G": 38, "H": 39, "I": 40, "J": 41, "K": 42}

    phredQual = []

    for each in quality:
        if each == "\n":
            break
        phredQual.append(ASCII_to_Phred[each])

    return phredQual


def trimLowQual5Prime(phredQualList):
    """

    @param phredQualList:
    @type phredQualList:
    @return:
    @rtype:
    """
    for i in range(0, len(phredQualList)):
        if (phredQualList[i] >= 20):
            start = i
            break

    return start

def trimLowQual3Prime(phredQualList):
    """

    @param phredQualList:
    @type phredQualList:
    @return:
    @rtype:
    """
    phredQualList.reverse()
    position = trimLowQual5Prime(phredQualList)
    end = len(phredQualList) - position
    return end

def writeHighQualFASTQ(fileName, defLine, sequence, qualASCII):
    """

    @param fileName:
    @type fileName:
    @param defLine:
    @type defLine:
    @param sequence:
    @type sequence:
    @param qualASCII:
    @type qualASCII:
    @return:
    @rtype:
    """
    fileName = fileName.split(".fastq")[0] + ".trim.fastq"

    file = open(fileName, "w+")
    file.writelines([defLine, sequence, "\n+\n", qualASCII])

    file.close()

    print("New file has been created")


def trimLowQual5PrimeCS(phredQualList):
    """

    @param phredQualList:
    @type phredQualList:
    @return:
    @rtype:
    """
    winSize = 6
    length = len(phredQualList)
    done = False
    start = 0

    while done != True:

        idx = 0

        averageOfFrame = sum(phredQualList[idx:idx + winSize]) / winSize

        if averageOfFrame >= 15:
            start = idx
            done = True
        else:
            smolArray = phredQualList[idx:idx + winSize]

            for i in range()
            idx = trimLowQual3Prime(smolArray) + idx

    return start


def main():
    print("Now running:", sys.argv[0], "on", sys.argv[1])
    fileName = sys.argv[1]
    defLine, sequence, qualASCII = readFASTQ(fileName)
    phredQual = getPhredQual(qualASCII)
    # start = trimLowQual5Prime(phredQual)
    start = trimLowQual5PrimeCS(phredQual)
    end = trimLowQual3Prime(phredQual)
    sequence = sequence[start:end]
    qualASCII = qualASCII[start:end]
    writeHighQualFASTQ(fileName, defLine, sequence, qualASCII)

if __name__ == '__main__':
    main()