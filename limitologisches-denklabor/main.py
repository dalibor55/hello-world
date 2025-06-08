"""Ein kleines Projekt zur poetischen Reflexion."""

from textwrap import fill


def generiere_reflexion(begriff: str) -> str:
    """Erzeugt eine kurze poetische Reflexion zu einem Begriff."""
    text = (
        f"Im Begriff '{begriff}' verbirgt sich ein Echo von Moeglichkeiten, "
        "ein Anstoss zum Weiterdenken, der die Schwelle des Gewohnten "
        "ueberschreitet."
    )
    return fill(text)


if __name__ == "__main__":
    print(generiere_reflexion("Riss"))
