import unittest

from .you_get_plugin import extract_urls


class TestExtractUrls(unittest.TestCase):
    def test_extract_urls(self):
        content = "Check out this tweet: https://twitter.com/user/status/123456"
        expected_urls = ["https://twitter.com/user/status/123456"]
        self.assertEqual(extract_urls(content), expected_urls)

        content = "Here is a link from x.com: https://x.com/tomeinohito/status/1796144897721835717"
        expected_urls = ["https://x.com/tomeinohito/status/1796144897721835717"]
        self.assertEqual(extract_urls(content), expected_urls)

        content = "No URLs in this content"
        expected_urls = []
        self.assertEqual(extract_urls(content), expected_urls)

        content = "Here have many urls: https://twitter.com/user/status/123456, https://x.com/post/status/789, Yes!"
        expected_urls = [
            "https://twitter.com/user/status/123456",
            "https://x.com/post/status/789",
        ]
        self.assertEqual(extract_urls(content), expected_urls)


if __name__ == "__main__":
    unittest.main()
