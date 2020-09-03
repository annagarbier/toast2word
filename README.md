# Toast-to-word

A collaborative game in which a human and computer navitage semantic space together, one question at a time.

Built with Python/Flask and SpaCy word embeddings.

## The original folk game

Toast-to-word is a modern take on a much older folk game. In the original game, two humans play.

The first person (_the picker_) picks a thing: e.g. a banana, a nightingale, the sky. The second person (_the guesser_) must discover that thing, but they can only do so through a series of constrained questions.

The guessing always begins with 'toast'-- hence the name of the game. An (artificially short) example game dialogue:

```txt
GUESSER:  Is it more like toast or a kitchen?
PICKER:   It's more like a kitchen.

GUESSER:  More like a kitchen or a living room?
PICKER:   It's more like a living room.

GUESSER:  More like a living room or a bedroom?
PICKER:   It's more like a living room.

GUESSER:  More like a living room or a couch?
PICKER:   More like a living room.

GUESSER:  More like a living room or a coffee table?
PICKER:   More like a living room.

GUESSER:  More like a living room or a carpet?
PICKER:   More like a carpet.

GUESSER:  More like a carpet or a vaccuum?
PICKER:   You got it! It's a vaccuum!
```

## The machine learning version

In this version of toast-to-word, a computer program acts as the picker. Gameplay begins when the program chooses a `TARGET` word from a large curated list of nouns.

Once the `TARGET` is chosen, the human guesser begins: "Is it more like WORDA or WORDB?" When the program answers, it does so by calculating the similarity between SpaCy word embeddings. Specifically, it calculates the cosine similarity between `WORDA` and the `TARGET`, and `WORDB` and the `TARGET`. If the latter is larger (i.e. more similar), then the player advances...getting one step cloesr to the `TARGET`.

Just as in the traditional game, this procedure is repeated until the guesser narrows in on the exact `TARGET`.

## Insights

## To run this code

```sh
# Install spacy, nltk, numpy.

# Run in demo mode
flask run

# Run in development mode
export FLASK_ENV=development
flask run
```
