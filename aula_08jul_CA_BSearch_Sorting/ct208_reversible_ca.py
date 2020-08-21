# -*- coding: utf-8 -*-
"""ct208_reversible_ca.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IhQ49th4peQE4L10R2MxwXJtawYemPZk
"""

# Reversible Celular Automaton
# Exemplo ajustado a partir de https://github.com/lantunes/cellpylib 
# Daniela America da Silva
# Ajustado especificamente para a regra 90 e sua reversão

# plot the resulting CA evolution
try:
  import cellpylib as cpl
except:
  !pip install cellpylib
  import cellpylib as cpl
 
from cellpylib import *

#import cellpylib as cpl

# initialize a CA with 200 cells (a random initialization is also available) 
cellular_automaton = cpl.init_simple(200)

# evolve the CA for 100 time steps, using Rule 30 as defined in NKS
cellular_automaton = cpl.evolve(cellular_automaton, timesteps=100, 
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, 90))

# plot the resulting CA evolution
cpl.plot(cellular_automaton)

cellular_automaton = cpl.init_random(200)
r = cpl.ReversibleRule(cellular_automaton[0], 90)

cellular_automaton = cpl.evolve(cellular_automaton, timesteps=100, 
                                apply_rule=r.apply_rule)

# plot the resulting reverse CA evolution
cpl.plot(cellular_automaton)