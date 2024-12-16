import xml.etree.ElementTree as ET
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def remove_comments_from_xml(file_path: str):
    """
    Removes all comments from an XML file and updates the file in place.

    Args:
        file_path (str): Path to the XML file to be updated.
    """
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Recursive function to remove comments
        def remove_comments(elem):
            for child in list(elem):
                if isinstance(child.tag, str):
                    # If the child is an element, recurse
                    remove_comments(child)
                else:
                    # If the child is not an element (likely a comment), remove it
                    elem.remove(child)

        # Remove comments starting from the root
        remove_comments(root)

        # Write the cleaned XML back to the same file
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        logger.info(f"Comments removed and XML file updated in place at '{file_path}'.")

    except ET.ParseError as e:
        logger.error(f"Error parsing XML file: {e}")
    except FileNotFoundError:
        logger.error(f"File '{file_path}' not found.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

# Example usage
file_path = "E:/Python/example.xml"
remove_comments_from_xml(file_path)
