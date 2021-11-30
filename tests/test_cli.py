
#$ pgbackup postgres://bob@example.com5432/db_one --driver s3 backups
import pytest
from pgbackup import cli

url = "postgres://bob@example.com5432/db_one"


def test_parser_wihtout_driver():
    """
    Without a specified driver the parser will exiti
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([url])


def test_parser_with_driver():
    """
    The parser wo; exit if it recieves a driver without a destination
    """

    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])


def test_parser_with_driver_and_destination():
    """
    The parser will not exit if it recieves a driver and destination
    """

    parser = cli.create_parser()
    parser.parse_args([url, "--driver", "local", "/some/path"])

    assert arg.url == url
    assert args.driver == "local"
    assert args.destination == "/some/path"

