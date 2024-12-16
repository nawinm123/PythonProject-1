import os
import unittest
import xml.etree.ElementTree as ET

from file_remove import remove_comments_from_xml  # Replace with your script's module name


class TestRemoveCommentsFromXML(unittest.TestCase):

    def setUp(self):
        """Set up test files before each test."""
        self.test_file = "test.xml"
        self.valid_xml_with_comments = """<?xml version="1.0"?>
        <root>
            <!-- This is a comment -->
            <child>Content</child>
            <!-- Another comment -->
        </root>"""
        self.expected_xml_no_comments = """<?xml version="1.0"?>
<root>
    <child>Content</child>
</root>"""

        self.invalid_xml = "<root><child>Content</child"  # Missing closing angle bracket

        # Create the test XML file
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(self.valid_xml_with_comments)

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def normalize_xml(self, file_path):
        """Normalize XML by removing unnecessary whitespace."""
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Convert to string, remove extra spaces/newlines, and reformat to a consistent structure
        rough_string = ET.tostring(root, encoding="unicode")
        # Strip unwanted leading/trailing whitespace and normalize internal whitespace
        return ' '.join(rough_string.split())

    def test_remove_comments(self):
        """Test that comments are correctly removed from a valid XML file."""
        remove_comments_from_xml(self.test_file)

        # Normalize the output XML for comparison
        normalized_output = self.normalize_xml(self.test_file)
        normalized_expected = self.normalize_xml_from_string(self.expected_xml_no_comments)

        self.assertEqual(normalized_output, normalized_expected)

    def test_invalid_xml(self):
        """Test behavior when the XML file is invalid."""
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(self.invalid_xml)

        with self.assertLogs(level='ERROR') as log:
            remove_comments_from_xml(self.test_file)

        self.assertIn("Error parsing XML file", log.output[0])

    def test_file_not_found(self):
        """Test behavior when the file does not exist."""
        non_existent_file = "nonexistent.xml"
        with self.assertLogs(level='ERROR') as log:
            remove_comments_from_xml(non_existent_file)

        self.assertIn(f"File '{non_existent_file}' not found.", log.output[0])

    def normalize_xml_from_string(self, xml_string):
        """Normalize an XML string to remove unnecessary whitespace."""
        tree = ET.ElementTree(ET.fromstring(xml_string))
        return ' '.join(ET.tostring(tree.getroot(), encoding="unicode").split())


if __name__ == "__main__":
    unittest.main()
