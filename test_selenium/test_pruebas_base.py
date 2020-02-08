def test_validando_url():
    assert 'http://www.google.com'.startswith('http')


def test_validando_sitio_seguro():
    assert 'http://www.google.com'.startswith('https'), "El sitio no cuenta con certificado SSL"