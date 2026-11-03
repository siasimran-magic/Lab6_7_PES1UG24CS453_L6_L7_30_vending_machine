import pytest
from vending_machine import select_item, make_change, purchase


# ---------------------------------------------------------------------------
# Tests for select_item
# ---------------------------------------------------------------------------

def test_select_item_invalid():
    assert select_item("water", {"cola": 5}, 150) == "invalid"


def test_select_item_sold_out_zero_stock():
    assert select_item("cola", {"cola": 0}, 150) == "sold_out"


def test_select_item_sold_out_missing_key():
    assert select_item("chips", {}, 100) == "sold_out"


def test_select_item_insufficient_credit():
    assert select_item("chips", {"chips": 5}, 50) == "insufficient"


def test_select_item_ok_exact_credit():
    assert select_item("chips", {"chips": 5}, 100) == "ok"


def test_select_item_ok_surplus_credit():
    assert select_item("candy", {"candy": 5}, 100) == "ok"


# ---------------------------------------------------------------------------
# Tests for make_change
# ---------------------------------------------------------------------------

def test_make_change_negative():
    with pytest.raises(ValueError, match="negative amount"):
        make_change(-1)


def test_make_change_zero():
    assert make_change(0) == []


def test_make_change_all_denominations():
    assert make_change(190) == [100, 50, 25, 10, 5]


def test_make_change_multiple_same_coin():
    assert make_change(200) == [100, 100]


def test_make_change_partial_coins():
    assert make_change(15) == [10, 5]


def test_make_change_impossible_remainder_small():
    assert make_change(3) is None


def test_make_change_impossible_remainder_after_coins():
    assert make_change(7) is None


# ---------------------------------------------------------------------------
# Tests for purchase
# ---------------------------------------------------------------------------

def test_purchase_status_invalid_item():
    status, change = purchase("soda", {"cola": 5}, 200)
    assert status == "invalid"
    assert change == []


def test_purchase_status_sold_out():
    stock = {"chips": 0}
    status, change = purchase("chips", stock, 100)
    assert status == "sold_out"
    assert change == []
    assert stock["chips"] == 0


def test_purchase_status_insufficient_credit():
    stock = {"cola": 3}
    status, change = purchase("cola", stock, 100)
    assert status == "insufficient"
    assert change == []
    assert stock["cola"] == 3


def test_purchase_no_exact_change():
    stock = {"chips": 2}
    status, change = purchase("chips", stock, 103)
    assert status == "no_exact_change"
    assert change == []
    assert stock["chips"] == 2


def test_purchase_success_exact_payment():
    stock = {"candy": 4}
    status, change = purchase("candy", stock, 75)
    assert status == "dispensed"
    assert change == []
    assert stock["candy"] == 3


def test_purchase_success_with_change():
    stock = {"cola": 5}
    status, change = purchase("cola", stock, 200)
    assert status == "dispensed"
    assert change == [50]
    assert stock["cola"] == 4

