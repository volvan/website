from .DBData import DBData


class DataWrapper:
    """A wrapper class around DBData to provide country-specific data queriesfor hosts, ports, services, and metadata."""

    def __init__(self):
        """Initialize the DataWrapper with a DBData instance."""
        self.dbData = DBData()

    def get_country_codes(self):
        """
        Retrieve a list of available country codes in the dataset.

        Returns:
            list: A list of country code strings.
        """
        return self.dbData.get_country_codes()

    def get_total_alive_hosts(self, country_code):
        """
        Get the total number of alive hosts for a given country.

        Args:
            country_code (str): The country code to query.

        Returns:
            int: Total number of alive hosts.
        """
        return self.dbData.get_total_alive_hosts(country_code)

    def get_ips_count(self, country_code):
        """
        Get the number of unique IP addresses for a given country.

        Args:
            country_code (str): The country code to query.

        Returns:
            int: Number of IP addresses.
        """
        return self.dbData.get_ips_count(country_code)

    def get_total_open_ports(self, country_code):
        """
        Get the total number of open ports for a given country.

        Args:
            country_code (str): The country code to query.

        Returns:
            int: Total number of open ports.
        """
        return self.dbData.get_total_open_ports(country_code)

    def get_port_amount(self, country_code):
        """
        Get the number of distinct open ports for a given country.

        Args:
            country_code (str): The country code to query.

        Returns:
            int: Number of distinct open ports.
        """
        return self.dbData.get_port_amount(country_code)

    def get_total_open_ports_plot(self, country_code):
        """
        Retrieve data for plotting total open ports in a given country.

        Args:
            country_code (str): The country code to query.

        Returns:
            Any: Plotting data (depends on DBData's implementation).
        """
        return self.dbData.get_total_open_ports_plot(country_code)

    def get_unique_open_ports(self, country_code):
        """
        Get the list or count of unique open ports in a given country.

        Args:
            country_code (str): The country code to query.

        Returns:
            list or int: Unique open ports data.
        """
        return self.dbData.get_unique_open_ports(country_code)

    def get_products_count(self, country_code):
        """
        Get the number of distinct products identified in a given country.

        Args:
            country_code (str): The country code to query.

        Returns:
            int: Product count.
        """
        return self.dbData.get_products_count(country_code)

    def get_services_count(self, country_code):
        """
        Get the number of distinct services detected in a given country.

        Args:
            country_code (str): The country code to query.

        Returns:
            int: Services count.
        """
        return self.dbData.get_services_count(country_code)

    def get_versions_count(self, country_code):
        """
        Get the number of distinct software versions detected in a given country.

        Args:
            country_code (str): The country code to query.

        Returns:
            int: Versions count.
        """
        return self.dbData.get_versions_count(country_code)

    def get_os_count(self, country_code):
        """
        Get the number of distinct operating systems detected in a given country.

        Args:
            country_code (str): The country code to query.

        Returns:
            int: OS count.
        """
        return self.dbData.get_os_count(country_code)

    def get_cpe_count(self, country_code):
        """
        Get the number of distinct CPE (Common Platform Enumeration) entries for a given country.

        Args:
            country_code (str): The country code to query.

        Returns:
            int: CPE count.
        """
        return self.dbData.get_cpe_count(country_code)
