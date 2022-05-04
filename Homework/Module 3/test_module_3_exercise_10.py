class TestPhraseLength:
    def test_phrase_length(self):
        phrase = input("Set a phrase:")

        assert len(phrase) < 15, f"Phrase has length more 15 symbols"
