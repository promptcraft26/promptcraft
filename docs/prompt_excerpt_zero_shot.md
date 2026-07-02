# Zero-Shot Prompt Excerpt (Sanitized)

This excerpt illustrates the structure of the zero-shot prompt family without
releasing the full private prompt asset.

```text
You are given a Solidity contract and a target function summary.
Generate test cases in a strict CSV-compatible structure.
Focus on:
1. normal behavior,
2. edge and boundary conditions,
3. exception-triggering scenarios,
4. business-rule-sensitive cases.
Return only structured test cases with fields:
Test Case ID, Function Under Test, Description, Pre-State Setup,
Input Parameters, Expected Outcome, Category, Priority.
```
