"""Real assertions for the safe application functions; no execution of unsafe_expression."""

import pytest

from quality_sandbox.app import add, classify_score, format_receipt, shipping_cost


@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (-5, 5, 0), (0, 0, 0)])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("score,expected", [(0, "fail"), (49, "fail"), (50, "pass"), (79, "pass"), (80, "excellent"), (100, "excellent")])
def test_score_categories(score, expected):
    assert classify_score(score) == expected


@pytest.mark.parametrize("score", [-1, 101])
def test_out_of_range_score(score):
    with pytest.raises(ValueError, match="between 0 and 100"):
        classify_score(score)


@pytest.mark.parametrize("total,priority,expected", [(0, False, 8.0), (99, False, 8.0), (100, False, 0.0), (200, False, 0.0), (50, True, 15.0)])
def test_shipping_cost(total, priority, expected):
    assert shipping_cost(total, priority) == expected


def test_shipping_negative_total():
    with pytest.raises(ValueError, match="negative"):
        shipping_cost(-1)


def test_format_receipt():
    assert format_receipt("  Alex  ", 20.5) == "Alex: 20.50"
