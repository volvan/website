from include.logic.LogicWrapper import LogicWrapper
from include.models.lineGraphModel import LineGraphModel
from include.models.blockModel import BlockModel
from include.models.multiBlockModel import MultiBlockModel
import random
from dotenv import load_dotenv
from flask import Flask, render_template

# Load environment variables from .env file
load_dotenv()

# Import logic and models

# Initialize Flask app and logic interface
app = Flask(__name__)
logicWrapper = LogicWrapper()


def populate_label(labels):
    """
    Populate a list with fixed date strings (used for testing or display labels).

    Args:
        labels (list): List to populate with date strings.
    """
    labels.insert(0, "17-04-2025")
    labels.insert(0, "18-04-2025")
    labels.insert(0, "19-04-2025")
    labels.insert(0, "20-04-2025")
    labels.insert(0, "21-04-2025")
    labels.insert(0, "22-04-2025")
    labels.insert(0, "23-04-2025")
    labels.insert(0, "24-04-2025")
    labels.append("29-04-2025")
    labels.append("30-04-2025")
    labels.append("01-05-2025")
    labels.append("02-05-2025")
    labels.append("03-05-2025")


def populate_values(values):
    """
    Populate a list with random integers between 0 and 25 for testing/demo data.

    Args:
        values (list): List to populate with random integer values.
    """
    values.insert(0, random.randint(0, 25))
    values.insert(0, random.randint(0, 25))
    values.insert(0, random.randint(0, 25))
    values.insert(0, random.randint(0, 25))
    values.insert(0, random.randint(0, 25))
    values.insert(0, random.randint(0, 25))
    values.insert(0, random.randint(0, 25))
    values.insert(0, random.randint(0, 25))

    values.append(random.randint(0, 25))
    values.append(random.randint(0, 25))
    values.append(random.randint(0, 25))
    values.append(random.randint(0, 25))
    values.append(random.randint(0, 25))
    values.append(random.randint(0, 25))
    values.append(random.randint(0, 25))
    values.append(random.randint(0, 25))


@app.route('/', defaults={'country_code': "IS"})
@app.route("/<string:country_code>")
def landing_page(country_code):
    """
    Landing page route that renders stats and graphs for a given country code.

    Args:
        country_code (str): ISO country code (e.g., "IS" for Iceland).

    Returns:
        Response: Rendered HTML page or error page depending on data availability.
    """
    valid_code = logicWrapper.dbLogic.verify_country_code(country_code)

    if valid_code is False:
        return render_template('404.html'), 404
    if valid_code is None:
        return render_template('not_found.html')

    # A list of BlockModel objects representing simple data blocks on the landing page
    simple_block_models = []
    # A list of MultiBlockModel objects representing multi data blocks on the landing page
    multi_block_models = []
    # A list of LineGraphModel objects representing data for Line Graphs on the landing page
    line_graph_models = []

    # Simple Block Cell: Total IPs Scanned
    scanned_ips_title = "Total IPs Scanned"
    scanned_ips_value = logicWrapper.get_ips_count(country_code)
    # if scanned_ips_value is None: return render_template('not_found.html')

    simple_block_models.append(BlockModel(scanned_ips_title, scanned_ips_value))

    # Simple Block Cell: Total Active IPs
    active_ips_title = "Total Active IPs"
    active_ips_value = logicWrapper.get_total_alive_hosts(country_code)
    # if active_ips_value is None: return render_template('not_found.html')

    simple_block_models.append(BlockModel(active_ips_title, active_ips_value))

    # Simple Block Cell: Total Ports Scanned
    ports_scanned_title = "Ports Scanned"
    ports_scanned_value = logicWrapper.get_port_amount(country_code)
    # if ports_scanned_value is None: return render_template('not_found.html')

    simple_block_models.append(BlockModel(ports_scanned_title, ports_scanned_value))

    # Simple Block Cell: Total Active Ports
    open_ports_title = "Total Open Ports"
    open_ports_value = logicWrapper.get_total_open_ports(country_code)
    # if open_ports_value is None: return render_template('not_found.html')

    simple_block_models.append(BlockModel(open_ports_title, open_ports_value))

    # Line Graph: Total Open Ports
    graph_open_ports_canvas_id = "line-graph_total-open-ports"
    graph_open_ports_title = "Total Open Ports"
    graph_open_ports_dates, graph_open_ports_plots = logicWrapper.get_total_open_ports_plot(country_code)
    # if graph_open_ports_dates is None: return render_template('not_found.html')
    # if graph_open_ports_plots is None: return render_template('not_found.html')

    line_graph_models.append(
        LineGraphModel(
            graph_open_ports_canvas_id,
            graph_open_ports_title,
            graph_open_ports_dates,
            graph_open_ports_plots
        )
    )

    # Multi-Block Cell: Total Unique Ports Open
    unique_ports_title = "Ports Identified"
    unique_ports_content = logicWrapper.get_unique_open_ports(country_code)
    multi_block_models.append(MultiBlockModel(unique_ports_title, unique_ports_content))

    # Multi-Block Cell: Get Services Count
    services_title = "Services Identified"
    services_content = logicWrapper.get_services_count(country_code)
    multi_block_models.append(MultiBlockModel(services_title, services_content))

    # Multi-Block Cell: Get Versions Count
    versions_title = "Versions Identified"
    versions_content = logicWrapper.get_versions_count(country_code)
    multi_block_models.append(MultiBlockModel(versions_title, versions_content))

    # Multi-Block Cell: Get Services Count
    services_title = "OS Identified"
    services_content = logicWrapper.get_os_count(country_code)
    multi_block_models.append(MultiBlockModel(services_title, services_content))

    # Multi-Block Cell: Get Products Count
    products_title = "Products Identified"
    products_content = logicWrapper.get_products_count(country_code)

    multi_block_models.append(MultiBlockModel(products_title, products_content))

    # Multi-Block Cell: Get Versions Count
    versions_title = "CPE Identified"
    versions_content = logicWrapper.get_cpe_count(country_code)
    multi_block_models.append(MultiBlockModel(versions_title, versions_content))

    return render_template('landing.html',
                           simple_cells=simple_block_models,
                           multi_cells=multi_block_models,
                           line_graphs=line_graph_models
                           )


@app.route("/chart")
def chart_test():
    """
    Test route to output chart data to console. Assumes `get_alive_hosts()` returns (labels, values).

    Returns:
        None
    """
    data = logicWrapper.get_alive_hosts()
    labels = data[0]
    values = data[1]

    print("labels:")
    print(labels)
    print("\nvalues:")
    print(values)

    labels.insert(0, "24-04-2025")
    values.insert(0, 0)

    labels.append("26-04-2025")
    values.append(0)
    labels.append("27-04-2025")
    values.append(0)
    labels.append("28-04-2025")
    values.append(0)


@app.route("/not")
def not_found():
    """
    Render the 'not found' template for undefined or unhandled logic failures.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('not_found.html')


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom handler for 404 errors. Renders a custom 404 page.

    Args:
        e (Exception): The error/exception raised.

    Returns:
        tuple: Rendered HTML and 404 status code.
    """
    return render_template('404.html'), 404
