database = {}
for i in range(0,4001):
    database[i] = []

# C-H
for i in range(2900,3201):
    database[i].append("Alkyl             C-H stretch")
for i in range(2900,3201):
    database[i].append("Vinyl / Aryl      C-H stretch")
for i in range(3300,3501):
    database[i].append("Alkyne            C-H stretch")
for i in range(2900,3201):
    database[i].append("Aldehyde          C-H stretch     (two peaks)")
for i in range(2700,3001):
    database[i].append("Aldehyde          C-H stretch     (two peaks)")
for i in range(2810,3051):
    database[i].append("-O-Alkyl          C-H stretch     (sharp)")
for i in range(1220,1451):
    database[i].append("Alkyl             C-H IP bend     (Not Useful)")
for i in range(950,1251):
    database[i].append("Vinyl             C-H IP bend     (Not Useful)")
for i in range(700,901):
    database[i].append("Al C-H            C-H IP bend")
for i in range(730,771):
    database[i].append("Monosub aro ring  C-X oop bend    (Two bands)")
for i in range(690,711):
    database[i].append("Monosub aro ring  C-X oop bend    (Two bands)")
for i in range(735,776):
    database[i].append("Orthosub aro ring C-X/C-Y oop bend")
for i in range(750,811):
    database[i].append("Metasub aro ring  C-X/C-Y oop bend")
for i in range(800,861):
    database[i].append("Parasub aro ring  C-X/C-Y oop bend")


#O-H
for i in range(3200,3551): ###
    database[i].append("Alcohol/Phenol    O-H stretch    (Not H bonded)")
for i in range(3350,3451):
    database[i].append("Alcohol/Phenol    O-H stretch    (H bonded)")
for i in range(2500,3301):###
    database[i].append("Carboxylic acid   O-H dimer stretch (very broad)")


#C-O
for i in range(1050,1201):
    database[i].append("Alcohol           C-O stretch    (intense)")
for i in range(1060,1151):
    database[i].append("Ether             R-O-R stretch  (two bands)")
for i in range(1030,1271):
    database[i].append("Ether             Ar-O-R stretch  (intense)")
for i in range(1030,1121):
    database[i].append("Ether             Ar-O-R stretch  (weak)")
for i in range(1150,1251):
    database[i].append("Ether             Ar-O-Ar stretch  (two bands)")


#S-H
for i in range(2550,2951):
    database[i].append("                  S-H            (weak bands)")


# C-Hal
for i in range(1090,1111):
    database[i].append("Halogen           C-F stretch")
for i in range(700,901):
    database[i].append("Halogen           C-Cl stretch    (not normally detected)")
for i in range(500,751):
    database[i].append("Halogen           C-Br stretch   (not normally detected)")
# C-I doesnt show up


# N-H
for i in range(3300,3501):
    database[i].append("Primary amine     N-H stretch    (two bands)")
for i in range(1580,1651):
    database[i].append("Primary amine     N-H deformartion")
for i in range(3100,3301):
    database[i].append("Secondary amine   N-H stretch")
for i in range(1550,1651):
    database[i].append("Secondary amine   N-H deformation")


#C-N
for i in range(1020,1221):
    database[i].append("Alkyl             C-N stretch")
for i in range(1250,1361):
    database[i].append("Aryl              C-N stretch")


#C=O
for i in range(1700,1726):
    database[i].append("R-C=O-R           C=O stretch")
for i in range(1670,1601):
    database[i].append("R-C=O-Ar          C=O stretch")
for i in range(1640,1681):
    database[i].append("Ar-C=O-Ar         C=O stretch")
for i in range(1690,1711):
    database[i].append("1,2 diketones     C=O stretch     (usually only one band)")
for i in range(1615,1631):
    database[i].append("1,3 diketones     C=O stretch     (H bonding)")
for i in range(1710,1731):
    database[i].append("R-CHO             C=O stretch")
for i in range(1670,1701):
    database[i].append("Ar-CHO            C=O stretch")
for i in range(1700,1726):
    database[i].append("RCOOH             C=O stretch")
for i in range(1680,1701):
    database[i].append("ArCOOH            C=O stretch")
for i in range(1690,1716):
    database[i].append("a/B unsat         C=O stretch")
for i in range(1550,1621):
    database[i].append("Salts             C=O stretch")
for i in range(1725,1746):
    database[i].append("RCOOR             C=O stretch")
for i in range(1700,1726):
    database[i].append("ArCOOR            C=O stretch")
for i in range(1750,1781):
    database[i].append("RCOOAr            C=O stretch")
for i in range(1740,1761):
    database[i].append("ArCOOAr           C=O stretch")
for i in range(1750,1801):
    database[i].append("RCOCl             C=O stretch")
for i in range(1760,1786):
    database[i].append("ArCOCl            C=O stretch")
for i in range(1780,1821):
    database[i].append("Acyclic Anhydride   C=0 stretch     (two bands)")
for i in range(1740,1761):
    database[i].append("Acyclic Anhydride   C=0 stretch     (two bands)")
for i in range(1810,1851):
    database[i].append("ArCOCl  Anhydride   C=0 stretch     (two bands)")
for i in range(1740,1781):
    database[i].append("ArCOCl  Anhydride   C=0 stretch     (two bands)")


# Amides
for i in range(1640,1661):
    database[i].append("RCONH2            C=O stretch")
for i in range(1630,1681):
    database[i].append("RCONHR            C=O stretch")
for i in range(1630,1681):
    database[i].append("RCONR2            C=O stretch")
for i in range(1620,1651):
    database[i].append("RCONH2            N-H deformation")
for i in range(1515,1571):
    database[i].append("RCONHR            N-H deformation")
for i in range(1400,1401):
    database[i].append("RCONH2            C=N stretch")
for i in range(1290,1291):
    database[i].append("RCONHR            C=N stretc")
# RCONR2 doesnt show up for C=N



#C=N
for i in range(1630,1691):
    database[i].append("                  C=N stretch        (weak bands)")


#C=C
for i in range(1640,1675):
    database[i].append("RCH=CH2           C=C stretch         (variable intensity)")
for i in range(1620,1641):
    database[i].append("RCH=CH-CH=CH2     C=C stretch         (variable intensity)")
for i in range(1625,1636):
    database[i].append("PhCH=CH2          C=C stretch         (variable intensity)")
for i in range(1580,1661):
    database[i].append("C=C-C=O           C=C stretch         (variable intensity)")
for i in range(1595,1606):
    database[i].append("C=C-C=O           C=C stretch         (Two bands)")
for i in range(1495,1505):
    database[i].append("Aromatic          C=C stretch         (variable intensity)")


# N=O
for i in range(1500,1601):
    database[i].append("R-N=O / Ar-N=O    N=O stretch")
for i in range(1500,1566):
    database[i].append("R-NO2 / Ar-NO2    N=O stretch       (Two bands)")
for i in range(1335,1386):
    database[i].append("R-NO2 / Ar-NO2    N=O stretch       (Two bands)")


# C=/C
for i in range(2190,2261):
    database[i].append("RC=/CR            C=/C stretch")
for i in range(2100,2141):
    database[i].append("RC=/CH            C=/C stretch")

# S=O
for i in range(1300,1351):
    database[i].append("RSO2R             S=O stretch")
for i in range(1140,1171):
    database[i].append("RSO2R             S=O stretch")
for i in range(1150,1211):
    database[i].append("RSO3H             S=O stretch")
for i in range(1030,1061):
    database[i].append("RSO3H             S=O stretch")
for i in range(1330,1371):
    database[i].append("RSO2H             S=O stretch")
for i in range(1160,1181):
    database[i].append("RSO2H             S=O stretch")
for i in range(1030,1071):
    database[i].append("R2S=O             S=O stretch")


# C=/N
for i in range(2205,2261):
    database[i].append("RC=/N             C=/N stretch")
for i in range(2115,2146):
    database[i].append("RN=/C             C=/N stretch")
for i in range(2240,2276):
    database[i].append("N=C=O             C=/N stretch")

############################################################################

peaks = []
while True :
    wavenumber = raw_input("Enter a wavenumber, type run to start: ")
    if wavenumber == 'run':
        break
    else:
        if wavenumber.isalpha() or len(wavenumber)==0:
            print "\nThat isn't a wavenumber ya plonker, try again...\n "
        else:
            wavenumber = int(wavenumber)
            peaks.append(wavenumber)
peaks.sort()
peaks.reverse()

print "\nInfra Red analysis predicts that"

def compiler():
    for peak in peaks:
        for reference in database:
            if reference == peak:
                print "\n" + str(peak) + " corresponds to data entry "
                print str(reference) + " cm^-1 :"
                print "||" + "\n|| ".join(database[reference])
compiler()
