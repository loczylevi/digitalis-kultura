import random
print(f"""Milyen műveletet szeretne gyakorolni?

    1. Összeadás
    2. Kivonás
    3. Szorzás """)

valasz = int(input("Választás (1-3): "))

db = 0
ok = 0

while ok < 5:
    db += 1
    a = random.randint(1,10)
    b = random.randint(1,10)
    if valasz == 1:
        d = a + b
        c = int(input(f"{a}+{b} = "))
    elif valasz == 2:
        d = a - b
        c = int(input(f"{a}-{b} = "))
    elif valasz == 3:
        d = a * b
        c = int(input(f"{a}*{b} = "))
        
    if c == d:
        ok += 1
        print("Helyes!")
    else:
        print("Hibás!")
        
print(f"Gratulálunk!\nSikerült {ok} helyes műveletet elvégezni {db} próbálkozásból.")
