class BlockModel:
    """
    A simple data container model representing a titled block with a value.

    Attributes:
        title (str): The title or label for the block.
        value (Any): The associated value for the block.
    """

    def __init__(self, title, value):
        """
        Initialize a BlockModel instance.

        Args:
            title (str): The title of the block.
            value (Any): The value associated with the block.
        """
        self.title = title
        self.value = value
