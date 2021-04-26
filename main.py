from blockchain import Blockchain


if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.add_new_block('$10.2 -> Zero -> João')
    blockchain.add_new_block('$4.5 -> João -> Maria')
    blockchain.add_new_block('$2.5 -> João -> Luiz')

    for hash in blockchain.get_all():
        print(hash)
