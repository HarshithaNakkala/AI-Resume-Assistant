from app.jd_parser import clean_jd, tokenize_jd


def test_clean_jd():
    text = "Python Developer!!!"
    result = clean_jd(text)

    assert result == "python developer"


def test_tokenize_jd():
    text = "python developer"
    result = tokenize_jd(text)

    assert "python" in result
    assert "developer" in result