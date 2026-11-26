# === Stage 6: Связи между сущностями ===
# Project: FlashDeck
def get_due_cards_for_deck(deck_id, db):
    """Return a list of flashcards in the given deck that are due for review.

    A flashcard is due when it has at least one review with a due date
    not later than today. The deck_id is validated against the deck table
    to ensure the relationship is intact.
    """
    today = _today_date()
    due_cards = []

    deck_row = db.execute(
        "SELECT id, name FROM deck WHERE id = ?", (deck_id,)
    ).fetchone()
    if deck_row is None:
        raise ValueError(f"deck with id {deck_id} not found")

    for card_row in db.execute(
        """
        SELECT c.id, c.question, c.answer
        FROM card c
        WHERE c.deck_id = ?
        ORDER BY c.id
        """,
        (deck_id,),
    ).fetchall():
        card_id = card_row[0]
        if _card_has_due_review(db, card_id, today):
            due_cards.append({
                "id": card_id,
                "question": card_row[1],
                "answer": card_row[2],
            })

    return due_cards


def _card_has_due_review(db, card_id, today):
    """Check whether a card has any review due on or before today."""
    row = db.execute(
        """
        SELECT due_date
        FROM review
        WHERE card_id = ? AND due_date <= ?
        ORDER BY due_date
        LIMIT 1
        """,
        (card_id, today),
    ).fetchone()
    return row is not None


def _today_date():
    """Return today's date formatted as YYYY-MM-DD."""
    from datetime import date
    return date.today().isoformat()
