def main():
    mass = int(input("What is the mass(kg)? "))
    emc2(mass)

def emc2(mass):
    energy = mass * pow(300000000, 2)
    print(energy)

main()
