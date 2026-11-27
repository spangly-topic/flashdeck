# === Stage 8: Фильтрация записей ===
# Project: FlashDeck
def filter_cards_by_answer(cards, answer):
    """Return cards whose answer field equals the given value."""
    return [card for card in cards if card.get("answer") == answer]


def filter_cards_by_date_range(cards, start_date, end_date):
    """Return cards created on or after start_date and on or before end_date.

    Dates are compared as strings in ISO format (YYYY-MM-DD) so lexicographic
    comparison matches chronological order.
    """
    result = []
    for card in cards:
        created = card.get("created_at")
        if created is None:
            continue
        if start_date is not None and created < start_date:
            continue
        if end_date is not None and created > end_date:
            continue
        result.append(card)
    return result


def filter_cards(cards, answer=None, start_date=None, end_date=None):
    """Apply answer and date-range filters to a list of card records.

    Each card is expected to be a dict with keys: question, answer, deck,
    created_at. Filters are applied in sequence and combined with logical AND.
    """
    filtered = list(cards)
    if answer is not None:
        filtered = filter_cards_by_answer(filtered, answer)
    if start_date is not None or end_date is not None:
        filtered = filter_cards_by_date_range(filtered, start_date, end_date)
    return filtered


if __name__ == "__main__":
    sample_cards = [
        {
            "id": "c1",
            "question": "What is 2 + 2?",
            "answer": "4",
            "deck": "math",
            "created_at": "2024-01-05",
        },
        {
            "id": "c2",
            "question": "Capital of France?",
            "answer": "Paris",
            "deck": "geography",
            "created_at": "2024-02-10",
        },
        {
            "id": "c3",
            "question": "What is the color of the sky?",
            "answer": "Blue",
            "deck": "science",
            "created_at": "2024-03-15",
        },
    ]

    print("Answer '4':")
    for card in filter_cards(sample_cards, answer="4"):
        print(f"  {card['id']}: {card['question']}")

    print("Answer 'Blue':")
    for card in filter_cards(sample_cards, answer="Blue"):
        print(f"  {card['id']}: {card['question']}")

    print("Created between 2024-01-01 and 2024-02-28:")
    for card in filter_cards(
        sample_cards, start_date="2024-01-01", end_date="2024-02-28"
    ):
        print(f"  {card['id']}: {card['question']}")

    print("Answer 'Blue' and created after 2024-02-01:")
    for card in filter_cards(
        sample_cards, answer="Blue", start_date="2024-02-01"
    ):
        print(f"  {card['id']}: {card['question']}")
