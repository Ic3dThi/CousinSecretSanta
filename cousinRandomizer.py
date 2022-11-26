import time
import csv
import random
import datetime
from twilio.rest import Client



client = Client(account_sid, auth_token)
from_number = '+13253088249'
to_number = '3462549945'

failurePrev = True
while failurePrev:
    with open('CousinChristmasList.csv') as file1:
        reader1 = csv.reader(file1)
        # sideA = random.choice(list(reader1))
        li1 = list(reader1)
        # print(li1)
        random.shuffle(li1)
    with open('CousinChristmasList.csv') as file2:
        reader2 = csv.reader(file2)
        # sideA = random.choice(list(reader1))
        li2 = list(reader2)
        random.shuffle(li2)
        # print(li2)
    finalList = []
    failure = False
    while len(li1) > 0 and len(li2) > 0:
        left = li1[0]
        right = li2[0]
        matched = 0
        start = ''
        looping = False
        while matched == 0:
            if looping == True and start == right:
                break
            if left[1] != right[1] and left[3] == right[3]:
                finalList.append([left[0], left[1], left[2], '-', right[0], right[1], right[2], right[4]])
                li1.pop(0)
                li2.pop(0)
                matched = 1
                start = ''
                looping = False
                print(len(li1))
            else:
                if looping == False:
                    start = li2[0]
                    looping = True
                li2.append(li2.pop(0))
                left = li1[0]
                right = li2[0]
        if looping == True and start == right:
            print('Failure')
            failure = True
            break
        else:
            looping == True
            start = ''
        if len(li1) == 0:
            failurePrev = False
if failure == False:
    finalListStr = ''
    for i in finalList:
        #print(i[0] + ' - ' + i[4])
        finalListStr += i[0] + ' - ' + i[4] + '\n'
    client.messages.create(to=to_number, from_=from_number, body=finalListStr)
    print('Is this matching acceptable?')
    approval = input('Answer y/n: ')
    if(approval == 'y'):
        current_time = str(datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))
        fileName = 'CousinSecretSanta_' +current_time + '.csv'
        with open(fileName, 'w') as f:
            # using csv.writer method from CSV package
            write = csv.writer(f)
            write.writerows(finalList)

        '''for cousin in finalList:
           client.messages.create(to=cousin[2], from_=from_number, body='Hello ' + cousin[0] + ', for the Cousin Secret Santa, you have ' + cousin[4] + ' for Christmas'
                                                                     '\n\n'
                                                                     'The budget is a maximum $50'
                                                                     '\n\n'
                                                                     'This is what they want: ' + cousin[7])'''

        #test code; comment out in prod
        for cousin in finalList:
            print('Hello ' + cousin[0] + ' ' + cousin[2] + ', for the Cousin Secret Santa, you have ' + cousin[4] + ' for Christmas'
                                                                     '\n\n'
                                                                     'The budget is a maximum $50'
                                                                     '\n\n'
                                                                     'This is what they want: ' + cousin[7])
