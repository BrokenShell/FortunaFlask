# FortunaFlask


Web API for Fortuna.

### `/canonical`
Returns a random float in range (0.0, 1.0], tail exclusive.

### `/triangular/<low>,<high>,<mode>`
Returns a random float in range [low, high] with a distribution peak at the mode.

### `/d<sides>`
Returns a random integer with uniform distribution in range [1, sides], inclusive.

### `/dice/<rolls>d<sides>`
Returns a random integer with geometric distribution based on the number of dice rolled, and the number of sides each die has.

### `/percent-true/<percent>`
Returns a random boolean, distribution based on the ratio of truth as a percent.

### `/random-range/<start>,<stop>,<step>`
Returns a random integer in range (start, stop] with stepping. Tail exclusive.
