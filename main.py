from bitcoin.core import COIN
import bitcoin.rpc
bitcoin.SelectParams("mainnet")

proxy = bitcoin.rpc.Proxy()
with open("walletlist.txt")  as f:
    lines = f.readlines()
    
for line in lines:
    tokens = line.split(";")
    addr = tokens[2].replace("\"", "")
    addr = addr.strip()
 #   print (addr)
    print(proxy.dumpprivkey(addr))
