# L6_L7_30 — Vending Machine

Lab 6: Code and Branch Coverage Analysis

## Deliverables

| Deliverable | File |
|---|---|
| **Code Coverage Test Cases** | [`CodeCoverageTest_vending_machine.py`](CodeCoverageTest_vending_machine.py) |
| **Branch Coverage Test Cases** | [`BranchCoverageTest_vending_machine.py`](BranchCoverageTest_vending_machine.py) |
| **Code Coverage Screenshot** | [`code_coverage_screenshot.png`](code_coverage_screenshot.png) |
| **Branch Coverage Screenshot** | [`branch_coverage_screenshot.png`](branch_coverage_screenshot.png) |
| **Code Coverage Analysis & Report** | [`Code_Coverage_Report.md`](Code_Coverage_Report.md) |
| **Branch Coverage Analysis & Report** | [`Branch_Coverage_Report.md`](Branch_Coverage_Report.md) |

## Commands to Run Coverage

### 1. Code Coverage
```powershell
coverage run -m pytest CodeCoverageTest_vending_machine.py
coverage report -m
```

### 2. Branch Coverage
```powershell
coverage run --branch -m pytest BranchCoverageTest_vending_machine.py
coverage report -m
```
