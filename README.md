# Pokemon Type Predictor

This repo contains python code that predicts Pokemon types based on Pokemon base statistics. The base statistics includes the Attack, Defense, Special Attack, Special Defense and Speed of the corresponding Pokemon. This prediction algorithm uses Sklearn's Decision tree library to determine the Pokemon type base on statistics. 

Relevant Pokemon background information and terminology: 

* [Pokemon Base Stats](http://bulbapedia.bulbagarden.net/wiki/Base_stats)

* [Pokemon Types](http://bulbapedia.bulbagarden.net/wiki/Type)

# Purpose

The purpose is to see if there are any connections to Pokemon Bast Stats v. Pokemon Type. For the purposes of this program, secondary types are not considered. For example, Bulbasaur is Grass and Poison type. In this case, Bulbasaur is a Grass type for the purposes of this program. 

# Relevant Files

* Pokemon.csv - CSV file of Pokemon species and their corresponding stats. Source of the csv file can be found on Kaggle through [this link](https://www.kaggle.com/abcsds/pokemon) **Last Accessed: November 5, 2016**

* test_script.py - This serves as the main.py of the file. Basically this files selects a random row of the csv file and grabs the relevant information. 

* type_predict.py
