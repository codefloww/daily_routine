# daily_routine
A simulation of my ordinar day using deterministic automata
## Structure
In [mystates.py](mystates.py) can be seen a 5 states of person despite initial state.  
Each hour based on the state of environment(hour of day, energy of person, place of person and current routine), the new state of automata is decided and changes to environment are made.  
There are also three random events that may change state of environment, including state of automata.  
## Usage 
For running simulation you simply need to clone repository and run [day_sim.py](day_sim.py).  
It will run 1000 hours of life of the automata, if energy doesn't drop below 0(automata dies and simulation ends).
