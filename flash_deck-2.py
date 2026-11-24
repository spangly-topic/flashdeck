# === Stage 2: Проверка полей ===
# Project: FlashDeck
from datetime import date


class Card:
    def __init__(self, question, answer, deck, due_date):
        self.question = question
        self.answer = answer
        self.deck = deck
        self.due_date = due_date


def normalize_input(value):
    if value is None:
        return ""
    return value.strip()


def normalize_date(value):
    if value is None:
        return None
    cleaned = value.strip()
    if cleaned.lower() in ("", "none", "n/a"):
        return None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d.%m.%Y", "%m/%d/%Y"):
        try:
            parsed = date.fromisoformat(cleaned[:10])
            return parsed
        except ValueError:
            continue
    raise ValueError("Date must be in YYYY-MM-DD or DD/MM/YYYY format")


def validate_card(card):
    errors = []
    question = normalize_input(card.question)
    if not question:
        errors.append("Question cannot be empty")
    if not normalize_input(card.answer):
        errors.append("Answer cannot be empty")
    if not normalize_input(card.deck):
        errors.append("Deck name cannot be empty")
    if card.due_date is not None:
        try:
            normalize_date(card.due_date)
        except ValueError as err:
            errors.append(str(err))
    return errors, question
