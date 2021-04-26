"""Entendendo como funciona o Blockchain."""
import hashlib


class EvandroCoinBlock:
    """Exemplo.

    >>> evandro = EvandroCoinBlock('str inicial', ['trans_01', 'trans_02'])
    >>> evandro.block_dados
    'trans_01-trans_02-str inicial'
    >>> evandro.block_hash
    'bdc134fa28bec09d1ec1595342f233a9ecce4f99c37f576a9300a567116917c3'
    """

    def __init__(self, hash_bloco_anterior, transacoes):
        self.hash_bloco_anterior = hash_bloco_anterior
        self.transacoes = transacoes

        self.block_dados = "-".join(transacoes) + "-" + hash_bloco_anterior
        self.block_hash = hashlib.sha256(self.block_dados.encode()).hexdigest()


t1 = "Ana envia 2.1 ECB para Joao"
t2 = "Bob envia 4.1 ECB para Ana"
t3 = "Joao envia 3.2 ECB para Luiz"
t4 = "Luiz envia 0.3 ECB para Bob"
t5 = "Bob envia 1 ECB para Joao"
t6 = "Luiz envia 2 ECB para Ana"


bloco_inicial = EvandroCoinBlock("Hash Inicial", [t1, t2])

print(bloco_inicial.block_dados)
print(bloco_inicial.block_hash)

segundo_bloco = EvandroCoinBlock(bloco_inicial.block_hash, [t3, t4])

print(segundo_bloco.block_dados)
print(segundo_bloco.block_hash)

terceiro_bloco = EvandroCoinBlock(segundo_bloco.block_hash, [t5, t6])

print(terceiro_bloco.block_dados)
print(terceiro_bloco.block_hash)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
