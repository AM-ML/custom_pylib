from logic import Implication, And, Not, Or
from logic import Symbol, model_check

rain = Symbol("rain") # Harry visited hagrid.
hagrid = Symbol("hagrid") # It is raining.
dumbledore = Symbol("dumbledore") # Harry visited dumbledore.

sentence = And(rain, hagrid) # It is raining and Harry visited Hagrid.

knowledge = And(
    Implication(Not(rain), hagrid), # if not rain => harry visited hagrid
    Or(hagrid, dumbledore), # Harry visited Hagrid or Dumbledore.
    Not(And(hagrid, dumbledore)), # Harry didn't visit both.
    dumbledore # Harry visited dumbledore.
)

print(model_check(knowledge, rain))
