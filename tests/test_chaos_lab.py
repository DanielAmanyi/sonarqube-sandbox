"""One passing assertion and one intentionally failing assertion."""
from chaos_lab import calculate_discount, normalize_email, shipping_cost


def test_shipping_cost():
    assert shipping_cost(120) == 0


def test_normalize_email():
    assert normalize_email('  USER@EXAMPLE.COM ') == 'user@example.com'


def test_discount_should_reduce_price():
    # INTENTIONAL FAILURE: application returns 110.0, expected 90.0.
    assert calculate_discount(100, 10) == 90
