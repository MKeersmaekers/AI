# %% [markdown]
# ## Task 1 Cryptarithmetic Puzzle
# 
# Milan Keersmaekers
# 
# 06/10/2023
# 
# # Inleiding
# 
# In deze taak is het de bedoeling dat ik een cryptarithmetic puzzle maak waarbij het de bedoeling is dat de gebruiker zelf de woorden ingeeft en dat de applicatie op basis daarvan de correcte waarden voor elk letter uitzoekt. 
# 
# Ik ben gestart met de oefeningen hierrond opnieuw te maken en de code zo goed mogelijk te begrijpen, vervolgens heb ik de oplossingen hiervan gebruikt om de basis te leggen voor deze applicatie. Het hard gecodeerde gedeelte heb ik weg gedaan en ben dan beginnen nadenken hoe ik de user input kan omzetten in mijn code. Het grootste obstakel voor mij was de constraint_addition functie, hiervoor heb ik de hulp van openAI gebruikt om mij terug uit te leggen hoe ik dit kan oplossen met het gebruik van een dictionary. 
# 
# # GenAI Tools
# 
# Ik heb gebruik gemaakt van openAI
# 
# Dit is de prompt die gebruikte om de constraint_addition functie te updaten:
# 
# from simpleai.search import CspProblem, backtrack
# 
# word1 = input("Enter the first word: ").upper()
# word2 = input("Enter the second word: ").upper()
# result = input("Enter the result word: ").upper()
# 
# variables = list(set(word1 + word2 + result))
# 
# domains = {char: (list(range(1, 10)) if char == word1[0] or char == word2[0] or char == result[0] else list(range(10))) for char in variables}
# 
# def constraint_unique(variables, values):
#     return len(values) == len(set(values))
# 
# def constraint_addition(variables, values):
#     word1_value = int(str(values[0]) + str(values[1]))
#     word2_value = int(str(values[2]))
#     result_value = int(str(values[0]) + str(values[0]) + str(values[0]))
#     return word1_value + word2_value == result_value
# 
# 
# constraints = [
#     (variables, constraint_unique),
#     (variables, constraint_addition),
# ]
# 
# problem = CspProblem(variables, domains, constraints)
# 
# output = backtrack(problem)
# print('\nSolutions:', output) how do i update the constraint_addition function so that every character in the word is given a value?
# 
# # Code
# 
# Uitleg van de code heb ik in de comments erbij gezet

# %%
import streamlit as st
from simpleai.search import CspProblem, backtrack

st.title("Cryptarithmetic Puzzle Solver")

# Dit vraagt de gebruiker voor de twee woorden die opgeteld worden, en welk woord het resultaat moet zijn. Dit wordt ook in uppercase gezet
word1 = st.text_input("Enter the first word: ").upper()
word2 = st.text_input("Enter the second word: ").upper()
result = st.text_input("Enter the result word: ").upper()

# Met de set halen we de unieke characters uit de woorden en zetten deze in een list
variables = list(set(word1 + word2 + result))

# Hiermee wordt elk character in variables een list gegeven met een range van 1 tot 10 wanneer het character de eerste letter is van het woord(zodat er geen leading zeros zijn)
# en 0 tot 10 voor de andere characters, en dit staat dan in een dictionary
domains = {char: (list(range(1, 10)) if char == word1[0] or char == word2[0] or char == result[0] else list(range(10))) for char in variables}

# Dit checkt de variabelen of ze uniek zijn, als dit het geval is returned dit true
def constraint_unique(variables, values):
    return len(values) == len(set(values))

# Er wordt voor elk character van het woord de value uit de dictionary gehaald en zet dit om in
# een string, deze strings worden aan elkaar geplakt en omgezet in een integer
def constraint_addition(variables, values):
    word1_value = int("".join(str(values[variables.index(char)]) for char in word1))
    word2_value = int("".join(str(values[variables.index(char)]) for char in word2))
    result_value = int("".join(str(values[variables.index(char)]) for char in result))
    return word1_value + word2_value == result_value


# Dit zijn de nodige constraints die op de variabelen moeten worden toegepast
constraints = [
    (variables, constraint_unique),
    (variables, constraint_addition),
]

# Calculeert de probleemstelling
problem = CspProblem(variables, domains, constraints)

# Geeft de oplossing
output = backtrack(problem)

# Originele puzzel
st.write("The puzzle: ")
st.write(f"{word1} + {word2} = {result}")

# Resultaat
st.write("\nSolutions:", output)

