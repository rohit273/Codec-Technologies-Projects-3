import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from password_lab import hash_password, verify_candidate, dictionary_demo, bounded_bruteforce_demo, run_demo

class PasswordLabTests(unittest.TestCase):
    def test_hash_is_deterministic_for_same_salt(self):
        self.assertEqual(hash_password("synthetic", b"salt"), hash_password("synthetic", b"salt"))

    def test_salt_changes_digest(self):
        self.assertNotEqual(hash_password("synthetic", b"salt-one"), hash_password("synthetic", b"salt-two"))

    def test_verify_candidate(self):
        salt = b"salt"
        expected = hash_password("b7", salt)
        self.assertTrue(verify_candidate("b7", salt, expected))
        self.assertFalse(verify_candidate("nope", salt, expected))

    def test_dictionary_demo(self):
        salt = b"salt"
        expected = hash_password("b7", salt)
        result = dictionary_demo(salt, expected, ["nope", "b7"])
        self.assertTrue(result["found"])
        self.assertEqual(result["attempts"], 2)

    def test_bruteforce_bound(self):
        with self.assertRaises(ValueError):
            bounded_bruteforce_demo(b"salt", "0" * 64, alphabet="ab", max_length=5)

    def test_report_does_not_include_demo_password_field(self):
        report = run_demo()
        self.assertNotIn("password", report)
        self.assertEqual(report["scope"], "synthetic local demonstration only")

if __name__ == "__main__":
    unittest.main()
