from src.include.data.DataWrapper import DataWrapper
import sys
from .DBLogic import DBLogic

sys.path.append('../../')


class LogicWrapper:
    """
    A wrapper class that connects web-facing Flask logic to the DBLogic layer.

    It acts as the main access point for route handlers to retrieve processed data.
    """

    def __init__(self):
        """Initialize LogicWrapper with internal DBLogic and DataWrapper instances."""
        self.dataWrapper = DataWrapper()
        self.dbLogic = DBLogic(self.dataWrapper)

    def get_total_alive_hosts(self, country_code):
        """
        Get the number of alive hosts in a given country.

        Args:
            country_code (str): The country code.

        Returns:
            int or None: Total alive hosts.
        """
        return self.dbLogic.get_total_alive_hosts(country_code)

    def get_ips_count(self, country_code):
        """
        Get the number of IPs scanned in a given country.

        Args:
            country_code (str): The country code.

        Returns:
            int or None: IP count.
        """
        return self.dbLogic.get_ips_count(country_code)

    def get_total_open_ports(self, country_code):
        """
        Get the total number of open ports in a given country.

        Args:
            country_code (str): The country code.

        Returns:
            int or None: Total open ports.
        """
        return self.dbLogic.get_total_open_ports(country_code)

    def get_port_amount(self, country_code):
        """
        Get the number of scanned ports in a given country.

        Args:
            country_code (str): The country code.

        Returns:
            int or None: Port count.
        """
        return self.dbLogic.get_port_amount(country_code)

    def get_total_open_ports_plot(self, country_code):
        """
        Get open port counts over time for a given country, for plotting.

        Args:
            country_code (str): The country code.

        Returns:
            tuple: (labels, values) or (None, None) on failure.
        """
        return self.dbLogic.get_total_open_ports_plot(country_code)

    def get_unique_open_ports(self, country_code):
        """
        Get the most common unique open ports for a country.

        Args:
            country_code (str): The country code.

        Returns:
            dict or None: Top unique open ports.
        """
        return self.dbLogic.get_unique_open_ports(country_code)

    def get_products_count(self, country_code):
        """
        Get the most common products found in a country.

        Args:
            country_code (str): The country code.

        Returns:
            dict or None: Top products.
        """
        return self.dbLogic.get_products_count(country_code)

    def get_services_count(self, country_code):
        """
        Get the most common services found in a country.

        Args:
            country_code (str): The country code.

        Returns:
            dict or None: Top services.
        """
        return self.dbLogic.get_services_count(country_code)

    def get_versions_count(self, country_code):
        """
        Get the most common software versions found in a country.

        Args:
            country_code (str): The country code.

        Returns:
            dict or None: Top software versions.
        """
        return self.dbLogic.get_versions_count(country_code)

    def get_os_count(self, country_code):
        """
        Get the most common operating systems found in a country.

        Args:
            country_code (str): The country code.

        Returns:
            dict or None: Top OS types.
        """
        return self.dbLogic.get_os_count(country_code)

    def get_cpe_count(self, country_code):
        """
        Get the most common CPEs found in a country.

        Args:
            country_code (str): The country code.

        Returns:
            dict or None: Top CPEs.
        """
        return self.dbLogic.get_cpe_count(country_code)
