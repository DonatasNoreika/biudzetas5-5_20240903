from biudzetas import Biudzetas

biudzetas = Biudzetas()

if __name__ == "__main__":
    while True:
        veiksmas = int(input("""
    1 - įvesti pajamas
    2 - įvesti išlaidas
    3 - parodyti žurnalą
    4 - parodyti balansą
    0 - išeiti
    """))
        match veiksmas:
            case 1:
                suma = abs(float(input("Suma: ")))
                siuntejas = input("Siuntėjas: ")
                info = input("Papildoma informacija: ")
                biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
            case 2:
                suma = abs(float(input("Suma: ")))
                atsiskaitymas = input("Atsiskaitymo būdas: ")
                isigyta = input("Įsigyta prekė/paslauga: ")
                biudzetas.prideti_islaidu_irasa(suma, atsiskaitymas, isigyta)
            case 3:
                biudzetas.parodyti_ataskaita()
            case 4:
                print(biudzetas.gauti_balansa())
            case 0:
                print("Viso gero")
                break
