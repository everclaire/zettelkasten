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
    parser.add_argument('--client_port', type=int, default=2181, help='Zookeeper client port')

    ## Four letter word subparser
    subparsers = parser.add_subparsers(help='Subcommands for Zookeeper or Kafka')

    cmd_parser = subparsers.add_parser('cmd', help='Zookeeper 4lw commands')
    cmd_parser.set_defaults(which='cmd')
    cmd_parser.add_argument('--leader', action='store_true', help='Determine the leader of the Zookeeper cluster')
    cmd_parser.add_argument('--cluster', action='store_true', help='Get Zookeeper cluster topology')
    
    ## Kafka commands subparser
    kafka_parser = subparsers.add_parser('kafka', help='Kafka cluster commands')
    kafka_parser.set_defaults(which='kafka')
    kafka_parser.add_argument('--brokers', action='store_true', help='Get Kafka a list of Kafka brokers')

    return parser.parse_args()