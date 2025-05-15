class CellModel:
    """A model representing a display cell with a title, content, and color-coded border."""

    def __init__(self, title: str, content: str, color: str = "blue") -> None:
        """
        Initialize a CellModel instance.

        Args:
            title (str): The cell title.
            content (str): The cell content.
            color (str, optional): The top border color. Defaults to "blue".
        """
        self.title = title
        self.content = content
        self.color = color

    def __str__(self) -> str:
        """
        Generate an HTML string representation of the cell.

        Returns:
            str: HTML snippet.
        """
        return f"""
<div class="data-display-cell" style="border-top: 1px solid {self.color};">
    <h3>{self.title}</h3>
    <p>{self.content}</p>
</div>
        """
