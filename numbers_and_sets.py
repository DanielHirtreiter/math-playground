"""
Numbers and sets: a small executable introduction.

Run:
    python numbers_and_sets.py

Mathematical number sets form a hierarchy:

    N ⊂ Z ⊂ Q ⊂ R ⊂ C

N  natural numbers: 0, 1, 2, ... (some books start at 1)
Z  integers: ..., -2, -1, 0, 1, 2, ...
Q  rational numbers: fractions p / q, where p and q are integers and q != 0
R  real numbers: every point on the number line
C  complex numbers: a + bi, where i² = -1

Important: Python types are representations of mathematical numbers.
For example, a float is only a finite approximation of most real numbers.
"""

from fractions import Fraction
from math import pi, sqrt


def explain_number_sets() -> None:
    """Show representative values from the main mathematical number sets."""
    natural_number = 5
    integer = -3
    rational_number = Fraction(2, 3)
    irrational_number = sqrt(2)
    real_number = pi
    complex_number = 2 + 3j

    examples = [
        ("Natural number N", natural_number),
        ("Integer Z", integer),
        ("Rational number Q", rational_number),
        ("Irrational real number", irrational_number),
        ("Real number R", real_number),
        ("Complex number C", complex_number),
    ]

    print("NUMBER SETS")
    print("-----------")
    for name, value in examples:
        print(f"{name:24}: {value!r}")

    print("\nHierarchy: N ⊂ Z ⊂ Q ⊂ R ⊂ C")
    print("Every natural number is an integer, but not every integer is natural.")
    print("Every integer is rational because, for example, -3 = -3/1.")
    print("Rational and irrational numbers together form the real numbers.")
    print("Every real number is complex because a real number a equals a + 0i.")


def explain_python_number_types() -> None:
    """Demonstrate how Python represents several kinds of numbers."""
    print("\nPYTHON NUMBER TYPES")
    print("-------------------")
    values = [5, -3, Fraction(2, 3), 0.1, 2 + 3j]
    for value in values:
        print(f"{value!r:12} -> {type(value).__name__}")

    print("\nFloats are approximations:")
    print(f"0.1 + 0.2 == 0.3 -> {0.1 + 0.2 == 0.3}")
    print(f"0.1 + 0.2        -> {0.1 + 0.2!r}")

    exact_sum = Fraction(1, 10) + Fraction(2, 10)
    print(f"1/10 + 2/10      -> {exact_sum} (exact)")


def explain_sets() -> None:
    """
    Demonstrate finite sets.

    A set is an unordered collection of distinct elements.
    Python writes a set with braces, for example {1, 2, 3}.
    """
    natural_examples = {0, 1, 2, 3, 4, 5}
    even_examples = {0, 2, 4}
    prime_examples = {2, 3, 5}
    empty_set = set()  # {} would create an empty dictionary, not an empty set.

    print("\nSETS")
    print("----")
    print(f"Natural-number sample N₅: {sorted(natural_examples)}")
    print(f"Even-number sample E     : {sorted(even_examples)}")
    print(f"Prime-number sample P    : {sorted(prime_examples)}")
    print(f"Empty set ∅              : {empty_set}")

    print("\nMembership and size:")
    print(f"3 ∈ N₅                    -> {3 in natural_examples}")
    print(f"7 ∈ N₅                    -> {7 in natural_examples}")
    print(f"|N₅|, the cardinality     -> {len(natural_examples)}")

    print("\nRelations and operations:")
    print(f"E ⊆ N₅ (subset)           -> {even_examples <= natural_examples}")
    print(f"E ∪ P (union)             -> {sorted(even_examples | prime_examples)}")
    print(f"E ∩ P (intersection)      -> {sorted(even_examples & prime_examples)}")
    print(f"E \\ P (difference)        -> {sorted(even_examples - prime_examples)}")
    print(
        f"E △ P (symmetric diff.)   -> "
        f"{sorted(even_examples ^ prime_examples)}"
    )

    cartesian_product = {
        (left, right)
        for left in {1, 2}
        for right in {"a", "b"}
    }
    print(
        "A × B (Cartesian product) -> "
        f"{sorted(cartesian_product)}"
    )


def explain_set_builder_idea() -> None:
    """Connect mathematical set-builder notation to a Python comprehension."""
    # Mathematical idea: E = {n ∈ N | n is even and n <= 10}
    even_numbers_to_ten = {n for n in range(11) if n % 2 == 0}

    print("\nSET-BUILDER IDEA")
    print("----------------")
    print("E = {n ∈ N | n is even and n ≤ 10}")
    print(f"Python result: {sorted(even_numbers_to_ten)}")


def main() -> None:
    explain_number_sets()
    explain_python_number_types()
    explain_sets()
    explain_set_builder_idea()


if __name__ == "__main__":
    main()
