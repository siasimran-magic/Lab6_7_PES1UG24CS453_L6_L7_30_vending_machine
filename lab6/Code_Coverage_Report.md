# Code Coverage Analysis & Report

**Course/Lab**: Lab 6 — Code and Branch Coverage Analysis  
**Module Under Test**: `vending_machine.py`  
**Test Suite**: `CodeCoverageTest_vending_machine.py`  
**Target Requirement**: $\ge 90\%$ Code (Line) Coverage  
**Outcome**: **90% Line Coverage** on `vending_machine.py` (**95% Total Suite Coverage**)

---

## 1. Introduction & Concepts
Code coverage (or line coverage) measures the percentage of executable statements in the source code executed during test execution:
$$\text{Line Coverage} = \frac{\text{Executed Lines}}{\text{Total Executable Lines}} \times 100\%$$

While line coverage ensures that lines of code are visited at least once, it does not guarantee that every logical branch or boundary decision has been thoroughly evaluated.

---

## 2. Initial Baseline Analysis
The initial starter test suite (`test_vending_machine.py`) included only 2 basic tests:
- `test_invalid_item`
- `test_no_change_needed`

### Initial Coverage Metrics:
- **Statements**: 30
- **Missed**: 17
- **Coverage**: **43%**
- **Untested Lines**: 8–12, 17, 21–22, 24, 29–36

---

## 3. Test Suite Design for Code Coverage ($\ge 90\%$)
To achieve the required threshold of at least 90% statement coverage, targeted test cases were constructed in `CodeCoverageTest_vending_machine.py`:

| Test Name | Function | Purpose / Path Tested |
|---|---|---|
| `test_invalid_item` | `select_item` | Item not present in catalog $\rightarrow$ returns `"invalid"` (Lines 6–7) |
| `test_sold_out_item` | `select_item` | Item has 0 stock $\rightarrow$ returns `"sold_out"` (Lines 8–9) |
| `test_insufficient_credit` | `select_item` | Deposited credit less than price $\rightarrow$ returns `"insufficient"` (Lines 10–11) |
| `test_select_item_ok` | `select_item` | Valid item with sufficient stock and credit $\rightarrow$ returns `"ok"` (Line 12) |
| `test_no_change_needed` | `make_change` | Zero change amount requested $\rightarrow$ returns `[]` (Lines 15, 18, 19, 23, 25) |
| `test_make_change_standard` | `make_change` | Standard change amount ($125 \rightarrow [100, 25]$) (Lines 20–22) |
| `test_purchase_status_failure` | `purchase` | Purchase when item selection fails $\rightarrow$ returns status and `[]` (Lines 29–31) |
| `test_purchase_successful` | `purchase` | Successful transaction dispensing item and returning change (Lines 28–30, 32, 35–36) |

---

## 4. Execution Commands & Terminal Output

### Commands
```powershell
cd lab6
coverage run -m pytest CodeCoverageTest_vending_machine.py
coverage report -m
```

### Terminal Output Summary
```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\siasi\Downloads\Lab6\L6_L7_30_vending_machine\lab6
plugins: anyio-4.14.0
collected 8 items

CodeCoverageTest_vending_machine.py ........                             [100%]

============================== 8 passed in 0.12s ==============================
Name                                  Stmts   Miss  Cover   Missing
-------------------------------------------------------------------
CodeCoverageTest_vending_machine.py      25      0   100%
vending_machine.py                       30      3    90%   17, 24, 34
-------------------------------------------------------------------
TOTAL                                    55      3    95%
```

---

## 5. Untested Paths & Gap Analysis
Although 90% statement coverage was achieved, three critical execution lines remained unexecuted:
1. **Line 17 (`raise ValueError("negative amount")`)**:
   - Negative amounts passed to `make_change()` were not tested.
2. **Line 24 (`return None`)**:
   - Amounts where exact change cannot be formed from available coins (`[100, 50, 25, 10, 5]`) were not tested.
3. **Line 34 (`return "no_exact_change", []`)**:
   - When `purchase()` attempts to make change and receives `None`, handling was untested.

This gap clearly demonstrates why branch coverage analysis is essential to discover untested alternate logical paths.

---

## 6. Screenshot Deliverable
The terminal output screenshot verifying $\ge 90\%$ code coverage is saved at:
- `lab6/code_coverage_screenshot.png`
