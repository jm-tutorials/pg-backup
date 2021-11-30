
#$ pgbackup postgres://bob@example.com5432/db_one --driver s3 backups
import pytest

from pgbackup import cli

url = "postgres://bob@example.com5432/db_one"

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_wihtout_driver(parser):
    """
    Without a specified driver the parser will exiti
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])


def test_parser_with_driver(parser):
    """
    The parser will exit if it receives a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])


def test_parser_wihtout_driverst_partner_with_unkown_driver(parser):
    """
    The parser will exit if the driver name is unknownn
    """ 
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "azure", "destination"])


def test_parser_with_known_drivers(parser):
    """
    The Parser will not exit if the driver name is known
    """
    for driver in ["local","s3"]:
        assert parser.parse_args([url, '--driver', driver, 'destination'])


def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it recieves a driver and destination
    """
    args = parser.parse_args([url, "--driver", "local", "/some/path"])

    assert args.url == url
    assert args.driver == "local"
    assert args.destination == "/some/path"

