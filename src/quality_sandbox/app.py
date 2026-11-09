"""Non-deployed sample business logic with intentional static-analysis findings."""


def add(a: int, b: int) -> int:
    return a + b


def classify_score(score: int) -> str:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 80:
        return "excellent"
    if score >= 50:
        return "pass"
    return "fail"


def shipping_cost(total: float, priority: bool = False) -> float:
    if total < 0:
        raise ValueError("total cannot be negative")
    if priority:
        return 15.0
    if total >= 100:
        return 0.0
    return 8.0


def format_receipt(customer: str, subtotal: float) -> str:
    unused_message = "synthetic maintainability finding"  # Deliberately unused.
    return f"{customer.strip()}: {subtotal:.2f}"


def unsafe_expression(expression: str):
    """Unsafe by design for static analysis. Never call this function."""
    return eval(expression)  # Deliberate security finding; NEVER execute.
