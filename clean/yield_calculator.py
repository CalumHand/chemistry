print

mass_SM = float(raw_input("Mass of limiting reagent used in grams: "))
gfm_SM = float(raw_input("G.F.M of limiting reagent in grams: "))
mol_SM = mass_SM / gfm_SM
print

SM_ratio = float(raw_input("Stoicheometric coefficient of limiting reagent: "))
TM_ratio = float(raw_input("Stoicheometric coefficient of target molecule: "))
ratio = TM_ratio / SM_ratio
print

gfm_TM = float(raw_input("G.F.M of target molecule in grams: "))

one_hundred_percent_yield = mol_SM * ratio * gfm_TM

TM_mass_collected = float(raw_input("Mass of Target molecule collected in grams: "))

observed_yield = (TM_mass_collected / one_hundred_percent_yield) * 100
observed_yield = str(observed_yield)
print "\nThe percentage yield for the target molecule based on the limiting\
 reagent is " + observed_yield + " %\n"
