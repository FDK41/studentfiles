import math 

#input 

aantal_mensen = 5
aantal_stukken = 2.5
aantal_stukken_pizza = 8

# Berekening gegevens

totaal_benodigde_stukken = aantal_mensen * aantal_stukken
benodigde_pizzas = math.ceil(totaal_aantal_pizza)  /  aantal_stukken_pizza

overgebleven_stukken = (benodigde pizza *aantal_stukken_pizza) - totaal_benodigde_stukken

totaal_aantal_pizza = totaal_benodigde_stukken / aantal_stukken_pizza

# output

print("je hebt",totaal_benodigde_stukken / aantal_stukken_pizza, "pizza's nodig om", aantal_mensen,"mensen te voeden")

print("dit zijn dus") 
print(math.ceil(totaal_aantal_pizza % aantal_stukken_pizza))
print("hele pizza's")
print("je hebt dus", overgebleven_stukken, "over")



# Hoeveel mensen eten? 5
# Hoeveel stukken per persoon? 2.5
# Hoeveel stukken per pizza? 8
# Je hebt 2 pizza's nodig om 5 mensen te voeden.
# Er zullen nog 3.5 stukken overblijven
# Hoeveel mensen eten? 25
# Hoeveel stukken per persoon? 2
# Hoeveel stukken per pizza? 8
# Je hebt 7 pizza's nodig om 25 mensen te voeden.
# Er zullen nog 6.0 stukken overblijven