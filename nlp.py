import re
import spacy
from nltk.corpus import wordnet as wn
from nounlist import nouns
from numpy import dot
from numpy.linalg import norm
from random import choice

model_md = spacy.load('en_core_web_md')
# log = []


def get_target():
    """Choose a target word from a list of common nouns."""
    target = choice(nouns)
    print('The target is %s.' % (target))
    return target


def normalize_for_display(token):
    """Return a normalized token for display.

        INPUT                    NORMALIZED
        Potato              ->   potato
         soccer             ->   soccer
        musical_instrument  ->   musical instrument
        mother-in-law       ->   mother-in-law
        1990s               ->   1990s
        roaring 20's        ->   roaring 20's
    """
    return token.lower().strip()


def normalize_for_evaluation(token):
    """Return a normalized token for evaluation.

        INPUT                    NORMALIZED
        Potato              ->   potato
         soccer             ->   soccer
        musical instrument  ->   musical_instrument
        mother-in-law       ->   mother-in-law
        1990s               ->   1990s
        roaring 20's        ->   roaring_20s
    """
    # Basic cleanup.
    token = token.lower().strip()
    # Remove articles the, a, an.
    articles = re.compile("^(a|an|the) ")
    token = articles.sub('', token)
    # Remove invalid characters.
    invalid_chars = re.compile("[^a-z0-9- ]")
    token = invalid_chars.sub('', token)

    return token


def vec(word, model=model_md):
    """Convert word to vector using the specified model."""
    return model.vocab[word].vector


def evaluate(current, guess, target):
    """Evaluate a guess."""
    print('Evaluate: %s, %s, %s' % (current, guess, target))
    global log

    current_vec = vec(current)
    guess_vec = vec(guess)
    target_vec = vec(target)

    current_similarity = vec_similarity(current_vec, target_vec)
    guess_similarity = vec_similarity(guess_vec, target_vec)

    if guess == target:
        msg = "Exactly! %s is a perfect match." % (
            guess)
        print(msg)
        move = 0  # End game.
        # log += [(guess, move)]
    elif guess_similarity >= current_similarity:
        msg = "It's more like '%s' than it is like '%s'." % (
            guess, current)
        print(msg)
        move = 1  # Advance.
        # log += [(guess, move)]
    elif guess_similarity == 0.0:
        msg = "'%s' is not in the program's dictionary." % (guess)
        print(msg)
        move = 2  # No change (unsure).
    else:
        msg = "It's more like '%s' than it is like '%s'." % (
            current, guess)
        print(msg)
        move = 3  # No change.
        # log += [(guess, move)]

    for item in log:
        print(item)
    return (move, msg)


def vec_similarity(vec1, vec2, use_abs=True):
    """Find the cosine similarity of two words."""
    if norm(vec1) > 0 and norm(vec2) > 0:
        similarity = dot(vec1, vec2) / (norm(vec1) * norm(vec2))
        if(use_abs):
            similarity = abs(similarity)
    else:
        similarity = 0.0
    return similarity
