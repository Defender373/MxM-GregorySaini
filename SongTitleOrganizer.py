#D:\MxM-Project
afile = 'D:\\MxM-Project\\songList.txt'
outputfile = 'D:\\MxM-Project\\SongCSV.txt'
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
    song = songTitle[x] + "," + singer[x] + "," + album[x] + "\n"
    #print(song)
    output.write(song)



#for line in f:
#    print(line)

