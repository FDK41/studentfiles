import math

#
# invoer gegevens
#
aantal_mensen = int(input("Hoeveel mensen eten? "))
aantal_stukken = float(input("Hoeveel stukken per persoon? "))
aantal_stukken_in_pizza = int(input("Hoeveel stukken per pizza? "))
#
# berekening gegevens
#
totaal_benodigde_stukken = aantal_mensen * aantal_stukken
benodigde_pizzas = math.ceil(totaal_benodigde_stukken / aantal_stukken_in_pizza)
overgebleven_stukken = (benodigde_pizzas * aantal_stukken_in_pizza) - totaal_benodigde_stukken

#
# console output
#
print("Je hebt", benodigde_pizzas ,"pizza's nodig om", aantal_mensen ,"mensen te voeden." )
print('Er zullen nog', overgebleven_stukken ,'stukken overblijven')


def main()
    gegevens_invoer()
    bereken_aantal_pizzas()
    output ()

main()
