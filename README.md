# Valorant_Agent_Suggest
A small Python program that recommends a Valorant agent based on the user's preferred playstyle using the Manhattan Distance algorithm.


Overview - 

Choosing an agent in Valorant can be difficult, especially for newer players who are unfamiliar with the different agents and their abilities.
This program attempts to simplify that decision by comparing the user's preferences with a dictionary of predefined agent statistics. It then recommends the agent whose attributes most closely match the user's selections.


How It Works - 

The program uses three attributes to determine the user's preferred playstyle:

Aggression – How aggressively the user prefers to play.

Teamplay – How much the user prefers to cooperate and support teammates.

Difficulty – The level of mechanical or strategic complexity the user is comfortable with.

Each agent in the dictionary has predefined values for these three attributes.
The program calculates the Manhattan Distance between the user's preferences and each agent's statistics.


The formula is:

[
D = |x_1-y_1| + |x_2-y_2| + |x_3-y_3|
]

The agent with the smallest calculated distance is selected as the closest match.


Technologies Used - 

Python

Manhattan Distance Algorithm

Dictionary-based data storage


Purpose - 

This project was created to experiment with algorithmic decision-making and apply mathematical concepts to a practical application inspired by Valorant.
