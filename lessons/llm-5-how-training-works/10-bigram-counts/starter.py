import math
import random

NAMES = """emma olivia ava sophia isabella mia amelia harper evelyn abigail emily ella elizabeth camila luna sofia avery mila aria scarlett penelope layla chloe victoria madison eleanor grace nora riley zoey hannah hazel lily ellie violet lillian zoe stella aurora natalie emilia everly leah aubrey willow addison lucy audrey bella nova brooklyn paisley savannah claire skylar isla genesis naomi elena caroline eliana anna maya valentina ruby kennedy ivy ariana aaliyah cora madelyn alice kinsley hailey gabriella allison gianna serenity samantha sarah autumn quinn eva piper sophie sadie delilah josephine nevaeh adeline arya emery lydia clara vivian madeline peyton julia rylee liam noah oliver elijah william james benjamin lucas henry alexander mason michael ethan daniel jacob logan jackson levi sebastian mateo jack owen theodore aiden samuel joseph john david wyatt matthew luke asher carter julian grayson leo jayden gabriel isaac lincoln anthony hudson dylan ezra thomas charles christopher jaxon maverick josiah isaiah andrew elias joshua nathan caleb ryan adrian miles eli nolan christian aaron cameron ezekiel colton luca landon hunter jonathan santiago axel easton cooper jeremiah angel roman connor jameson robert greyson jordan ian carson jaxson leonardo nicholas dominic austin everett brooks xavier kai jose parker adam jace wesley kayden silas""".split()
CHARS = "." + "abcdefghijklmnopqrstuvwxyz"
STOI = {ch: i for i, ch in enumerate(CHARS)}


def count_bigrams(names):
    N = [[0] * 27 for _ in range(27)]
    return N


def to_probs(N):
    P = []
    return P


def nll(P, names):
    return 0


def sample(P, rng):
    if len(P) != 27:
        return "?"
    out, i = "", 0
    while True:
        i = rng.choices(range(27), weights=P[i])[0]
        if i == 0:
            return out
        out += CHARS[i]


N = count_bigrams(NAMES)
print("count of 'a' followed by 'n':", N[STOI["a"]][STOI["n"]])
P = to_probs(N)
print(f"average NLL: {nll(P, NAMES):.3f}  (uniform guessing: {math.log(27):.3f})")
rng = random.Random(3)
print("samples:", [sample(P, rng) for _ in range(6)])
