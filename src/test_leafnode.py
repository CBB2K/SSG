import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_tag_plus_text(self):
        leaf1 = LeafNode("p", "This is a paragraph")
        self.assertEqual(leaf1.to_html(), "<p>This is a paragraph</p>")

    def test_tag_plus_attrs(self):
        leaf2 = LeafNode("a", "Click me!", {"href": "https://example.com"})
        self.assertEqual(leaf2.to_html(), '<a href="https://example.com">Click me!</a>')

    def test_no_tag_text(self):
        leaf3 = LeafNode(None, "Just text without a tag.")
        self.assertEqual(leaf3.to_html(), "Just text without a tag.")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", "")

    def test_empty_attrs(self):
        leaf4 = LeafNode("span", "Some text", {})
        self.assertEqual(leaf4.to_html(), "<span>Some text</span>")


if __name__ == "__main__":
    unittest.main()
