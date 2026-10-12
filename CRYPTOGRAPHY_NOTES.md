# Cryptography Notes

## Hashing
A cryptographic hash maps input data to a fixed-size digest. SHA-256 returns a 256-bit digest. It is designed to be fast, which is useful for integrity checking but undesirable for password storage when attackers can guess many candidates.

## Salt
A salt is a random, per-password value stored with the password hash. It prevents identical passwords from automatically producing identical stored hashes and makes precomputed rainbow-table attacks less useful. A salt does not need to be secret.

## Password hashing
Use a dedicated, tunable password-hashing function such as Argon2id, scrypt, or bcrypt, with parameters chosen for the application's threat model and updated as hardware changes. Use a maintained library rather than implementing these algorithms yourself.

## Brute force and dictionary search
- **Dictionary search:** tries candidates from a list of likely passwords.
- **Brute force:** enumerates all candidates in a defined character space.
- **Bounded search:** limits alphabet and candidate length to keep a demonstration manageable.

## Hashcat and John the Ripper
These are established password-auditing tools. They are not invoked by this repository's code. Use them only in a properly authorized lab and with synthetic or explicitly authorized test hashes.

## Common misconceptions
- Hashing is not encryption: a hash is not meant to be decrypted.
- A salt is not a pepper. A pepper is a separate secret kept outside the password database.
- Salting does not make a weak password strong.
- Fast general-purpose hashes such as raw SHA-256 should not be used alone for password storage.
