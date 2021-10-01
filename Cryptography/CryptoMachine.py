"""
Created on Wed Sep  9 12:36:15 2020
@author: ISH KAPOOR
"""
def machine():

    keys = 'abcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()_-+=/.?|<>:;{}[]'
    values = keys[-1] + keys[0:-1]

    encryptDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))

    message = input("Plaese enter your secret message:\n")
    mode = input("Please enter the mode:\nE(Encode)/D(Decode)\n")

    if mode.upper() == 'E':
        newMessage1 = ''.join([encryptDict[lttr] for lttr in message.lower()])
        newMessage = ''.join([encryptDict[nM1] for nM1 in newMessage1.lower()])
    elif mode.upper() == 'D':
       newMessage1 = ''.join([decryptDict[lttr] for lttr in message.lower()])
       newMessage = ''.join([decryptDict[nM1] for nM1 in newMessage1.lower()])
    else:
        print("please enter a correct choice!")

    return newMessage

if __name__ == "__main__":

    machine = machine()
    print(machine)