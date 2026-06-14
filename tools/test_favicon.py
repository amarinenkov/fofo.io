import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class FaviconTest(unittest.TestCase):
    def test_index_declares_modern_favicon_links(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        expected = [
            '<link rel="icon" href="/favicon.ico" sizes="any">',
            '<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">',
            '<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">',
        ]
        for snippet in expected:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, html)

    def test_favicon_assets_exist(self):
        for path in ("favicon.ico", "assets/favicon-32.png", "assets/apple-touch-icon.png"):
            with self.subTest(path=path):
                asset = ROOT / path
                self.assertTrue(asset.is_file(), f"{path} is missing")
                self.assertGreater(asset.stat().st_size, 0, f"{path} is empty")


if __name__ == "__main__":
    unittest.main()
