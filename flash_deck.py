# === Stage 1: Каркас модуля ===
# Project: FlashDeck
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Card:
    question: str
    answer: str
    deck: str
    due_date: date = field(default_factory=date.today)


def create_demo_cards() -> list[Card]:
    return [
        Card(question="What is the capital of France?", answer="Paris", deck="Geography"),
        Card(question="What is 2 + 2?", answer="4", deck="Math"),
        Card(question="Python file extension?", answer=".py", deck="Programming"),
    ]


def main() -> None:
    cards = create_demo_cards()
    for card in cards:
        print(f"Q: {card.question}")
        print(f"A: {card.answer}")
        print(f"Deck: {card.deck}")
        print(f"Due: {card.due_date}\n")


if __name__ == "__main__":
    main()
