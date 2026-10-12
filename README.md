# Password Cracking and Hashing Algorithms

An educational, local-only project demonstrating password hashing, per-password salts, and **bounded guessing against a synthetic sample hash**. It helps learners understand why fast unsalted hashes are unsuitable for password storage and why salts and purpose-built password-hashing algorithms matter.

> **Safety scope:** This project operates only on a built-in synthetic example generated for the demo. It does not read system password files, harvest credentials, or attack real accounts/hashes. The demo search space is deliberately tiny and capped.

## Objectives
- Understand cryptographic hashes and password verification.
- Demonstrate the purpose of a unique random salt.
- Compare a tiny dictionary search with a bounded brute-force demonstration.
- Record reproducible results in a JSON report.
- Explain why production systems should use Argon2id, scrypt, or bcrypt rather than plain SHA-256 for password storage.

## Tools
- Python 3.10+
- Standard library: `hashlib`, `secrets`, `itertools`, `json`, `argparse`
- Optional external tools for further supervised study: Hashcat and John the Ripper. **They are not invoked by this implementation.**

## Quick start

Windows:
```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python src\password_lab.py --out reports\demo.json
```

Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python src/password_lab.py --out reports/demo.json
```

Run tests:
```bash
python -m unittest discover -s tests -v
```

## How the demo works
1. Creates a synthetic sample password from a small fixed demo set.
2. Generates a random 16-byte salt.
3. Computes `SHA-256(salt || password)` for demonstration.
4. Tests a small, hard-coded demonstration wordlist.
5. Runs a bounded brute-force search over a tiny alphabet and maximum length.
6. Writes only the sample label, salt, hash, attempt counts, and outcome to JSON. The report does not store the sample password.

## Important cryptographic distinction
SHA-256 is a general-purpose cryptographic hash, not a password-storage function. It is fast by design, which makes large-scale guessing cheaper. Salting prevents identical passwords from having identical stored hashes and frustrates precomputed rainbow tables, but **salting alone does not make a fast hash slow**. For real applications, use a maintained password-hashing library implementing Argon2id, scrypt, or bcrypt with suitable parameters.

## Methodology
1. Define an isolated learning objective and use synthetic credentials only.
2. Generate a unique random salt for the demonstration.
3. Hash the synthetic password and retain the salt alongside the hash.
4. Reproduce verification by hashing each candidate with the same salt.
5. Compare the candidate hash with the stored demo hash using constant-time comparison.
6. Keep dictionary and brute-force search spaces small and bounded.
7. Record attempt counts and the final status in JSON.
8. Discuss limitations and compare the demonstration with production password-storage practices.

## Requirements
- Python 3.10 or newer
- No third-party dependencies
- Local execution; no network access required

## Repository contents
- `src/password_lab.py` — demo implementation
- `docs/METHODOLOGY.md` — procedure and rationale
- `docs/REQUIREMENTS.md` — functional and non-functional requirements
- `docs/CRYPTOGRAPHY_NOTES.md` — hashing, salts, and safe storage
- `docs/TEST_PLAN.md` — verification plan
- `tests/` — automated tests
- `reports/` — sample report output location

## Limitations
- The tiny search is illustrative and is not a password-auditing engine.
- Hashcat and John the Ripper are documented as related tools but are not integrated or executed.
- No real hash files, operating-system credentials, network services, or accounts are accessed.
- The sample uses salted SHA-256 to demonstrate mechanics; do not copy it as a production password-storage design.
