class LineGraphModel:
    """
    A model representing data for a multi-line graph visualization.

    Attributes:
        canvas_id (str): The HTML canvas element ID for rendering.
        title (str): The title of the graph.
        x_vals (list): The x-axis values shared by all plots.
        plots (tuple): One or more plot datasets to render.
    """

    def __init__(self, canvas_id, title, x_vals, *plots):
        """
        Initialize the LineGraphModel.

        Args:
            canvas_id (str): ID of the canvas element in HTML.
            title (str): Title of the graph.
            x_vals (list): X-axis values.
            *plots: One or more plot objects or datasets.
        """
        self.canvas_id = canvas_id
        self.title = title
        self.x_vals = x_vals
        self.plots = plots

    def __len__(self):
        """
        Get the number of plots in the graph.

        Returns:
            int: Number of plots.
        """
        return len(self.plots)

    def __str__(self):
        """
        Return a human-readable summary of the graph model.

        Returns:
            str: Multi-line string describing the graph contents.
        """
        plot_descriptions = []
        for idx, plot in enumerate(self.plots, start=1):
            plot_descriptions.append(f"Plot {idx}: {plot}")

        return (
            f"LineGraphModel(\n"
            f"  canvas_id={self.canvas_id!r},\n"
            f"  title={self.title!r},\n"
            f"  x_vals={self.x_vals!r},\n"
            "  plots=[\n    " + "\n    ".join(plot_descriptions) + "\n  ]\n"
            ")"
        )
