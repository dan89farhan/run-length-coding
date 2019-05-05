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
                encryptCode = encryptCode + ';'
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

                encryptCode = encryptCode + ';' + LPRESYM + BINSYM + input_string[
                    charIndex]

            # encryptCode = encryptCode + ';' + char + '' + str(count)
            count = 1
        charIndex = charIndex + 1
        # print(char, encryptCode)

    return encryptCode


def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
                #print lst
            count = 1
            prev = character
        else:
            count += 1
    else:
        try:
            entry = (character, count)
            lst.append(entry)
            return (lst, 0)
        except Exception as e:
            print("Exception encountered {e}".format(e=e))
            return (e, 1)


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q


#Method call
# value = encode("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
# value = encode(data)
# if value[1] == 0:
#     print("Encoded value is {}".format(value[0]))
#     decode(value[0])

encodedData = encodeRun(data)
print(encodedData)
