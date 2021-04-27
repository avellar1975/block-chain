from blockchain import Blockchain

if __name__ == '__main__':
    blockchain = Blockchain()
    blockchain.add_new_block('$3.7\t De: Satochi\t -> Maria')
    blockchain.add_new_block('$4.5\t De: Joao\t -> Maria')
    blockchain.add_new_block('$2.6\t De: Joao\t -> Luiz')


    indice = 1

    for hash in blockchain.get_all():
        print('\n--------------------------------------------')
        print(f'#{indice} {hash}')
        indice += 1
