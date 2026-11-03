import pytest
from vending_machine import select_item, make_change, purchase


def test_invalid_item():
    assert select_item("water", {}, 100) == "invalid"


def test_sold_out_item():
    assert select_item("cola", {"cola": 0}, 150) == "sold_out"


def test_insufficient_credit():
    assert select_item("chips", {"chips": 5}, 50) == "insufficient"


def test_select_item_ok():
    assert select_item("candy", {"candy": 5}, 75) == "ok"


def test_no_change_needed():
    assert make_change(0) == []


def test_make_change_standard():
    assert make_change(125) == [100, 25]


def test_purchase_status_failure():
    stock = {"chips": 0}
    status, change = purchase("chips", stock, 100)
    assert status == "sold_out"
    assert change == []


def test_purchase_successful():
    stock = {"cola": 2}
    status, change = purchase("cola", stock, 200)
    assert status == "dispensed"
    assert change == [50]
    assert stock["cola"] == 1

