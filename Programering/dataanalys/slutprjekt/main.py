import numpy as np # Importerar numpy, pandas och matplotlib
import pandas as pd
import matplotlib.pyplot as plt 

menyText = ''' 
Välkommen till mitt dataanalysprojekt.

1: Dagliga dödsfall.
2: Dödsfall hos åldersgrupp.
3: Mest drabbade regioner.
4. Smittfall Kön.
5. Dagliga smittfall bland regioner.
0: Avsluta.

Vilken data vill du se?
''' # Meny och inputmedelande

def validInput(inputMsg, errorMsg ): # Skapar en funktion med parametrarna inputMsg och errorMsg
    while True: # Oändelig loop
        try: 
            value = int(input(inputMsg)) # Försök att få en ordentlig input, om ja så avbryt loopen.
            break
        except: 
            print(errorMsg) # Om input är fel så printe felmedelande och låt användaren försöka igen.
    return value


def dailyDeaths(): # Definierar daily deaths
    
    df = pd.read_csv('assets/National_Daily_Deaths.csv') #Läser in National daily deaths.
    plt.plot(df['Date'], df['National_Daily_Deaths']) # Skapar ett linjediagram av datum och dagens dödsfall
    plt.title('Antalet dödsfall varje dag.') # Titel på grafen
    plt.xticks(df.Date[::30], rotation=35) # Ser till att bara var tretionde datum visar och roterar dem 35 grader.
    plt.ylabel('Dagliga dödsfall') # titel för y axel
    plt.xlabel('Datum') # titel för x axel
    plt.show() # Visar grafen

def ageGroup(): # Definierer åldergrupp
    df = pd.read_csv('assets/National_Total_Deaths_by_Age_Group.csv') # läser in national total deaths by age group
    plt.title('Totla smittfallen uppdelade efter åldersgrupp') # Titel för grafen
    plt.pie(df.Total_Cases, labels=df.Age_Group, autopct='%.2f') # skapar ett cirkeldiagram med varje åldergrupp. varje del visar gåldersgruppen och andel
    plt.show()


def regions100k(): # Definierer regions100k
    df = pd.read_csv('assets/Regional_totals_data.csv') # Läser in csv filen
    plt.title('Mest drabbade regioner \n Antal drabbade per 100k invånare') # Sätter titeln
    plt.bar(x=df.Region, height=df.Cases_per_100k_Pop, bottom=100) # Skapar ett stapeldiagram av regioner och cases per 100k inv.
    plt.xticks(rotation = 90) # Roterar regionernas namn 90 grader
    plt.show() # Visar grafen

def gender(): # Definierar gender.
    df = pd.read_csv('assets/Gender_Data.csv') # Läser in csv filen
    plt.bar(x = df.Gender, height= df.Total_Cases) # Skapar ett stapeldiagram av kön och antal fall
    plt.title('Antal smittade för varje kön') # Sätter titel
    plt.show() # Visar grafen

def regionalDailyCases(): # Definierer regional daily cases
      
    df = pd.read_csv('assets/Regional_Daily_Cases.csv') # Läser in csv filen
    date = df.Date # Date blir en lista av alla datum
    regions = df.columns[2:] # Regions blir en lista av alla lolumner efter 2
    for i in regions: # loopar igenom alla regioner
        plt.plot(date,df[i]) # Skaper ett linjediagram av regionen och datum
    plt.xlabel('Date') # Titel för x axeln
    plt.ylabel('Daily cases') # titel för y axeln
    plt.title('Daily cases for every region') # Titel för grafen
    plt.xticks(date[::30], rotation=35) # Visar bara var trettionde datum och roterar dem 35 grader
    plt.show() # Visar grafen
    # Kanske inte särsilt hjälpsam men grafen ser snygg ut


while True: # Oandelig loop
    command = validInput(menyText, 'Felaktigt kommando.') # Command blir validInputs output
    
    if command == 1: # Checkar alla tillåtna värden för command
        dailyDeaths() # Kör dailyDeaths()
    elif command == 2:
        ageGroup() # Kör ageGroup
    elif command == 3:
        regions100k() # Kör regions100k
    elif command == 4:
        gender() # kör gender
    elif command ==5:
        regionalDailyCases() # kör regionalDailyCases
    elif command == 0:
        break # Avslutar programmet
    else: # Annast visas felmedelande
        print('Du har angett ett felaktigt kommando.')


