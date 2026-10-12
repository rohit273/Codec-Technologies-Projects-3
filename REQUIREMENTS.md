# Requirements

## Functional requirements
- FR-01 Generate a cryptographically random salt for each demo run.
- FR-02 Compute a salted demonstration hash for a synthetic sample.
- FR-03 Verify candidate passwords by hashing with the same salt.
- FR-04 Demonstrate a small fixed dictionary search.
- FR-05 Demonstrate brute-force enumeration with strict length and alphabet limits.
- FR-06 Export results and metadata to JSON.
- FR-07 State clearly that Hashcat and John the Ripper are not integrated.

## Non-functional requirements
- NFR-01 Python 3.10 or newer.
- NFR-02 Use only Python standard-library modules.
- NFR-03 Work offline and avoid accessing real accounts or credential stores.
- NFR-04 Keep search bounds small and explicit.
- NFR-05 Use readable output and automated tests.
- NFR-06 Do not include recovered passwords in the report.

## Out of scope
- Cracking real user hashes or system password files.
- Attacking online login forms or accounts.
- GPU cracking or integration with Hashcat/John the Ripper.
- Production password storage using raw SHA-256.
