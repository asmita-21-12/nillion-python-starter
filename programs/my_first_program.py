from nada_dsl import *

def nada_main():
    # Define the party
    party1 = Party(name="Party1")
    
    # Define inputs as SecretIntegers
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    # Perform the computation: Add the two secret integers
    result = my_int1 + my_int2
    
    # Output the result
    return [Output(result, "sum_output", party=party1)]
