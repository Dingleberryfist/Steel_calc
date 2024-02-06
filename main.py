print("This beam calculator assumes access to the book ´Teknisk Ståbi´ version 25."
      "\nThe document uses chapter 2, and the numerated formulas."
      "\nSupported formulas:"
      "\n2.3"
      "\n2.11"
      "\n2.15"
      "\n2.17")

formula = float(input("Formula: "))

if formula == 2.3:
    q = float(input("q load (kN): "))
    length = float(input("length (m): "))
    Reaction_A = 1 / 2 * q * length
    Reaction_B = Reaction_A
    M_max = 1 / 8 * q * length ** 2
    print(f"Reaction A: {Reaction_A} kN\nReaction B: {Reaction_B} kN\nMaximum moment: {M_max} kNm")
elif formula == 2.11:
    Q = float(input("q load (kN): "))
    length = float(input("length (m): "))
    Reaction_A = 1 / 2 * Q
    Reaction_B = Reaction_A
    M_max = 1 / 4 * Q * length
    print(f"Reaction A: {Reaction_A} kN\nReaction B: {Reaction_B} kN\nMaximum moment: {M_max} kNm")
elif formula == 2.15:
    q = float(input("q load (kN): "))
    length = float(input("length (m): "))
    Reaction_B = q * length
    Moment_B = -(1 / 2) * q * length ** 2
    print(f"Reaction B: {Reaction_B} kN\nMaximum moment: {Moment_B} kNm")
elif formula == 2.17:
    Q = float(input("q load (kN): "))
    length = float(input("length (m): "))
    Reaction_B = Q
    Moment_B = Q * length
    print(f"Reaction B: {Reaction_B} kN\nMaximum moment: {Moment_B} kNm")

Elasticity_YN = input("Is modulus of elasticity different from 200.000MPa? (Yes: Y/No: N): ")
if Elasticity_YN == "Y":
    Elasticity = float(input("Modulus of elasticity: "))
else:
    Elasticity = 200000
