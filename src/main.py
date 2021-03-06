import sys
from data_types import *
from queue_manager import *


CONFIGS_MWAPI = {
    'DEFAULT': MWAPIConfig(host='localhost', port=50051, max_conns=10)
}

CONFIGS_ETH = {
    'LOCAL': EthConfig(server='http://127.0.0.1', port=8545,
                       contract='0x33c9d18fb98e08fe73262e333bcbf428ebedbeff',
                       abi='../abi'),
    'INFURA': EthConfig(server='https://ropsten.infura.io', port=443,
                        contract='0xE275e9c7ceBF2C093C365439b836adF9A28537E2',
                        abi='../abi/test_contract.json')
}

CONFIGS_IPFS = {
    'LOCAL': IPFSConfig(server='127.0.0.1', port=5001, data_path='/tmp'),
    'INFURA': IPFSConfig(server='https://ipfs.infura.io', port=5001, data_path='/tmp')
}

CONFIGS = {
    'TEST_INFURA': QueueManagerConfig(
        mnapi=None,
        mwapi=CONFIGS_MWAPI['DEFAULT'],
        ipfs=CONFIGS_IPFS['LOCAL'],
        eth=CONFIGS_ETH['LOCAL'],
        version=Version(major=0, minor=1, patch=0, agent='neuromaster')
    )
}


def run(config_name):
    print('Starting masternode with config %s...' % config_name)
    queue_manager = QueueManager(CONFIGS[config_name])
    queue_manager.run()


def main(argv):
    run('TEST_INFURA')

if __name__ == "__main__":
    main(sys.argv)
