import pytest
from motivational_quotes import MotivationalQuotes

@pytest.fixture
def motivational_quotes_instance():
    return MotivationalQuotes()

def test_print_random_quote(motivational_quotes_instance, capsys, monkeypatch):
    # Mock the random.choice function to return a known value
    monkeypatch.setattr('random.choice', lambda x: 'Test Motivational Quote')

    # Call the method that prints the quote
    motivational_quotes_instance.print_random_quote()

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert that the captured output contains the expected quote
    assert 'Test Motivational Quote' in captured.out.strip()
