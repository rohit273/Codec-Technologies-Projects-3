#!/usr/bin/env python3
"""Safe password hashing demonstration using only a synthetic sample."""
import argparse
import hashlib
import hmac
import itertools
import json
import secrets
from datetime import datetime, timezone
from pathlib import Path

DEMO_PASSWORD = "b7"  # Synthetic demonstration value, not a user credential.
DEMO_WORDLIST = ("hello", "password", "abc", "b7", "welcome")
DEMO_ALPHABET = "ab7"
DEMO_MAX_LENGTH = 2

def hash_password(password: str, salt: bytes) -> str:
    """Educational salted SHA-256; not recommended for production storage."""
    return hashlib.sha256(salt + password.encode("utf-8")).hexdigest()

def verify_candidate(candidate: str, salt: bytes, expected_hash: str) -> bool:
    candidate_hash = hash_password(candidate, salt)
    return hmac.compare_digest(candidate_hash, expected_hash)

def dictionary_demo(salt: bytes, expected_hash: str, wordlist=DEMO_WORDLIST) -> dict:
    attempts = 0
    for candidate in wordlist:
        attempts += 1
        if verify_candidate(candidate, salt, expected_hash):
            return {"found": True, "attempts": attempts, "method": "dictionary"}
    return {"found": False, "attempts": attempts, "method": "dictionary"}

def bounded_bruteforce_demo(salt: bytes, expected_hash: str,
                            alphabet=DEMO_ALPHABET, max_length=DEMO_MAX_LENGTH) -> dict:
    if not alphabet or max_length < 1 or max_length > 4:
        raise ValueError("Use a non-empty alphabet and max_length from 1 to 4.")
    attempts = 0
    for length in range(1, max_length + 1):
        for chars in itertools.product(alphabet, repeat=length):
            attempts += 1
            candidate = "".join(chars)
            if verify_candidate(candidate, salt, expected_hash):
                return {"found": True, "attempts": attempts, "method": "bounded_bruteforce"}
    return {"found": False, "attempts": attempts, "method": "bounded_bruteforce"}

def run_demo() -> dict:
    salt = secrets.token_bytes(16)
    expected_hash = hash_password(DEMO_PASSWORD, salt)
    dictionary = dictionary_demo(salt, expected_hash)
    brute_force = bounded_bruteforce_demo(salt, expected_hash)
    return {
        "project": "Password Cracking and Hashing Algorithms",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "synthetic local demonstration only",
        "algorithm_demo": "SHA-256(salt || password)",
        "salt_hex": salt.hex(),
        "stored_hash_sha256": expected_hash,
        "salt_length_bytes": len(salt),
        "dictionary_result": dictionary,
        "bounded_bruteforce_result": brute_force,
        "production_note": "Use Argon2id, scrypt, or bcrypt through a maintained library for real password storage. This SHA-256 example is educational only.",
        "external_tools": {"hashcat": "not integrated", "john_the_ripper": "not integrated"}
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("reports/demo.json"),
                        help="Output JSON report path (default: reports/demo.json)")
    args = parser.parse_args()
    report = run_demo()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Demo complete. Dictionary found: {report['dictionary_result']['found']}; "
          f"bounded search found: {report['bounded_bruteforce_result']['found']}")
    print(f"Report written to {args.out}")

if __name__ == "__main__":
    main()
