dict2 = {}                  # created an empty dictionary
for i in range(0,4001):     # gave it 4000 key value pairs each key is a number
    dict2[i] = []           # from 0-4000 and each value is an empty list


# lines 10  through to  208  are literally just appending the lists dependant
# on the wavenumber of the particular bond

# C-H
for i in range(3000,3001):
    dict2[i].append("Alkyl             C-H stretch")
for i in range(3000,3001):
    dict2[i].append("Vinyl / Aryl      C-H stretch")
for i in range(3300,3301):
    dict2[i].append("Alkyne            C-H stretch")
for i in range(2900,2901):
    dict2[i].append("Aldehyde          C-H stretch     (two peaks)")
for i in range(2700,2701):
    dict2[i].append("Aldehyde          C-H stretch     (two peaks)")
for i in range(2810,2851):
    dict2[i].append("-O-Alkyl          C-H stretch     (sharp)")
for i in range(1220,1451):
    dict2[i].append("Alkyl             C-H IP bend     (Not Useful)")
for i in range(950,1251):
    dict2[i].append("Vinyl             C-H IP bend     (Not Useful)")
for i in range(700,901):
    dict2[i].append("Al C-H            C-H IP bend")
for i in range(730,771):
    dict2[i].append("Monosub aro ring  C-X oop bend    (Two bands)")
for i in range(690,711):
    dict2[i].append("Monosub aro ring  C-X oop bend    (Two bands)")
for i in range(735,776):
    dict2[i].append("Orthosub aro ring  C-X/C-Y oop bend")
for i in range(750,811):
    dict2[i].append("Metasub aro ring  C-X/C-Y oop bend")
for i in range(800,861):
    dict2[i].append("Parasub aro ring  C-X/C-Y oop bend")


#O-H
for i in range(3600,3601):
    dict2[i].append("Alcohol/Phenol    O-H stretch    (Not H bonded)")
for i in range(3400,3401):
    dict2[i].append("Alcohol/Phenol    O-H stretch    (H bonded)")
for i in range(2500,3301):
    dict2[i].append("Carboxylic acid   O-H dimer stretch (very broad)")


#C-O
for i in range(1050,1201):
    dict2[i].append("Alcohol           C-O stretch    (intense)")
for i in range(1060,1151):
    dict2[i].append("Ether             R-O-R stretch  (two bands)")
for i in range(1030,1271):
    dict2[i].append("Ether             Ar-O-R stretch  (intense)")
for i in range(1030,1121):
    dict2[i].append("Ether             Ar-O-R stretch  (weak)")
for i in range(1150,1251):
    dict2[i].append("Ether             Ar-O-Ar stretch  (two bands)")


#S-H
for i in range(2550,2951):
    dict2[i].append("                  S-H            (weak bands)")


# C-Hal
for i in range(1090,1111):
    dict2[i].append("Halogen           C-F stretch")
for i in range(700,901):
    dict2[i].append("Halogen           C-Cl stretch    (not normally detected)")
for i in range(500,751):
    dict2[i].append("Halogen           C-Br stretch   (not normally detected)")
# C-I doesnt show up


# N-H
for i in range(3300,3501):
    dict2[i].append("Primary amine     N-H stretch    (two bands)")
for i in range(1580,1651):
    dict2[i].append("Primary amine     N-H deformartion")
for i in range(3100,3301):
    dict2[i].append("Secondary amine   N-H stretch")
for i in range(1550,1651):
    dict2[i].append("Secondary amine   N-H deformation")


#C-N
for i in range(1020,1221):
    dict2[i].append("Alkyl             C-N stretch")
for i in range(1250,1361):
    dict2[i].append("Aryl             C-N stretch")


#C=O
for i in range(1700,1726):
    dict2[i].append("R-C=O-R          C=O stretch")
for i in range(1670,1601):
    dict2[i].append("R-C=O-Ar         C=O stretch")
for i in range(1640,1681):
    dict2[i].append("Ar-C=O-Ar        C=O stretch")
for i in range(1690,1711):
    dict2[i].append("1,2 diketones    C=O stretch     (usually only one band)")
for i in range(1615,1631):
    dict2[i].append("1,3 diketones    C=O stretch     (H bonding)")
for i in range(1710,1731):
    dict2[i].append("R-CHO            C=O stretch")
for i in range(1670,1701):
    dict2[i].append("Ar-CHO           C=O stretch")
for i in range(1700,1726):
    dict2[i].append("RCOOH            C=O stretch")
for i in range(1680,1701):
    dict2[i].append("ArCOOH           C=O stretch")
for i in range(1690,1716):
    dict2[i].append("a/B unsat        C=O stretch")
for i in range(1550,1621):
    dict2[i].append("Salts            C=O stretch")
for i in range(1725,1746):
    dict2[i].append("RCOOR            C=O stretch")
for i in range(1700,1726):
    dict2[i].append("ArCOOR           C=O stretch")
for i in range(1750,1781):
    dict2[i].append("RCOOAr           C=O stretch")
for i in range(1740,1761):
    dict2[i].append("ArCOOAr          C=O stretch")
for i in range(1750,1801):
    dict2[i].append("RCOCl            C=O stretch")
for i in range(1760,1786):
    dict2[i].append("ArCOCl           C=O stretch")
for i in range(1780,1821):
    dict2[i].append("Acyclic Anhydride   C=0 stretch     (two bands)")
for i in range(1740,1761):
    dict2[i].append("Acyclic Anhydride   C=0 stretch     (two bands)")
for i in range(1810,1851):
    dict2[i].append("ArCOCl  Anhydride   C=0 stretch     (two bands)")
for i in range(1740,1781):
    dict2[i].append("ArCOCl  Anhydride   C=0 stretch     (two bands)")


# Amides
for i in range(1640,1661):
    dict2[i].append("RCONH2           C=O stretch")
for i in range(1630,1681):
    dict2[i].append("RCONHR           C=O stretch")
for i in range(1630,1681):
    dict2[i].append("RCONR2           C=O stretch")
for i in range(1620,1651):
    dict2[i].append("RCONH2           N-H deformation")
for i in range(1515,1571):
    dict2[i].append("RCONHR           N-H deformation")
for i in range(1400,1401):
    dict2[i].append("RCONH2           C=N stretch")
for i in range(1290,1291):
    dict2[i].append("RCONHR           C=N stretc")
# RCONR2 doesnt show up for C=N



#C=N
for i in range(1630,1691):
    dict2[i].append("                C=N stretch        (weak bands)")


#C=C
for i in range(1640,1675):
    dict2[i].append("RCH=CH2        C=C stretch         (variable intensity)")
for i in range(1620,1641):
    dict2[i].append("RCH=CH-CH=CH2  C=C stretch         (variable intensity)")
for i in range(1625,1636):
    dict2[i].append("PhCH=CH2       C=C stretch         (variable intensity)")
for i in range(1580,1661):
    dict2[i].append("C=C-C=O        C=C stretch         (variable intensity)")
for i in range(1595,1606):
    dict2[i].append("C=C-C=O        C=C stretch         (Two bands)")
for i in range(1495,1505):
    dict2[i].append("Aromatic        C=C stretch         (variable intensity)")


# N=O
for i in range(1500,1601):
    dict2[i].append("R-N=O / Ar-N=O    N=O stretch")
for i in range(1500,1566):
    dict2[i].append("R-NO2 / Ar-NO2    N=O stretch       (Two bands)")
for i in range(1335,1386):
    dict2[i].append("R-NO2 / Ar-NO2    N=O stretch       (Two bands)")


# C=/C
for i in range(2190,2261):
    dict2[i].append("RC=/CR            C=/C stretch")
for i in range(2100,2141):
    dict2[i].append("RC=/CH            C=/C stretch")

# S=O
for i in range(1300,1351):
    dict2[i].append("RSO2R             S=O stretch")
for i in range(1140,1171):
    dict2[i].append("RSO2R             S=O stretch")
for i in range(1150,1211):
    dict2[i].append("RSO3H             S=O stretch")
for i in range(1030,1061):
    dict2[i].append("RSO3H             S=O stretch")
for i in range(1330,1371):
    dict2[i].append("RSO2H             S=O stretch")
for i in range(1160,1181):
    dict2[i].append("RSO2H             S=O stretch")
for i in range(1030,1071):
    dict2[i].append("R2S=O             S=O stretch")


# C=/N
for i in range(2205,2261):
    dict2[i].append("RC=/N             C=/N stretch")
for i in range(2115,2146):
    dict2[i].append("RN=/C             C=/N stretch")
for i in range(2240,2276):
    dict2[i].append("N=C=O             C=/N stretch")



# here another empty list was created to store user inputted wavenumbers
peaks = []
while 1<4:  # while loop just to allow as many entrys as needed
    frequency = raw_input("Enter a wavenumber, type run to start: ")
    if frequency == 'run':
        break  # i.e. if input is run the program then the while loop stops
    else:
        frequency = int(frequency) # if input is a number then gets converted to int
        peaks.append(frequency)   # and appended to the empty list peaks.
peaks.sort()                      # sort it because why the hell not
peaks.reverse()
# this will give it back highest wavenumber first (more useful than 800 etc)

for peak in peaks:     # for every inputted peak (stored in the list)
    for key in dict2:  # it will be checked against every key in the now appended dictionary
        if key == peak: # if the peak is equal to a key
            print "\n",peak, "corresponds to "   #
            print key,"cm^-1 :",                #
            print "||","\n|| ".join(dict2[key])                     # prints various stuff
