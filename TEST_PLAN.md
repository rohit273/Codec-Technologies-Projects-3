# Test Plan

| ID | Test | Expected result |
|---|---|---|
| P-01 | Same password and salt | Same digest |
| P-02 | Same password with different salts | Different digest |
| P-03 | Correct candidate | Verification succeeds |
| P-04 | Incorrect candidate | Verification fails |
| P-05 | Tiny dictionary contains demo candidate | Candidate found |
| P-06 | Brute-force limits exceeded | ValueError |
| P-07 | Run CLI | JSON report created |
| P-08 | Report review | Password itself is not stored |
