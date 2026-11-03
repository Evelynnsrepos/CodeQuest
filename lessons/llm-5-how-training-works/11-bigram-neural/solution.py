import math

NAMES = """emma olivia ava sophia isabella mia amelia harper evelyn abigail emily ella elizabeth camila luna sofia avery mila aria scarlett penelope layla chloe victoria madison eleanor grace nora riley zoey hannah hazel lily ellie violet lillian zoe stella aurora natalie emilia everly leah aubrey willow addison lucy audrey bella nova brooklyn paisley savannah claire skylar isla genesis naomi elena caroline eliana anna maya valentina ruby kennedy ivy ariana aaliyah cora madelyn alice kinsley hailey gabriella allison gianna serenity samantha sarah autumn quinn eva piper sophie sadie delilah josephine nevaeh adeline arya emery lydia clara vivian madeline peyton julia rylee liam noah oliver elijah william james benjamin lucas henry alexander mason michael ethan daniel jacob logan jackson levi sebastian mateo jack owen theodore aiden samuel joseph john david wyatt matthew luke asher carter julian grayson leo jayden gabriel isaac lincoln anthony hudson dylan ezra thomas charles christopher jaxon maverick josiah isaiah andrew elias joshua nathan caleb ryan adrian miles eli nolan christian aaron cameron ezekiel colton luca landon hunter jonathan santiago axel easton cooper jeremiah angel roman connor jameson robert greyson jordan ian carson jaxson leonardo nicholas dominic austin everett brooks xavier kai jose parker adam jace wesley kayden silas""".split()
CHARS = "." + "abcdefghijklmnopqrstuvwxyz"
STOI = {ch: i for i, ch in enumerate(CHARS)}
PAIRS = [(STOI[a], STOI[b]) for name in NAMES for a, b in zip("." + name, name + ".")]


def softmax(row):
    m = max(row)
    e = [math.exp(x - m) for x in row]
    s = sum(e)
    return [x / s for x in e]


def loss_and_grad(W, pairs):
    probs = [softmax(row) for row in W]
    grad = [[0.0] * 27 for _ in range(27)]
    loss = 0.0
    for a, b in pairs:
        loss += -math.log(probs[a][b])
        for j in range(27):
            grad[a][j] += probs[a][j]
        grad[a][b] -= 1
    n = len(pairs)
    return loss / n, [[g / n for g in row] for row in grad]


W = [[0.0] * 27 for _ in range(27)]
for epoch in range(60):
    loss, grad = loss_and_grad(W, PAIRS)
    for i in range(27):
        for j in range(27):
            W[i][j] -= 50 * grad[i][j]
    if epoch % 10 == 0 or epoch == 59:
        print(f"epoch {epoch:2}: loss {loss:.3f}")
final_loss = loss
