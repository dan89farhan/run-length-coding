import math

LFIX = 4
# print('length', len('11111111111'), len('00'), len('1'),
#       len('00000000000000000'))
data = '11111111111' + '00' + '1' + '00000000000000000'


def encodeRun(input_string):
    length = len(input_string)
    count = 1
    encryptCode = ''
    charIndex = 0
    # for charIndex in range(length):
    while charIndex < length:
        if charIndex + 1 < length and input_string[charIndex] == input_string[
                charIndex + 1]:
            # print(input_string[charIndex])
            count = count + 1
        else:
            # print('charIndex', charIndex, count)
            if count < LFIX:
                # encryptCode = encryptCode + ';'
                encryptCode = encryptCode + '0'
                passUntil = 4
                charIndex = charIndex - count + 1
                while passUntil > 0 and charIndex < length:
                    passUntil = passUntil - 1
                    encryptCode = encryptCode + input_string[charIndex]
                    # print(input_string[charIndex], encryptCode)
                    charIndex = charIndex + 1
                    # print(input_string[charIndex], charIndex)
                count = 1
                continue
            else:
                LPRE = int(math.log2(count))
                LSYM = count - 2**LPRE
                BINSYM = format(LSYM, '0' + str(LPRE) + 'b')
                # print(count, LSYM, BINSYM)
                LPRESYM = ''
                for i in range(LPRE - 1):
                    LPRESYM = LPRESYM + '1'
                LPRESYM = LPRESYM + '0'

                # encryptCode = encryptCode + ';' + LPRESYM + BINSYM + input_string[
                #     charIndex]

                encryptCode = encryptCode + LPRESYM + BINSYM + input_string[
                    charIndex]

            # encryptCode = encryptCode + ';' + char + '' + str(count)
            count = 1
        charIndex = charIndex + 1
        # print(char, encryptCode)

    return encryptCode


def decodeRun(encodedMessage):

    length = len(encodedMessage)
    charIndex = 0
    decodeMessage = ''

    while charIndex < length:
        count = 0
        if encodedMessage[charIndex] == '1':
            count += 1
            isZeroFound = False
            while not isZeroFound:
                charIndex += 1
                if encodedMessage[charIndex] == '0':
                    isZeroFound = True
                count += 1

            wordLength = 2**(count)
            sym = ''
            while count > 0 and charIndex < length:
                charIndex += 1
                if (charIndex < length):
                    sym = sym + encodedMessage[charIndex]
                count -= 1
            symLength = int(sym, 2)

            wordLength = wordLength + symLength
            count = 0

            for i in range(wordLength):
                decodeMessage = decodeMessage + encodedMessage[charIndex]
            # print(decodeMessage)
            wordLength = 0
            charIndex += 1

        elif encodedMessage[charIndex] == '0':
            charIndex += 1
            count = 0
            fourChar = ''
            while count < LFIX and charIndex < length:
                fourChar = fourChar + encodedMessage[charIndex]
                charIndex += 1
                count += 1
            charIndex -= 1
            decodeMessage = decodeMessage + fourChar

        charIndex += 1
        # print(charIndex, char)
    return decodeMessage


#Method call
# value = encode("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
# value = encode(data)
# if value[1] == 0:
#     print("Encoded value is {}".format(value[0]))
#     decode(value[0])

# outputFile = open('output.txt', 'a+')
# outputFile.write('\n\n\n\n')
# outputFile.write('************************\n')
# outputFile.write('Run length coding example\n')
# outputFile.write('original data\n')
# outputFile.write(str(data) + '\n')
# outputFile.write('encoded data \n')

# print('original data', data)
# encodedData = encodeRun(data)
# print(encodedData)
# outputFile.write(encodedData + '\n')
# decodedData = decodeRun(encodedData)
# print('decode data ', decodedData)
# outputFile.write('decoded data\n')
# outputFile.write(decodedData + '\n')

# print(data == decodedData)
