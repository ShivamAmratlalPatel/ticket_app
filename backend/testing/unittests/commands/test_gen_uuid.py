import unittest


class TestGenUUID(unittest.TestCase):
    def test_gen_uuid(self):
        from backend.src.commands import generate_uuid
        from uuid import UUID

        result = generate_uuid()

        self.assertIsInstance(result, UUID)
        result = str(result)
        self.assertEqual(len(result), 36)
        self.assertEqual(result[14], "4")
        self.assertIn(result[19], ["8", "9", "a", "b"])
        self.assertEqual(result[8], "-")
        self.assertEqual(result[13], "-")
        self.assertEqual(result[18], "-")
        self.assertEqual(result[23], "-")


if __name__ == "__main__":
    unittest.main()
