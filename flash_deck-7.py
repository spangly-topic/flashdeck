# === Stage 7: Генерация идентификаторов ===
# Project: FlashDeck
import string
import secrets
import datetime


PROJECT_PREFIX = "fd"
ID_NAMESPACE = "flashdeck"


def _generate_unique_suffix(length: int = 8) -> str:
    alphabet = string.ascii_lowercase + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def generate_deck_id() -> str:
    while True:
        candidate = f"{PROJECT_PREFIX}:{ID_NAMESPACE}:deck:{_generate_unique_suffix()}"
        if not _is_taken(candidate):
            return candidate


def generate_card_id() -> str:
    while True:
        candidate = f"{PROJECT_PREFIX}:{ID_NAMESPACE}:card:{_generate_unique_suffix()}"
        if not _is_taken(candidate):
            return candidate


def generate_review_id() -> str:
    while True:
        candidate = f"{PROJECT_PREFIX}:{ID_NAMESPACE}:review:{_generate_unique_suffix()}"
        if not _is_taken(candidate):
            return candidate


def _is_taken(candidate: str) -> bool:
    for entity_type, collection in _iter_existing():
        for existing_id in collection:
            if existing_id == candidate:
                return True
    return False


def _iter_existing():
    yield "deck", _deck_ids()
    yield "card", _card_ids()
    yield "review", _review_ids()


def _deck_ids():
    return set(_DECK_IDS)


def _card_ids():
    return set(_CARD_IDS)


def _review_ids():
    return set(_REVIEW_IDS)


_DECK_IDS: set[str] = set()
_CARD_IDS: set[str] = set()
_REVIEW_IDS: set[str] = set()


def register_id(entity_type: str, identifier: str) -> None:
    if entity_type == "deck":
        _DECK_IDS.add(identifier)
    elif entity_type == "card":
        _CARD_IDS.add(identifier)
    elif entity_type == "review":
        _REVIEW_IDS.add(identifier)
    else:
        raise ValueError(f"unknown entity type: {entity_type}")


def _register_all() -> None:
    for identifier in _DECK_IDS:
        register_id("deck", identifier)
    for identifier in _CARD_IDS:
        register_id("card", identifier)
    for identifier in _REVIEW_IDS:
        register_id("review", identifier)


_register_all()


def now_utc() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def to_isoformat(value: datetime.datetime) -> str:
    return value.astimezone(datetime.timezone.utc).isoformat()


def from_isoformat(text: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(text).astimezone(datetime.timezone.utc)
