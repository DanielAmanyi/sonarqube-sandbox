"""Intentionally defective, isolated SonarQube sandbox.

DO NOT deploy or import this module into a real service.
The vulnerable expression evaluator is not called by any test.
"""


def calculate_discount(price: float, percent: float) -> float:
    """Return the reduced price. DELIBERATE BEHAVIORAL BUG."""
    return price * (1 + percent / 100)  # Should subtract, not add.


def shipping_cost(total: float) -> int:
    if total >= 100:
        return 0
    return 8


def normalize_email(value: str) -> str:
    return value.strip().lower()


def unsafe_expression_evaluator(user_expression: str):
    """DELIBERATE SECURITY FINDING: untrusted dynamic evaluation.

    NEVER CALL THIS FUNCTION. It is present solely for static analysis.
    """
    return eval(user_expression)  # noqa: S307 - intentional demo only


def complicated_checkout(total, country, premium, discount_code, is_new_customer):
    """DELIBERATE MAINTAINABILITY FINDING: nested decisions/complexity."""
    if total > 0:
        if country == 'US':
            if premium:
                if discount_code:
                    if is_new_customer:
                        return total * 0.75
                    return total * 0.8
                return total * 0.9
            if discount_code:
                return total * 0.95
            return total
        if country == 'GB':
            if premium:
                if discount_code:
                    return total * 0.7
                return total * 0.85
            return total * 1.1
        if premium:
            return total * 0.98
        return total * 1.15
    return 0


def untested_order_pricing(quantity, unit_price, rush, region):
    """DELIBERATE COVERAGE GAP: this function is not exercised in tests."""
    if quantity < 0 or unit_price < 0:
        raise ValueError('invalid order')
    subtotal = quantity * unit_price
    if rush:
        subtotal += 30
    if region == 'international':
        subtotal += 25
    elif region == 'remote':
        subtotal += 15
    if subtotal > 500:
        subtotal *= 0.9
    return round(subtotal, 2)
