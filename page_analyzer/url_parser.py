from urllib.parse import urlsplit, urlunsplit


def url_parse(url):
    scheme, netloc, path, qs, anchor = urlsplit(url)
    path = ''
    qs = ''
    anchor = ''
    return (urlunsplit((scheme, netloc, path, qs, anchor)))