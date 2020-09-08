# Toast2word V1 (Global)

A collaborative game in which a human and computer program navitage semantic space together, one question at a time. Written in Python, using SpaCy word embeddings, and Flask micro web framework.

## The original folk game

The original game is played through dialogue alone. Player 1 thinks of a word or phrase. It can be any noun (e.g. PENGUIN, FORKLIFT, or DONALD GLOVER). Player 2 tries to guess the target word or phrase through questions and answers, beginning with "Is it more like TOAST or \_\_\_?" For example, "Is it more like TOAST or CAT?" If the target is more like CAT, then the question pivots: "Is it more like CAT or \_\_\_?" This procedure continues until Player 2 arrives at the target.

## The machine learning version

In this ML version, a computer program begins by choosing a target from a large, curated list of nouns. Once the target is selected, a human player begins the questioning. As before, the first question is always: "Is the word more like TOAST or \_\_\_?"

The interface through which the human and program communicate is a simple web form, built using Flask. When the program answers the human's questions, it does so by 1) finding the word embeddings for the two candidates in question, then 2) calculating the cosine similarities between the candidate words and the target word. If the new candidate is more similar (i.e. has a higher cosine similarity) to the target, then Player 2 advances, and the web form updates.

## Watch the demo & read more

https://annagarbier.com/Toast2word-V1-Global

## Run the code

1. `cd toast2word`
1. `flask run`
