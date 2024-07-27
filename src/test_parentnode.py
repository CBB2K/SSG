import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_parentnode_to_html(self):
        # Setup
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        # Execute
        result = node.to_html()

        # Verify
        expected = "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        self.assertEqual(result, expected)

    def test_missing_tag_raises_value_error(self):
        # Setup
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
            ],
        )

        # Verify
        with self.assertRaises(ValueError) as e:
            # Execute
            node.to_html()
        
        # Verify
        self.assertEqual(str(e.exception), "No tag")

    def test_missing_children_raises_value_error(self):
        # Setup and Execute
        with self.assertRaises(ValueError) as e:
            ParentNode("p", None)
        
        # Verify
        self.assertEqual(str(e.exception), "Children must be provided")

    def test_no_children_raises_value_error_in_to_html(self):
        # Setup
        node = ParentNode("p", [])

        # Verify
        with self.assertRaises(ValueError) as e:
            # Execute
            node.to_html()
        
        # Verify
        self.assertEqual(str(e.exception), "No children")

    def test_nested_parentnode_to_html(self):
        nested_node = ParentNode(
            "div",
            [
                LeafNode("h1", "Header"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text in paragraph"),
                    ]
                ),
            ],
        )
        result = nested_node.to_html()
        expected = "<div><h1>Header</h1><p><b>Bold text in paragraph</b></p></div>"
        self.assertEqual(result, expected)

    def test_mixed_children(self):
        # Setup
        node = ParentNode(
            "div",
            [
                LeafNode("h1", "Header"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, " and some normal text."),
                    ]
                ),
            ],
        )

        # Execute
        result = node.to_html()

        # Verify
        expected = "<div><h1>Header</h1><p><b>Bold text</b> and some normal text.</p></div>"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

