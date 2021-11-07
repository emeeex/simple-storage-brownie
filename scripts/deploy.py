from brownie import (
    accounts, 
    config, 
    SimpleStorage,
    network
    )

# import os

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_keys"])

def deploy_simple_storage():
    # deployer_account = accounts[0]
    # deployer_account =accounts.load('deployer_address')
    # deployer_account = accounts.add(os.getenv("RINKEBY_PRIVATE_KEY"))
    # deployer_account = accounts.add(config["wallets"]["from_keys"])
    deployer_account=get_account()
    simple_storage = SimpleStorage.deploy({"from": deployer_account})
    stored_value = simple_storage.retrieve()
    stored_value = simple_storage.retrieve()
    print("Before update", stored_value)
    transaction = simple_storage.store(15, {"from": deployer_account})
    print("After update", simple_storage.retrieve())
    # print("----updated code---------")
    # print(deployer_account)
    # print(simple_storage)
    # print("----updated code---------")

    # print(deployer_account)


def main():
    deploy_simple_storage()


# if __name__ == '__main__':
#      deploy_simple_storage()
