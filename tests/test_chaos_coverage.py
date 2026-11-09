"""Passing tests but insufficient coverage, to isolate the coverage gate."""
from chaos_lab import normalize_email, shipping_cost


def test_shipping_small_order():
    assert shipping_cost(20) == 8


def test_email_normalization():
    assert normalize_email('  ALICE@EXAMPLE.COM ') == 'alice@example.com'
