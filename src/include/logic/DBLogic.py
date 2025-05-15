# from os import path
# import sys
# current_dir = path.dirname(__file__)
# sys.path.append(current_dir)

from ..data.DataWrapper import DataWrapper


class DBLogic:
    """Logic layer that validates and processes country-specific data from the DataWrapper (which pulls from DBData)."""

    def __init__(self, dataWrapper: DataWrapper):
        """
        Initialize with a DataWrapper instance.

        Args:
            dataWrapper (DataWrapper): Instance used to query the database.
        """
        self.dataWrapper = dataWrapper

    def __sort_highest_first(self, org_dict: dict) -> dict:
        """
        Sort a dictionary by its values in descending order.

        Args:
            org_dict (dict): Dictionary to sort.

        Returns:
            dict: Sorted dictionary.
        """
        if not org_dict:
            return {}
        return dict(sorted(org_dict.items(), key=lambda value: value[1], reverse=True))

    def __shortify(self, long_dict: dict) -> dict:
        """
        Limit dictionary to a maximum of 5 entries.

        Args:
            long_dict (dict): Dictionary to truncate.

        Returns:
            dict: Truncated dictionary.
        """
        if not long_dict:
            return {}
        if len(long_dict) > 5:
            return dict(list(long_dict.items())[:5])
        return long_dict

    def verify_country_code(self, country_code: str) -> bool | None:
        """
        Check if a country code is valid.

        Args:
            country_code (str): Country code to validate.

        Returns:
            bool or None: True if valid, False if not, None if data fetch fails.
        """
        all_country_codes = self.dataWrapper.get_country_codes()
        if all_country_codes is None:
            return None
        return country_code.upper() in all_country_codes

    def get_total_alive_hosts(self, country_code: str):
        """
        Return total alive hosts for the given country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None
        """
        return self.dataWrapper.get_total_alive_hosts(country_code)

    def get_ips_count(self, country_code: str):
        """
        Return IP count for the given country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None
        """
        if self.verify_country_code(country_code) is None:
            return None
        return self.dataWrapper.get_ips_count(country_code)

    def get_total_open_ports(self, country_code: str):
        """
        Return total open ports for the given country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None
        """
        if self.verify_country_code(country_code) is None:
            return None
        return self.dataWrapper.get_total_open_ports(country_code)

    def get_port_amount(self, country_code: str):
        """
        Return the number of scanned ports for the given country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None
        """
        if self.verify_country_code(country_code) is None:
            return None
        return self.dataWrapper.get_port_amount(country_code)

    def get_total_open_ports_plot(self, country_code: str):
        """
        Return plotting data of open ports over time.

        Args:
            country_code (str): Country code.

        Returns:
            tuple: (labels, values) or (None, None) on failure.
        """
        if self.verify_country_code(country_code) is None:
            return None, None
        return self.dataWrapper.get_total_open_ports_plot(country_code)

    def get_unique_open_ports(self, country_code: str):
        """
        Return top 5 unique open ports sorted by frequency.

        Args:
            country_code (str): Country code.

        Returns:
            dict or None
        """
        if self.verify_country_code(country_code) is None:
            return None
        content = self.dataWrapper.get_unique_open_ports(country_code)
        return self.__shortify(self.__sort_highest_first(content))

    def get_products_count(self, country_code: str):
        """
        Return top 5 products by occurrence.

        Args:
            country_code (str): Country code.

        Returns:
            dict or None
        """
        if self.verify_country_code(country_code) is None:
            return None
        content = self.dataWrapper.get_products_count(country_code)
        return self.__shortify(self.__sort_highest_first(content))

    def get_services_count(self, country_code: str):
        """
        Return top 5 services by occurrence.

        Args:
            country_code (str): Country code.

        Returns:
            dict or None
        """
        if self.verify_country_code(country_code) is None:
            return None
        content = self.dataWrapper.get_services_count(country_code)
        return self.__shortify(self.__sort_highest_first(content))

    def get_versions_count(self, country_code: str):
        """
        Return top 5 versions by occurrence.

        Args:
            country_code (str): Country code.

        Returns:
            dict or None
        """
        if self.verify_country_code(country_code) is None:
            return None
        content = self.dataWrapper.get_versions_count(country_code)
        return self.__shortify(self.__sort_highest_first(content))

    def get_os_count(self, country_code: str):
        """
        Return top 5 operating systems by occurrence.

        Args:
            country_code (str): Country code.

        Returns:
            dict or None
        """
        if self.verify_country_code(country_code) is None:
            return None
        content = self.dataWrapper.get_os_count(country_code)
        return self.__shortify(self.__sort_highest_first(content))

    def get_cpe_count(self, country_code: str):
        """
        Return top 5 CPE identifiers by occurrence.

        Args:
            country_code (str): Country code.

        Returns:
            dict or None
        """
        if self.verify_country_code(country_code) is None:
            return None
        content = self.dataWrapper.get_cpe_count(country_code)
        return self.__shortify(self.__sort_highest_first(content))
