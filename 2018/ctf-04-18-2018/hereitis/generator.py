flag = 'utflag{more_than_meets_the_eye}'

def appendChar(index, character):
    text = "You blocks, you stones, you worse than senseless things! O you hard hearts, you cruel men of Rome, Knew you not Pompey? Many a time and oft Have you climb'd up to walls and battlements, To towers and windows, yea, to chimney-tops, Your infants in your arms, and there have sat The live-long day, with patient expectation, To see great Pompey pass the streets of Rome: And when you saw his chariot but appear, Have you not made an universal shout, That Tiber trembled underneath her banks, To hear the replication of your sounds Made in her concave shores? And do you now put on your best attire? And do you now cull out a holiday? And do you now strew flowers in his way That comes in triumph over Pompey's blood? Be gone! Run to your houses, fall upon your knees, Pray to the gods to intermit the plague That needs must light on this ingratitude.You blocks, you stones, you worse than senseless things! O you hard hearts, you cruel men of Rome, Knew you not Pompey? Many a time and oft Have you climb'd up to walls and battlements, To towers and windows, yea, to chimney-tops, Your infants in your arms, and there have sat The live-long day, with patient expectation, To see great Pompey pass the streets of Rome: And when you saw his chariot but appear, Have you not made an universal shout, That Tiber trembled underneath her banks, To hear the replication of your sounds Made in her concave shores? And do you now put on your best attire? And do you now cull out a holiday? And do you now strew flowers in his way That comes in triumph over Pompey's blood? Be gone! Run to your houses, fall upon your knees, Pray to the gods to intermit the plague That needs must light on this ingratitude."

    while text[index] == ' ':
        index += 1
    return (character + text[index], index + 1)

index = 0
output = ""

for char in flag:
    index = appendChar(index, ' ')[1]
    output += appendChar(index, ' ')[0]
    index = appendChar(index, ' ')[1]
    output += appendChar(index, ' ')[0]
    index = appendChar(index, ' ')[1]
    output += appendChar(index, ' ')[0]
    for binny in bin(ord(char))[2:]:
        if binny == '1':
            index = appendChar(index, '\t')[1]
            output += appendChar(index, '\t')[0]
        if binny == '0':
            index = appendChar(index, ' ')[1]
            output += appendChar(index, ' ')[0]
    index = appendChar(index, '\n')[1]
    output += appendChar(index, '\n')[0]
    index = appendChar(index, '\t')[1]
    output += appendChar(index, '\t')[0]
    index = appendChar(index, '\n')[1]
    output += appendChar(index, '\n')[0]
    index = appendChar(index, ' ')[1]
    output += appendChar(index, ' ')[0]
    index = appendChar(index, ' ')[1]
    output += appendChar(index, ' ')[0]


print output
