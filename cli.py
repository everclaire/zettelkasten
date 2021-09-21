def parser():
    try:
        import argparse
    except ModuleNotFoundError:
        print('Error: zetl requires argparse')
        sys.exit(1)
    # Start the argument parser
    parser = argparse.ArgumentParser()
    # Set the cluster endpoint i.e. localhost
    parser.add_argument('--addr', type=str, default='127.0.0.1', help='The address of the Zookeeper host. Defaults to 127.0.0.1. IP address only at this time')
    parser.add_argument('--port', type=int, default=8080, help='Command port for the Zookeeper instance(s)')
    parser.add_argument('--protocol', type=str, default='http', help='Protocol for accessing Zookeeper')

    ## Four letter word subparser
    subparsers = parser.add_subparsers(help='Subcommands for Zookeeper')

    cmd_parser = subparsers.add_parser('cmd', help='Four letter word commands')
    cmd_parser.set_defaults(which='cmd')
    cmd_parser.add_argument("--leader", action="store_true", help="Determine the leader of the Zookeeper cluster")
    cmd_parser.add_argument("--cluster", action="store_true", help="Get cluster topology")
    
    return parser.parse_args()