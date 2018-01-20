import hashlib as hasher

class Block:
    """
        生成块结构，但是现在创建的是区块链，所以需要向实际的链中添加块，每个块都
        需要上一个块的信息，因此区块链的第一个区块，起源块，是个特殊的块要手动添加
        ，或特殊的逻辑允许添加。
    """
    def __init__(self, index, timestamp, data, previous_hash):
         self.index = index
         self.timestamp = timestamp
         self.data = data
         self.previous_hash = previous_hash
         self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
        return sha.hexdigest()



"""
以下创建函数简单的返回一个区块以便产生第一个区块，这个块的索引为0 ，它具有任意
的数据值和‘前一个哈希’参数的任意值
"""
import datetime as date


def create_genesis_block():
    return Block(0, date.datetime.now(), 'Genesis Block', '0')


"""
创建函数，以便在区块链中生成后续的块，这个函数把链中的前一个块作为参数，创建生成
的块的数据，并使用适当的数据返回新块，当新的块哈希信息来自前面的块时，区块链的完整
性会随着每个新块而增加，如果不这样做，外部组织就更容易“改变过去”，用全新的方式
取代过去已有的链条，这一系列的散列可以作为加密的证据，有助于确保一旦将块添加到区块链
，它就不能被替换或删除
"""
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


"""
创建区块链，本次实列中，区块链本身是一个简单的Python列表，列表的第一个元素是起源块
当然还要添加后续的块，因为SnakeCoin是最小的区块链，这里添加20个
"""

blockchain = [create_genesis_block()]
previous_block = blockchain[0]
numm_of_blocks_add = 20

for i in range(0, numm_of_blocks_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} has been added to blockchain!".format(block_to_add.index))
    print("Hash:{}".format(block_to_add.hash))