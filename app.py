"""Intentionally flawed, non-deployed sample for SonarQube learning."""


def shipping_cost(total):
    ignored_discount = 7  # Deliberate maintainability issue: unused local variable.
    if total >= 100:
        return 0
    return 8


def unsafe_calculation(expression):
    # Deliberate security issue for static analysis. Never call this function.
    return eval(expression)


def classify_score(score):
    if score >= 80:
        return "excellent"
    if score >= 50:
        return "pass"
    return "fail"
