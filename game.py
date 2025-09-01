import random

def porta():
    porta_premio = {"Porta1": "Gato", "Porta2": "Gato", "Porta3": "Gato"}

    random_number = random.random()
    print(random_number)

    if random_number < 0.33:
        porta_premio["Porta1"] = "10 milhoes"
    elif random_number < 0.66:
        porta_premio["Porta2"] = "10 milhoes"
    else:
        porta_premio["Porta3"] = "10 milhoes"

    import random

    porta_premio = {"Porta1": "Gato", "Porta2": "Gato", "Porta3": "Gato"}

    random_number = random.random()
    print(random_number)

    if random_number < 0.33:
        porta_premio["Porta1"] = "10 milhoes"
    elif random_number < 0.66:
        porta_premio["Porta2"] = "10 milhoes"
    else:
        porta_premio["Porta3"] = "10 milhoes"

    print(porta_premio)
    return(porta_premio)

