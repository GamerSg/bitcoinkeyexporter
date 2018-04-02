from bitcoin.core import COIN
import bitcoin.rpc
bitcoin.SelectParams("mainnet")

proxy = bitcoin.rpc.Proxy()
with open("priv.txt")  as f:
    lines = f.readlines()

i = 1
for line in lines:
    addr = line.strip()
    #print (addr)
    print (i)
    print(proxy.call("importprivkey", addr,  "ImportWrongWalletAddr" + str(i),  False))
