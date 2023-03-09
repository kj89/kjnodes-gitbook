# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)




## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: [https://nibiru-testnet.grpc.kjnodes.com](https://nibiru-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (42)
```bash
peers="37e20163b663340f28ef86fe95460a81f6ca6ad6@88.210.12.60:26656,afc39d2bddb63b49d0c42bb7703011d09ce032b2@84.46.241.94:26656,540a366efc3987627306bde0f1acb2354f277789@78.10.207.252:26656,bf10da2792c9439edbfccce2cf0852e692039112@185.215.180.237:26656,f5d99801be3160120468babdfe6866b2c7b7ed58@65.109.111.159:26656,00abaa0b6be5c41bbb6a72315b301091481a8aaa@95.128.140.24:12656,959a635aaea40cfc4ee75b01506d7816b3bb992e@66.94.104.84:26656,4eb0cc5fa9727b3c1803536e9fe48b045cb9923e@194.60.201.124:26656,91d0512ebcedb3f4ab9f26ae13b67166ce7a7003@46.180.223.102:26656,a4f4265d98011e80100559e5ce16546168fbccc6@161.97.103.11:26656,478b3fbd3152c90662a02e293efdab599fc1799f@43.133.199.91:26657,b6db16ab4d2dfd61d0be94df4738ce5f1913de11@212.41.9.98:26656,e634fbf8800f76cb911d03e665f2e573188147c0@154.53.32.30:26657,82d8f0d473863b8f104623539b0c4b65a997318a@146.190.226.211:26656,591b00c0bfdda9f94e40128869041d1da9ee1639@149.102.152.77:26656,1750291aa1de3b04f07161ad4c0f2a47e7879d63@65.21.63.46:26656,d5f5a397f04c8ca3875fda638395fd57e1dc39c9@84.46.247.146:26656,cea3f4607fbf298466e65e027d82e04123b92ab5@161.97.143.105:26656,4ff077065e3f810685336ed28363e5f82de0a38c@90.188.59.213:26656,11c5066a3f8004e874f1508a7edb807206c531eb@194.163.175.32:26656,a2cb5ae6fa93db8e8d470dd05ec7ca29d40bdbd8@217.79.178.84:39656,55dfbbffebc40b147b2b765fc65a65711dafcbcd@31.220.78.145:39656,81e70cd7967803bef67e9d2cd0c569bc406d1968@38.242.241.56:26656,50167a61281928220a34d521f3666eb32340cfdd@165.232.77.10:26656,9024178fb93ce4062eea8f368285d721a2dd1a9b@45.61.161.15:26656,1e360e7ae5de39cddf3aa3fe5b380c89ba50f0ed@149.102.142.180:26656,4591a6d3bb34030aa3b7be72691e36eb72cd6eff@128.199.47.116:26656,3feddf650d5b3ba64b0461ac7bf3195e8dc0fa39@95.217.182.223:26556,265a7d0a57e8891f06b2c88a1abc14e298192bf2@65.21.189.233:26656,c24993901b157f9515f162569a9eee65b9776674@155.133.22.19:36656,e385e251cd84176dda032ad47fbe93096b7e03c7@84.46.246.136:26656,5b4b12ded2c0db5f29345580b507156ca5399053@31.220.84.69:26656,aedf05252d5fac762d5732ab1bc8728a3337b81d@185.197.195.13:26656,4d1780c1abcd7df29391bed1f5138af88424ce22@185.182.184.194:26656,58c4f92775bc63621513ce145d58f239aec8c510@89.117.49.71:26656,d63f834d73a17b894840cc068b335351c91f3646@138.68.98.218:26656,a5091d1afa277bab864a495d43226ee44f85604e@212.23.222.91:39656,fb26e0b2ea196136f27d5bb2704b46d12f194495@164.92.202.21:26656,7cd09b8cfa8730a7ffc6b5796b51b346c10e1a4f@194.163.164.150:26656,77d89a919f28122c9ceef7be1d0dc761fd35a330@20.199.10.78:26656,64d2ea39df1cf635fccb17311c245b9fdc56194a@91.107.195.121:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
