class HostModel:
    """
    A dynamic model for storing host-related attributes using keyword arguments.

    Attributes:
        All attributes are dynamically assigned from keyword arguments.
    """

    def __init__(self, **kwargs):
        """
        Initialize a HostModel instance with arbitrary attributes.

        Args:
            **kwargs: Arbitrary keyword arguments to set as attributes.
        """
        for key, item in kwargs.items():
            setattr(self, key, item)

    def __str__(self) -> str:
        """
        Return a string representation of the host and its attributes.

        Returns:
            str: A formatted string listing all attribute keys and values.
        """
        ret_str = "\n"
        for key, item in self.__dict__.items():
            ret_str += f"{key}: {item}\n"
        return ret_str
