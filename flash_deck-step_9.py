# === Stage 9: Сортировка записей ===
# Project: FlashDeck
from datetime import datetime


def sort_cards_by_question(cards):
    return sorted(cards, key=lambda card: str(card["question"]).lower())


def sort_cards_by_created_date(cards):
    return sorted(cards, key=lambda card: card["created_at"], reverse=True)


def sort_cards_by_created_date_asc(cards):
    return sorted(cards, key=lambda card: card["created_at"])


def sort_cards_by_question_and_date(cards):
    return sorted(cards, key=lambda card: (str(card["question"]).lower(), card["created_at"]))


def sort_cards_by_question_and_date_desc(cards):
    return sorted(cards, key=lambda card: (str(card["question"]).lower(), card["created_at"]), reverse=True)
