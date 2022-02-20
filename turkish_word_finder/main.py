import random
from itertools import count, permutations
from turtle import st
from word_list import turkish_words

def word_finder():

    count = int(input("Girilecek harf sayısını giriniz:"))

    letter_list = []
    founded = []

    for i in range(count):
        letter_list.append(str(input("")))

    
    while 3 <= count:

        for perm in permutations(letter_list, count):
            x = ("".join(perm))
            for all in x:
                founded.append(x)

        count = count -1

    sorted_list = sorted((set(founded).intersection(turkish_words)), key =len)

    if set(founded).intersection(turkish_words):
        print("Bu harfler ile", sorted_list,"yazabilirsin")

    else:
        print("Bu harfler ile kelime yazamazsın")


word_finder()


