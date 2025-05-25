def calcFreq(string):

    splitstr = string.split(" ")
    dict = {}

    for i in splitstr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    print(dict)

output = input("Enter sentance to check the frequency: ")

calcFreq(output)