from src.parser import parse_quotes

def test_parse_quotes():
    html = """
    <div class="quote">
        <span class="text">"Hello World"</span>
        <small class="author">John Doe</small>
    </div>
    """
    quotes = parse_quotes(html)
    assert len(quotes) == 1
    assert quotes[0]['author'] == 'John Doe'
