from argparse import Action, ArgumentParser

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser()
    parser.add_argument("url", help="URL of the PostgreSQL database to backup")
    parser.add_argument("--driver",
        help="how & where to store the backup",
        nargs=2,
        action=DriverAction,
        required=True)
    return parser
