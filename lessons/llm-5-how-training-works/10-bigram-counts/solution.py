import math
import random

NAMES = """emma olivia ava sophia isabella mia amelia harper evelyn abigail emily ella elizabeth camila luna sofia avery mila aria scarlett penelope layla chloe victoria madison eleanor grace nora riley zoey hannah hazel lily ellie violet lillian zoe stella aurora natalie emilia everly leah aubrey willow addison lucy audrey bella nova brooklyn paisley savannah claire skylar isla genesis naomi elena caroline eliana anna maya valentina ruby kennedy ivy ariana aaliyah cora madelyn alice kinsley hailey gabriella allison gianna serenity samantha sarah autumn quinn eva piper sophie sadie delilah josephine nevaeh adeline arya emery lydia clara vivian madeline peyton julia rylee liam noah oliver elijah william james benjamin lucas henry alexander mason michael ethan daniel jacob logan jackson levi sebastian mateo jack owen theodore aiden samuel joseph john david wyatt matthew luke asher carter julian grayson leo jayden gabriel isaac lincoln anthony hudson dylan ezra thomas charles christopher jaxon maverick josiah isaiah andrew elias joshua nathan caleb ryan adrian miles eli nolan christian aaron cameron ezekiel colton luca landon hunter jonathan santiago axel easton cooper jeremiah angel roman connor jameson robert greyson jordan ian carson jaxson leonardo nicholas dominic austin everett brooks xavier kai jose parker adam jace wesley kayden silas""".split()
CHARS = "." + "abcdefghijklmnopqrstuvwxyz"
STOI = {}
for i in range(len(CHARS)):
    STOI[CHARS[i]] = i


def count_bigrams(names):
    N = []
    for i in range(27):
        N.append([0] * 27)
    for name in names:
        s = "." + name + "."
        for i in range(len(s) - 1):
            a = STOI[s[i]]
            b = STOI[s[i + 1]]
            N[a][b] = N[a][b] + 1
    return N


def to_probs(N):
    P = []
    for row in N:
        total = 0
        for c in row:
            total = total + c + 1
        new_row = []
        for c in row:
            new_row.append((c + 1) / total)
        P.append(new_row)
    return P


def nll(P, names):
    total = 0.0
    n = 0
    for name in names:
        s = "." + name + "."
        for i in range(len(s) - 1):
            a = STOI[s[i]]
            b = STOI[s[i + 1]]
            total = total - math.log(P[a][b])
            n = n + 1
    return total / n


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
