
def count15(num_hand):
    sum15 = 0
    for x1 in range (0,5):
        for x2 in range(x1+1,5):
            if num_hand[x1][0] + num_hand[x2][0] == 15:
                sum15 += 2
            for x3 in range(x2+1,5):
                if num_hand[x1][0] + num_hand[x2][0] + num_hand[x3][0] == 15:
                    sum15 += 2
                for x4 in range(x3+1,5):
                    if num_hand[x1][0] + num_hand[x2][0] + num_hand[x3][0] + num_hand[x4][0] == 15:
                        sum15 += 2
                    for x5 in range(x4+1,5):
                        if num_hand[x1][0] + num_hand[x2][0] + num_hand[x3][0] + num_hand[x4][0] + num_hand[x5][0] == 15:
                           sum15 += 2
    return(sum15)


def countxofakind(valuecount):
    sumofakind = 0
    for each in valuecount:
        if each == 2:
            sumofakind += 2
        if each == 3:
            sumofakind += 6
        if each == 4:
            sumofakind += 12
    return sumofakind

def countruns(valuecount):
    i = 0
    run = 0
    boollist=[]
    for each in valuecount:
        if each > 0:
            boollist.append(True)
        else:
            boollist.append(False)
    while i < 12:
         if boollist[i]:
             if boollist[(i+1) % 13] and boollist[(i+2) % 13] and boollist[(i+3) % 13 ] and boollist[(i+4) % 13]:
                run = 5
                return (run)
             elif boollist[(i+1) % 13] and boollist[(i+2) % 13] and boollist[(i+3) % 13 ]:
               # Check if this is a double run of 4
                if valuecount[i] + valuecount[(i+1) % 13] + valuecount[(i+2) % 13] + valuecount[(i+3) % 13] > 4:
                    run = 8
                else:
                    run = 4
                return (run)
             elif boollist[(i+1) % 13] and boollist[(i+2) % 13]:
                # Check if this is a double run of 3
                if valuecount[i] + valuecount[(i+1) % 13] + valuecount[(i+2) % 13] > 3:
                    run = 6
                else:
                    run = 3
                return(run)
             else:
                i += 1
         else:
            i += 1
    return(run)

        
def flush(hand):
    flushpoints = 0
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1]:
        flushpoints = 4
        if hand[3][1] == hand[4][1]:
            flushpoints = 5
    return(flushpoints)

def nobs(hand):
    nobpoints = 0
    for each in range (0,4):
        if hand[each][2] == 'j' and hand[each][1] == hand[4][1]:
            nobpoints = 1
    return(nobpoints)



def main():

    import sys
    hand=[]
    suite= {'c':0,'d':0,'h':0,'s':0}
    valuecount = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    # Notes about the above
    # hand is an array or tupples that contain each vaule of the cards to be counted
    # The tupples contain the following:
    #    point value of the card as an int, 
    #    the suite as a character (c for clubs, d for diamonds, h for hearts, s for spades),
    #    card name if face card other than ace as sting (j for jack, q for queen, k for king, x otherwise)
    #
    # suite is a dictionary that contains the suite as the key and the count of the suite as an integer
    #
    # valuecount is an array of 13 integers.  valuecount[0] is the total number of aces, valuecount[1] is the totatl number of 2's etc.

    
    for each in sys.argv[1:]:
        if each[:-1] == 'j' or each[:-1] == 'q' or each[:-1] == 'k':
            val = 10
            if each[:-1] == 'j':
               valuecount[10] += 1
               card = 'j'
            elif each[:-1] == 'q':
                valuecount[11] += 1
                card = 'q'
            elif each[:-1] == 'k':
                valuecount[12] += 1
                card = 'k'
        elif each[:-1] == 'a':
            val = 1
            valuecount[0] += 1
            card = 'a'
        elif each[:-1] == '0':
            val = 10
            valuecount[9] += 1
        else:
            val = int(each[:-1])
            valuecount[val-1] += 1
            card = 'x'
        hand.append((val,each[-1],card))
    #print(hand)

    # Count by suite
    for each in hand:
        if each[1] == 'c':
            suite['c'] += 1
        if each[1] == 'd':
            suite['d'] += 1
        if each[1] == 'h':
            suite['h'] += 1
        if each[1] =='s':
            suite['s'] += 1
 
    t15 =  count15(hand)
    txofakind = countxofakind(valuecount)
    trun = countruns(valuecount)
    tflush = flush(hand)
    if valuecount[10] > 0:
        nobpoints = nobs(hand)
    else:
        nobpoints = 0
    print("15's",t15)
    print("sum of a kind ",txofakind )
    print ("Runs", trun)
    print("Flush",tflush)
    print("nobs", nobpoints)
    print('TOTAL: ', t15 + txofakind + trun + tflush + nobpoints)


if __name__ == "__main__" :
    main()
