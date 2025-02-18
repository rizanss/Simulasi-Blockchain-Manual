import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index  # Nomor blok
        self.previous_hash = previous_hash  # Hash blok sebelumnya
        self.data = data  # Data transaksi
        self.timestamp = timestamp or time.time()  # Waktu pembuatan blok
        self.hash = self.calculate_hash()  # Hash blok saat ini

    def calculate_hash(self):
        """Bikin hash SHA-256 dari isi blok"""
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}".encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Awal blockchain

    def create_genesis_block(self):
        """Bikin blok pertama (Genesis Block)"""
        return Block(0, "0", "Genesis Block")

    def add_block(self, data):
        """Tambah blok baru ke blockchain"""
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Cek apakah blockchain valid"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Cek apakah hash blok masih valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Cek apakah blok terhubung dengan benar
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_chain(self):
        """Tampilkan isi blockchain"""
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Data: {block.data}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Hash: {block.hash}\n")

# Jalankan simulasi
my_blockchain = Blockchain()
my_blockchain.add_block("Transaksi 1: Alice kirim 10 BTC ke Bob")
my_blockchain.add_block("Transaksi 2: Bob kirim 5 BTC ke Charlie"

# Cetak blockchain
my_blockchain.print_chain())

# Cek validitas blockchain
print(f"Blockchain Valid? {my_blockchain.is_chain_valid()}")
