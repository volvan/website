class ValidationLogic:
    """A utility class containing static methods for basic data validation."""

    @staticmethod
    def list_is_unique(input_list):
        """
        Check if all elements in a list are unique.

        Args:
            input_list (list): The list to validate.

        Returns:
            bool: True if all elements are unique, False otherwise.
        """
        input_set = set(input_list)
        return len(input_set) == len(input_list)
