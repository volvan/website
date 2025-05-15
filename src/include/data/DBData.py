import os
import psycopg2


class DBData:
    """Handles database interactions for querying scanning summary data."""

    def __init__(self):
        """Initialize configuration values."""
        self.max_multi_cell_values = 5

    def get_db_connection(self):
        """
        Establish a connection to the PostgreSQL database using environment credentials.

        Returns:
            connection (psycopg2.connection): DB connection object or None on failure.
        """
        try:
            return psycopg2.connect(
                host='130.208.246.143',
                database='scandb',
                user=os.environ['DB_USERNAME'],
                password=os.environ['DB_PASSWORD'],
                connect_timeout=5
            )
        except psycopg2.OperationalError as e:
            print(f"[DB ERROR] could not connect to database: {e}")
            return None

    def __send_graph_query(self, query):
        """
        Execute a query that returns date and count pairs for graph plotting.

        Args:
            query (str): SQL query string.

        Returns:
            tuple: (labels: list[str], values: list[int]) or None on failure.
        """
        conn = self.get_db_connection()
        if conn is None:
            return None

        try:
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
        except Exception as e:
            print(f"[DB ERROR] query failed: {e}")
            return None
        finally:
            conn.close()

        labels = []
        values = []
        for dt, count in rows:
            labels.append(dt.strftime("%d-%m-%Y"))
            values.append(count)

        return labels, values

    def __send_simple_query(self, query):
        """
        Execute a query and return all fetched rows.

        Args:
            query (str): SQL query string.

        Returns:
            list[tuple]: Query results or None on failure.
        """
        conn = self.get_db_connection()
        if conn is None:
            return None

        try:
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            return rows
        except Exception as e:
            print(f"[DB ERROR] query failed: {e}")
            return None
        finally:
            conn.close()

    def get_country_codes(self):
        """
        Get a list of unique country codes from the summary table.

        Returns:
            list[str]: List of country codes or None on failure.
        """
        query = """
            SELECT DISTINCT country FROM summary
        """
        raw_results = self.__send_simple_query(query)
        if raw_results is None:
            return None

        return [country[0] for country in raw_results]

    def get_ips_count(self, country_code):
        """
        Get the total number of scanned IPs for a given country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None: IP count or -1 on failure.
        """
        query = f"""
            SELECT total_ips_scanned
            FROM summary
            WHERE country = '{country_code}';
        """
        try:
            return self.__send_simple_query(query)[0][0]
        except Exception:
            return -1

    def get_total_alive_hosts(self, country_code):
        """
        Get the number of alive hosts for a country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None: Host count or -1 on failure.
        """
        query = f"""
            SELECT total_ips_active
            FROM summary
            WHERE country = '{country_code}';
        """
        try:
            return self.__send_simple_query(query)[0][0]
        except Exception:
            return -1

    def get_total_open_ports(self, country_code):
        """
        Get the total number of open ports for a country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None: Port count or -1 on failure.
        """
        query = f"""
            SELECT total_ports_open
            FROM summary
            WHERE country = '{country_code}';
        """
        try:
            return self.__send_simple_query(query)[0][0]
        except Exception:
            return -1

    def get_port_amount(self, country_code):
        """
        Get the number of distinct ports scanned in a country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None: Port count or -1 on failure.
        """
        query = f"""
            SELECT total_ports_scanned
            FROM summary
            WHERE country = '{country_code}';
        """
        try:
            return self.__send_simple_query(query)[0][0]
        except Exception:
            return -1

    def get_total_open_ports_plot(self, country_code):
        """
        Get time series data of open ports for plotting.

        Args:
            country_code (str): Country code.

        Returns:
            tuple: (labels: list[str], values: list[int]) or None on failure.
        """
        query = f"""
            SELECT done_date, open_ports
            FROM (
                SELECT
                    id,
                    port_scan_done_ts::date AS done_date,
                    total_ports_open AS open_ports
                FROM summary
                WHERE
                    total_ports_open IS NOT NULL AND
                    port_scan_done_ts IS NOT NULL AND
                    country = '{country_code}'
                ORDER BY port_scan_done_ts DESC
                LIMIT 10
            ) AS last_two
            ORDER BY done_date ASC;
        """
        return self.__send_graph_query(query)

    def get_unique_open_ports(self, country_code):
        """
        Get the count of unique open ports for a country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None: Port count or -1 on failure.
        """
        query = f"""
            SELECT open_ports_count
            FROM summary
            WHERE country = '{country_code}';
        """
        try:
            return self.__send_simple_query(query)[0][0]
        except Exception:
            return -1

    def get_products_count(self, country_code):
        """
        Get the number of identified products in a country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None: Product count or -1 on failure.
        """
        query = f"""
            SELECT products_count
            FROM summary
            WHERE country = '{country_code}';
        """
        try:
            return self.__send_simple_query(query)[0][0]
        except Exception:
            return -1

    def get_services_count(self, country_code):
        """
        Get the number of identified services in a country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None: Service count or -1 on failure.
        """
        query = f"""
            SELECT services_count
            FROM summary
            WHERE country = '{country_code}';
        """
        try:
            return self.__send_simple_query(query)[0][0]
        except Exception:
            return -1

    def get_versions_count(self, country_code):
        """
        Get the number of software versions found in a country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None: Version count or -1 on failure.
        """
        query = f"""
            SELECT versions_count
            FROM summary
            WHERE country = '{country_code}';
        """
        try:
            return self.__send_simple_query(query)[0][0]
        except Exception:
            return -1

    def get_os_count(self, country_code):
        """
        Get the number of detected operating systems in a country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None: OS count or -1 on failure.
        """
        query = f"""
            SELECT os_count
            FROM summary
            WHERE country = '{country_code}';
        """
        try:
            return self.__send_simple_query(query)[0][0]
        except Exception:
            return -1

    def get_cpe_count(self, country_code):
        """
        Get the number of CPE entries in a country.

        Args:
            country_code (str): Country code.

        Returns:
            int or None: CPE count or -1 on failure.
        """
        query = f"""
            SELECT cpe_count
            FROM summary
            WHERE country = '{country_code}';
        """
        try:
            return self.__send_simple_query(query)[0][0]
        except Exception:
            return -1
