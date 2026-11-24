# === Stage 4: Редактирование записей ===
# Project: FlashDeck
from datetime import date


def _validate_card_fields(card):
    if "question" not in card or "answer" not in card or "deck" not in card or "date" not in card:
        raise ValueError("Card must contain 'question', 'answer', 'deck', and 'date'.")
    if not isinstance(card["question"], str) or not card["question"].strip():
        raise ValueError("Question must be a non-empty string.")
    if not isinstance(card["answer"], str) or not card["answer"].strip():
        raise ValueError("Answer must be a non-empty string.")
    if not isinstance(card["deck"], str) or not card["deck"].strip():
        raise ValueError("Deck must be a non-empty string.")
    valid_date = isinstance(card["date"], date)
    if not valid_date:
        raise ValueError("Date must be a datetime.date instance.")
    return True


def update_card(card_id, updates, existing_cards):
    card = existing_cards.get(card_id)
    if card is None:
        raise KeyError(f"Card with id {card_id!r} not found.")
    allowed_fields = {"question", "answer", "deck"}
    for key, value in updates.items():
        if key not in allowed_fields:
            raise ValueError(f"Field {key!r} is not editable for a card.")
        if key == "date":
            if not isinstance(value, date):
                raise ValueError("Date must be a datetime.date instance.")
            card[key] = value
        else:
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Field {key!r} must be a non-empty string.")
            card[key] = value
    return card


def create_card(question, answer, deck, study_date):
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Question must be a non-empty string.")
    if not isinstance(answer, str) or not answer.strip():
        raise ValueError("Answer must be a non-empty string.")
    if not isinstance(deck, str) or not deck.strip():
        raise ValueError("Deck must be a non-empty string.")
    if not isinstance(study_date, date):
        raise ValueError("Study date must be a datetime.date instance.")
    return {
        "question": question,
        "answer": answer,
        "deck": deck,
        "date": study_date,
    }


def list_cards_by_deck(deck_name, existing_cards):
    return [card for card in existing_cards.values() if card["deck"] == deck_name]


def card_stats(card):
    return {
        "question": card["question"],
        "answer": card["answer"],
        "deck": card["deck"],
        "study_date": card["date"].isoformat(),
    }
