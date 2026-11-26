# === Stage 5: Удаление и восстановление ===
# Project: FlashDeck
from datetime import datetime


class Card:
    """A single flashcard: a question paired with an answer.

    Cards support soft deletion. When deleted, the flag is set and the
    record remains in the deck so it can be restored later.
    """

    def __init__(self, question, answer, deck_id, created=None):
        self.id = None
        self.question = question
        self.answer = answer
        self.deck_id = deck_id
        self.created = created or datetime.now()
        self.deleted = False

    def delete(self):
        """Soft-delete the card. The row is kept but marked deleted."""
        self.deleted = True

    def restore(self):
        """Undo a soft deletion and return the card to active state."""
        self.deleted = False

    def is_active(self):
        """Return True when the card is not soft-deleted."""
        return not self.deleted

    def __repr__(self):
        return (
            f"Card(id={self.id}, question={self.question!r}, "
            f"deck_id={self.deck_id}, deleted={self.deleted})"
        )


class CardStore:
    """In-memory collection of cards with deletion and restore support."""

    def __init__(self):
        self._cards = {}

    def add(self, card):
        """Register a new card and assign it an integer id."""
        card.id = len(self._cards) + 1
        self._cards[card.id] = card
        return card

    def get(self, card_id):
        """Return the card with the given id, or None if missing."""
        return self._cards.get(card_id)

    def active_cards(self):
        """Yield only cards that are not soft-deleted."""
        return (card for card in self._cards.values() if card.is_active())

    def delete(self, card_id):
        """Soft-delete the card identified by card_id."""
        card = self.get(card_id)
        if card is not None:
            card.delete()
            return True
        return False

    def restore(self, card_id):
        """Restore the soft-deleted card identified by card_id."""
        card = self.get(card_id)
        if card is not None and card.deleted:
            card.restore()
            return True
        return False

    def count_active(self):
        """Return the number of currently active cards."""
        return sum(1 for card in self.active_cards())

    def to_list(self):
        """Return a list of all cards, newest first."""
        return sorted(self._cards.values(), key=lambda c: c.id, reverse=True)
