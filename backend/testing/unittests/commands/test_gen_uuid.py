"""Tests for generate_uuid() command."""
import unittest


class TestGenUUID(unittest.TestCase):
    """Test generate_uuid() command."""

    def test_gen_uuid(self: "TestGenUUID") -> None:
        """
        Test generate_uuid() command.

        Test that generate_uuid() returns a UUID with the correct format.

        Args:
        ----
            self (TestGenUUID): instance of TestGenUUID

        Returns:
        -------
            None
        """
        from uuid import UUID

        from backend.src.commands import generate_uuid

        result = generate_uuid()

        assert isinstance(result, UUID)
        result = str(result)
        uuid_length = 36
        assert len(result) == uuid_length
        assert result[14] == "4"
        assert result[19] in ["8", "9", "a", "b"]
        assert result[8] == "-"
        assert result[13] == "-"
        assert result[18] == "-"
        assert result[23] == "-"


if __name__ == "__main__":
    unittest.main()
