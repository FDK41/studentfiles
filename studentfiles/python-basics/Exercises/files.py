f = open("1880-boys.txt")  # Open 1880-boys.txt and assign result to f.
boys = f.read()  # Read contents of file into content variable.
print(boys)  # Print content.
f.close()  # Close the file.

f = open("1880-girls.txt")  # Open 1880-girls.txt and assign result to f.
girls = f.read()  # Read contents of file into content variable.
print(girls)  # Print content.
f.close()  # Close the file.

# nieuwe regel toevoegen
boys = "\n" + boys 

# wegschrijven jongensnamen in nieuw bestand
f2 = open ("1880-all.txt", "w")
f2.write(boys)

# wegschrijven meisjesnamen in nieuw bestand
f2 = open ("1880-all.txt", "a")
f2.write(girls)
