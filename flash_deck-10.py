# === Stage 10: Поиск по нескольким словам ===
# Project: FlashDeck
from typing import Iterable, List, Set


def _tokenize(query: str) -> List[str]:
    query = query.strip()
    if not query:
        return []
    tokens = query.split()
    return tokens


def _split_word(token: str) -> tuple:
    if token.startswith("-"):
        return ("exclude", token[1:].strip().lower())
    return ("include", token.lower())


def parse_query(query: str) -> tuple:
    includes: Set[str] = set()
    excludes: Set[str] = set()
    tokens = _tokenize(query)
    for token in tokens:
        kind, word = _split_word(token)
        if kind == "include":
            includes.add(word)
        else:
            excludes.add(word)
    return (includes, excludes)


def cards_match(query: str, cards: Iterable) -> List:
    includes, excludes = parse_query(query)
    return [
        card
        for card in cards
        if _matches(card, includes) and _matches(card, excludes)
    ]


def _matches(card, required: Set[str]) -> bool:
    haystack: Set[str] = set()
    for field in ("question", "answer"):
        value = getattr(card, field, "")
        if isinstance(value, str):
            haystack.update(_split_text(value))
    return required.issubset(haystack)


def _split_text(text: str) -> Set[str]:
    words: Set[str] = set()
    for piece in text.split():
        words.add(piece.lower())
    return words


def find_cards(query: str, cards: Iterable) -> List:
    return cards_match(query, list(cards))


if __name__ == "__main__":
    class Card:
        def __init__(self, question: str, answer: str):
            self.question = question
            self.answer = answer

    deck = [
        Card("What is the capital of France?", "Paris"),
        Card("What is the capital of Italy?", "Rome"),
        Card("What is the capital of Spain?", "Madrid"),
    ]

    for pattern in ("France", "-France Italy", "capital -Italy"):
        matches = find_cards(pattern, deck)
        print(f"Pattern '{pattern}':")
        for match in matches:
            print(f"  {match.question} -> {match.answer}")
        print()
