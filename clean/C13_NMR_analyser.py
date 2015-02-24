# Runs the exact same as the IR analyser just with
# a different database


database = {}
for i in range(0,230):
    database[i] = []

for i in range(201,229):
    database[i].append("    >C=O        Ketone")
for i in range(182,209):
    database[i].append("    >C=O        Aldehyde")
for i in range(171,184):
    database[i].append("    >C=O        Acid")
for i in range(159,176):
    database[i].append("    >C=O        Ester / Amide")
for i in range(189,203):
    database[i].append("    >C=S        Thioketone")
for i in range(144,162):
    database[i].append("    >C=N-       Azomethine")
for i in range(117,125):
    database[i].append("    >C=/N       Nitrile")
for i in range(144,154):
    database[i].append("    >C=N        Heteraromatic")
for i in range(104,144):
    database[i].append("    >C=C<       Alkene")
for i in range(112,137):
    database[i].append("    >C=C<       Aromatic")
for i in range(115,140):
    database[i].append("    >C=C<       Heteroaromatic")
for i in range(75,93):
    database[i].append("    >C=/C-      Alkyne")
for i in range(29,53):
    database[i].append("    ->C-C<-     Quaternity")
for i in range(73,84):
    database[i].append("    ->C-O-")
for i in range(61,77):
    database[i].append("    ->C-N<")
for i in range(53,71):
    database[i].append("    ->C-S-")
for i in range(35,79):
    database[i].append("    ->C-Halogen")
for i in range(32,61):
    database[i].append("    >CH-C<-     Tertiary")
for i in range(65,78):
    database[i].append("    >C-O<-")
for i in range(57,69):
    database[i].append("    >C-N<")
for i in range(57,68):
    database[i].append("    >C-S-")
for i in range(32,65):
    database[i].append("    >C-Halogen")
for i in range(22,45):
    database[i].append("    >CH2-C<     Secondary")
for i in range(1,4,):
    database[i].append("    >CH2-O<     Cyclopropane")
for i in range(42,71):
    database[i].append("    -CH2-O-")
for i in range(43,59):
    database[i].append("    -CH2-N<")
for i in range(28,44):
    database[i].append("    -CH2-S-")
for i in range(2,40):
    database[i].append("    -CH2-Halogen")
for i in range(4,29):
    database[i].append("    CH3-C<-     Primary")
for i in range(49,49):
    database[i].append("    CH3-O-")
for i in range(12,43):
    database[i].append("    CH3-N<")
for i in range(10,19):
    database[i].append("    CH3-S-")
for i in range(2,29):
    database[i].append("    CH3-Halogen")



peaks = []
while 1<4 :
    ppm = raw_input("Enter a peak ppm, type run to start: ")
    if ppm == 'run':
        break
    else:
        ppm = int(ppm)
        peaks.append(ppm)
peaks.sort()
peaks.reverse()

print "\nCarbon 13 analysis predicts that"

for peak in peaks:
    for reference in database:
        if reference == peak:
            print "\n",peak,"ppm corresponds to data entry "
            print reference,"ppm :"
            print "||","\n|| ".join(database[reference])
