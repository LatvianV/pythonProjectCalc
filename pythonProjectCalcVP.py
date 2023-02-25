import math

# Funkcija, lai aprēķinātu kuba virsmas laukumu
def cube_surface_area(side):
    return 6 * side**2

# Funkcija kuba tilpuma aprēķināšanai
def cube_volume(side):
    return side**3

# Funkcija, lai aprēķinātu cilindra virsmas laukumu
def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * height + 2 * math.pi * radius**2

# Funkcija cilindra tilpuma aprēķināšanai
def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

# Funkcija, lai aprēķinātu piramīdas virsmas laukumu
def pyramid_surface_area(base, height):
    slant_height = math.sqrt(base**2 + height**2)
    return base**2 + 2 * base * slant_height

# Funkcija piramīdas tilpuma aprēķināšanai
def pyramid_volume(base, height):
    return (1/3) * base**2 * height

# Funkcija prizmas virsmas laukuma aprēķināšanai
def prism_surface_area(base, height, sides):
    base_area = base * height
    side_area = sides * base * height
    return 2 * base_area + side_area

# Funkcija prizmas tilpuma aprēķināšanai
def prism_volume(base, height):
    return base * height

# Programmas izvēlne
def menu():
    print("Ģeometrijas kalkulators")
    print("1. Kubs")
    print("2. Cilindrs")
    print("3. Piramīda")
    print("4. Prizma")
    print("5. Izeja")

# Galvenā programmas cilpa
while True:

    menu()
    # Lūdziet lietotājam izvēlēties figūru
    choice = input("Ievadiet figūras numuru (1-5): ")
    
    # Pārbaudiet lietotāja izvēli
    if choice == '1':   # Kubs
        side = float(input("Ievadiet kuba malas garumu: "))
        print(f"Kuba virsmas laukums ir {cube_surface_area(side):.2f} kvadrātveida vienības.")
        print(f"Kuba tilpums ir {cube_volume(side):.2f} kubikvienības.")
    elif choice == '2': # Cilindrs
        radius = float(input("Ievadiet cilindra rādiusu: "))
        height = float(input("Ievadiet cilindra augstumu: "))
        print(f"Cilindra virsmas laukums ir {cylinder_surface_area(radius, height):.2f} kvadrātveida vienības.")
        print(f"Cilindra tilpums ir {cylinder_volume(radius, height):.2f} kubikvienības.")
    elif choice == '3': # Piramīda
        base = float(input("Ievadiet piramīdas pamatnes garumu: "))
        height = float(input("Ievadiet piramīdas augstumu: "))
        print(f"Piramīdas virsmas laukums ir {pyramid_surface_area(base, height):.2f} kvadrātveida vienības.")
        print(f"Piramīdas tilpums ir {pyramid_volume(base, height):.2f} kubikvienības.")
    elif choice == '4': # Prizma
        base = float(input("Ievadiet prizmas pamatnes garumu: "))
        height = float(input("Ievadiet prizmas augstumu: "))
        sides = int(input("Ievadiet prizmas malu skaitu: "))
        print(f"Prizmas virsmas laukums ir {prism_surface_area(base, height, sides):.2f} kvadrātveida vienības.")
        print(f"Prizmas tilpums ir {prism_volume(base, height):.2f} kubikvienības.")
    elif choice == '5': # Izeja
        print("Notiek iziešana no programmas...")
        break
    else:
        print("Nepareiza ievade")
