"""Validate generated pages and guard against publishing template content."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


class Navigation(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_nav = False
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == "nav":
            self.in_nav = True
        if self.in_nav and tag == "a":
            href = dict(attrs).get("href", "")
            parsed = urlparse(href)
            if href and not parsed.netloc and not parsed.fragment:
                self.links.add(parsed.path)

    def handle_endtag(self, tag):
        if tag == "nav":
            self.in_nav = False


site = Path("_site")
pages = {
    "about": site / "index.html",
    "blog": site / "blog/index.html",
    "publications": site / "publications/index.html",
}
for name, path in pages.items():
    assert path.is_file(), f"Missing {name} page: {path}"
    html = path.read_text(encoding="utf-8")
    nav = Navigation()
    nav.feed(html)
    assert nav.links == {"/", "/blog/", "/publications/"}, (
        f"Unexpected navigation on {name}: {nav.links}"
    )
    for demo in ("Albert Einstein", "the_godfather", "al-folio: a simple theme"):
        assert demo not in html, f"Template content on {name}: {demo}"

home = pages["about"].read_text(encoding="utf-8")
assert "wenhuiwu@mail.sdu.edu.cn" in home, "Public email is missing"
assert "github.com/whwu07" in home, "GitHub profile is missing"
assert "prof_pic" in home, "Homepage photograph is missing"
publications = pages["publications"].read_text(encoding="utf-8")
assert "Improved Linear Key Recovery Attacks on PRESENT" in publications
assert "10.1109/TIT.2024.3474701" in publications
assert "QARMAv2" not in publications, "Accepted work is not a published paper"
blog = pages["blog"].read_text(encoding="utf-8")
assert 'class="post-title"' not in blog, "The blog should remain empty"
for removed in ("projects", "repositories", "cv", "teaching", "people", "books", "news", "plugins"):
    assert not (site / removed / "index.html").exists(), f"Unused page still published: {removed}"
for removed in ("assets/json/resume.json", "assets/pdf/example_pdf.pdf", "assets/img/prof_pic_color.png"):
    assert not (site / removed).exists(), f"Template asset still published: {removed}"

print("Personal website checks passed.")
