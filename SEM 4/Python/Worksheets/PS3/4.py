# create dictionary and initialise
alonzo = {"age": 10, "height": 42, "weight": 175, "instrument": "fiddle" }
turing = {"age": 41, "height": 70, "weight": 160, "instrument": "theremin"}
bertha = {"age": 32, "height": 97, "weight": 587, "instrument": "cello"}
tinkerB = {"age": 100, "height": 4, "weight": 0.5, "instrument": "cello"}
banditos = {"Alonzo": alonzo, "Turing": turing, "Bertha": bertha, "TinkerB": tinkerB}


# function that returns new dictionary with people
# playing the instrument passed in the function parameter
def get_new_dictionary(instrument):
    # initialise empty dictionary
    particular_instrument = {}
    for key, value in banditos.items():
        # checking for instrument in banditos dictionary
        # updating it to the new dictionary 'particular_instrument'
        if value['instrument'] == instrument:
            particular_instrument.update({key: value})
    return particular_instrument


if __name__ == '__main__':
    # print result of get_new_dictionary function that returns people playing input instrument
    print(get_new_dictionary(input('Enter the instrument : ')))

# in case of no instruments available, empty dictionary is returned
