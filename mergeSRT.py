import os,sys

try:
    srt1 = open("D:/Users/Crystal/Documents/GitHub/PyPractice/srt_en.srt", "r")
except IOError:
    print "The file don't exist, Please double check!"
    exit()
print 'The file mode is ',srt1.mode
print 'The file name is ',srt1.name
P = srt1.tell()
print 'the postion is %d' %(P)

try:
    srt2 = open("D:/Users/Crystal/Documents/GitHub/PyPractice/srt_ch.srt", "r")
except IOError:
    print "The file don't exist, Please double check!"
    exit()
print 'The file mode is ',srt2.mode
print 'The file name is ',srt2.name
P = srt2.tell()
print 'the postion is %d' %(P)

srtout = open('D:/Users/Crystal/Documents/GitHub/PyPractice/srt_out.srt', 'w')

dict1, dict2 = {}, {}

for EachLine in srt2:
    try:
        key = int(EachLine)
    except:
        continue

    if key == 11:
        print key
    if key == 2:
        print key

    time = srt2.next()
    nextline = srt2.next()
    subtext = ''
    while not nextline == '\n':
        subtext += nextline
        try:
            nextline = srt2.next()
        except:
            break

    dict2[key]=(time, subtext)

for EachLine in srt1:
    try:
        key = int(EachLine)
    except:
        continue

    time = srt1.next()
    nextline = srt1.next()
    subtext = ''
    while not nextline == '\n':
        subtext += nextline
        try:
            nextline = srt1.next()
        except:
            break
    dict1[key]=(time, subtext)

    srtout.write(str(key)+'\n')
    srtout.write(dict1[key][0])
    srtout.write(dict1[key][1])
    try:
        srtout.write(dict2[key][1])
    except:
        pass
    srtout.write('\n')

srt2.close()
srt1.close()
srtout.close()
