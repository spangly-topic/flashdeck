# === Stage 3: Хранилище в памяти ===
# Project: FlashDeck
import time
import uuid


class Card:
    def __init__(self, question, answer, deck_id, created_at=None):
        self.id = uuid.uuid4().hex
        self.question = question
        self.answer = answer
        self.deck_id = deck_id
        self.created_at = created_at if created_at is not None else time.time()

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "deck_id": self.deck_id,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            question=data["question"],
            answer=data["answer"],
            deck_id=data["deck_id"],
            created_at=data.get("created_at"),
        )

    def __repr__(self):
        return f"Card(id={self.id}, question={self.question!r})"


class CardStore:
    def __init__(self):
        self._cards = {}

    def add(self, card):
        self._cards[card.id] = card
        return card

    def get(self, card_id):
        return self._cards.get(card_id)

    def list(self, deck_id=None):
        if deck_id is None:
            return list(self._cards.values())
        return [c for c in self._cards.values() if c.deck_id == deck_id]

    def count(self):
        return len(self._cards)
