from huffman import HuffmanCoding
import sys

path = "sample.bin"

h = HuffmanCoding(path)

#it's taking path as an input path
decom_path = h.decompress(path)
print("Decompressed file path: " + decom_path)

