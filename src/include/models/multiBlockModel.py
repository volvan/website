class MultiBlockModel:
    """
    A model representing a block with a title and multi-item content.

    Attributes:
        title (str): The title of the block.
        content (Any): The content associated with the block.
    """

    def __init__(self, title, content):
        """
        Initialize a MultiBlockModel instance.

        Args:
            title (str): The block title.
            content (Any): The associated content (e.g., list, dict, text).
        """
        self.title = title
        self.content = content
