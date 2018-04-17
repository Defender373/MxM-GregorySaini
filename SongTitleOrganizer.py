afile = 'C:\\Users\\sainig\\Desktop\\Spring_2018_semester\\MxM\\MxM-GregorySaini\\songList.txt'
outputfile = 'C:\\Users\\sainig\\Desktop\\Spring_2018_semester\\MxM\\MxM-GregorySaini\\songFinal.txt'
f = open(afile, 'r')
output = open(outputfile, 'w')

#line = f.readline()

songTitle = []
singer = []
album = []



for line in f:
    group = line.split('\t')

    if group[0] not in songTitle:
        songTitle.append(group[0])
        singer.append(group[1])
        album.append(group[2])

    

    
print(len(songTitle))
#print(len(singer))
#print(len(album))

for x in range( len(songTitle)  ):
    song = songTitle[x] + "\t" + singer[x] + "\t" + album[x] + "\n"
    #print(song)
    output.write(song)



#for line in f:
#    print(line)

