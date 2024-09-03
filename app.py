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
                biudzetas.prideti_pajamu_irasa()
            case 2:
                biudzetas.prideti_islaidu_irasa()
            case 3:
                biudzetas.parodyti_ataskaita()
            case 4:
                print(biudzetas.gauti_balansa())
            case 0:
                print("Viso gero")
                break
