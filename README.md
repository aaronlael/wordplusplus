# wordplusplus
Wordle-a-like in a mastermind flavor

This is my tribute to wordle and mastermind.  It is a game that encourages you to use words to probe before ultimately trying to guess the word on your 6th "guess".

For example, if your target word was "tacos"

And you initially guessed "flame", you'd get:

flame - 01000 > this tells you that one letter from flame occurs in the 2nd position of the target word.

Now, let's say guess two you guessed "flood", you'd get:

flood - 01020 > you still have the 1 letter from flame, but now you have incremented position 4 twice!  This must be an "o"

And so on and so forth ... until your ultimate guess.

For clarification, if your target word was "flood" and you guessed "boils", you'd get 01110.

This is entirely a CLI based game but I intend to adapt it to the web.

You won't win nearly as often with this as you do on Wordle, and that is perfectly fine.
