import random

def porta(gato):
    porta_premio = {"Porta1": "Gato", "Porta2": "Gato", "Porta3": "Gato"}

    random_number = random.random()
    print(random_number)

    if random_number < 0.33:
        porta_premio["Porta1"] = gato
        return porta_premio, "Porta1"
    elif random_number < 0.66:
        porta_premio["Porta2"] = gato
        return porta_premio, "Porta2"
    else:
        porta_premio["Porta3"] = gato
        return porta_premio, "Porta3"
