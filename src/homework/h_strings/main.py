from strings import get_hamming_distance, get_dna_complement

def main():
    running = True
    while running:    
        print("MAIN MENU")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")
        selection = input("Enter selection here: ")
        if selection == "1":
            print("")
            print("Hamming distance calculator")
            dna1 = input("Enter first DNA string: ")
            dna2 = input("Enter second DNA string: ")
            print("")
            valid_chars = set("TCGAtcga")
            if len(dna1)!=len(dna2):
                print("Error, DNA strings must be same length")
                print("")
            elif not all(ch in valid_chars for ch in dna1):
                    print("Error: First DNA string contains invalid characters.")
                    print("")
                    print("")
            elif not all(ch in valid_chars for ch in dna2):
                    print("Error: Second DNA string contains invalid characters.")
                    print("")
                    print("")
                
            else: 
                hamming_distance = get_hamming_distance(dna1, dna2)
                print(f"Hamming Distance: {hamming_distance}")
                print("")
                print("")

        elif selection == "2":
            print("")
            print("DNA compliment calculator")
            dna = input("Enter DNA string: ")
            print("")
            valid_chars = set("TCGAtcga")
            if not all(ch in valid_chars for ch in dna):
                    print("Error: DNA string contains invalid characters.")
                    print("")
            else:
                dna_compliment = get_dna_complement(dna)
                print(f"DNA compliment is: {dna_compliment}")
                print("")
                print("")
        elif selection == '3':
            print("Exiting the program.")
            break

        else:
            print("invalid entry, please select 1,2,or 3")    

if __name__ == '__main__':
    main()