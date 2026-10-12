# Methodology

## 1. Scope
The project demonstrates password-hash concepts in an isolated, local environment. It uses one synthetic sample and a small, predefined search space only.

## 2. Salt generation
A 16-byte salt is generated with Python's `secrets` module. In real systems, salts are normally stored beside the hash and are not treated as secret.

## 3. Hash creation
The demo computes SHA-256 over `salt || password`. This makes the role of the salt easy to inspect, but SHA-256 is too fast for production password storage.

## 4. Candidate verification
Each candidate is hashed with the same salt and compared with the stored hash using `hmac.compare_digest`, a constant-time comparison function.

## 5. Dictionary demonstration
A small fixed wordlist is checked sequentially. The program records the number of attempts, not the recovered sample password.

## 6. Bounded brute-force demonstration
The program enumerates strings from a tiny alphabet with maximum length two. A hard cap prevents the example from expanding into a large search job.

## 7. Reporting
A JSON report contains the salt, hash, attempt counts, method results, scope, and production warning. The synthetic password itself is not written to the report.

## 8. Evaluation
Automated tests check salted-hash consistency, salt-dependent output, candidate verification, bounded-search limits, and report structure.

## 9. Interpretation
The demo illustrates how guessable passwords can be found in a tiny search space. It does not represent real-world cracking speed or the strength of any real credential.
