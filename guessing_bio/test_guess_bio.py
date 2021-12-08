"""
Testing Bio
"""
import pytest
from guessing_bio import GuessBio


class TestBio:
    """
    Tests for Guess Bio
    """

    def test_names(self):
        """
        Test if you can enter first and second names
        :return: None
        """
        guess_bio_obj = GuessBio("Joseph", "Njeri")
        assert guess_bio_obj.first_name == "Joseph"
        assert guess_bio_obj.last_name == "Njeri"

    def test_guess_bio(self):
        guess_bio_dict = GuessBio("Joseph", "Njeri").guess_bio()
        assert isinstance(guess_bio_dict["address"], str)
        assert isinstance(guess_bio_dict["phone"], str)
        assert isinstance(guess_bio_dict["email"], str)

    def test_wrong_instance(self):
        guessing_bio = GuessBio(["Joseph"], ["Njeri"])
        try:
            guessing_bio.guess_bio()
        except:
            with pytest.raises(TypeError) as type_error:
                guessing_bio.guess_bio()
            assert "['Joseph'] must be a string" in str(type_error.value)
