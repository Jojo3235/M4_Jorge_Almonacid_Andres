import pandas as pd

titulos = pd.read_csv('imdb_titulos.csv')
print(titulos.head())


elenco = pd.read_csv('imdb_elenco.csv')
print(elenco.head())

print(titulos.shape[0])
print(elenco.shape[0])

print(titulos.tail())

print(titulos[titulos["title"].str.contains('Dracula')])

print(titulos["title"].value_counts().head(10))

print(titulos[titulos["title"]=="Romeo and Juliet"].sort_values("year").head(1))

print(titulos[titulos["title"].str.contains("Exorcist")].sort_values("year").head())

print(titulos[titulos["year"]==1950].shape[0])

print(titulos[(titulos["year"]>=1950) & (titulos["year"]<=1959)].shape[0])

print(elenco[elenco["title"]=="The Godfather"]["name"].value_counts())

print(elenco[(elenco["title"]=="Dracula") & (elenco["year"]==1958)].sort_values("n"))

print(elenco[elenco["character"]=="Bruce Wayne"]["name"].value_counts())

print(elenco[elenco["name"]=="Robert De Niro"]["character"].value_counts())

print(elenco[(elenco["name"]=="Charlton Heston") & (elenco["n"]==1) & (elenco["year"]>=1960) & (elenco["year"]<=1969)].sort_values("year", ascending=False))

print(elenco[(elenco["type"]=="actor") & (elenco["year"]>=1950) & (elenco["year"]<=1959)].shape[0])

print(elenco[(elenco["type"]=="actress") & (elenco["year"]>=1950) & (elenco["year"]<=1959)].shape[0])