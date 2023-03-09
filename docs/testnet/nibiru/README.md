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
peers="42c72d74b6a3a5104f332b94615b9053753d5a47@65.109.132.63:26656,6fefa7ece2ff81d1c228c31eda72692d9299d8bc@38.242.248.145:26656,81e70cd7967803bef67e9d2cd0c569bc406d1968@38.242.241.56:26656,a5091d1afa277bab864a495d43226ee44f85604e@212.23.222.91:39656,cea3f4607fbf298466e65e027d82e04123b92ab5@161.97.143.105:26656,82d8f0d473863b8f104623539b0c4b65a997318a@146.190.226.211:26656,7cd09b8cfa8730a7ffc6b5796b51b346c10e1a4f@194.163.164.150:26656,9fa1b05c446850c9e3d55299f7991b61d47d70f6@1.53.109.68:26656,37e20163b663340f28ef86fe95460a81f6ca6ad6@88.210.12.60:26656,591b00c0bfdda9f94e40128869041d1da9ee1639@149.102.152.77:26656,e634fbf8800f76cb911d03e665f2e573188147c0@154.53.32.30:26657,55dfbbffebc40b147b2b765fc65a65711dafcbcd@31.220.78.145:39656,5b4b12ded2c0db5f29345580b507156ca5399053@31.220.84.69:26656,64d2ea39df1cf635fccb17311c245b9fdc56194a@91.107.195.121:26656,cdc4fa8458e3225cc61b45ae6708cc5ccc0f2d18@38.242.153.228:26656,bf10da2792c9439edbfccce2cf0852e692039112@185.215.180.237:26656,77d89a919f28122c9ceef7be1d0dc761fd35a330@20.199.10.78:26656,0e9c978b9a4e8c8adf2c27edc8a512a522c3da86@185.15.244.148:26656,b64a4369b555c14a8e05782f25841f54f634b724@101.35.224.91:26657,c39d6a8ff27c3854dab8823019465bed49134ccb@144.76.101.121:26656,959a635aaea40cfc4ee75b01506d7816b3bb992e@66.94.104.84:26656,4eb0cc5fa9727b3c1803536e9fe48b045cb9923e@194.60.201.124:26656,dbfe627f6010f1167eb971ebe9bcd82dea9cf6d3@144.91.116.98:26656,aab71f268f0926ea6e2450f9b18dd2a91750b7e0@38.242.141.113:26656,4591a6d3bb34030aa3b7be72691e36eb72cd6eff@128.199.47.116:26656,64cf20514a03108936e27b9382c228d42b4642e1@88.198.14.157:26656,ffec1bf617c0856ae62bb4fbf61f6199be965d0c@5.75.229.132:26656,46b2205032ff6f15ce8cdca7d225aca3d84db47d@45.85.146.7:39656,9ebe58ce146562b2a92f4b7bb04beaa0f40817a1@23.88.36.176:26656,120a6ef9986295439e4a920e2fbe89e4314a9976@149.102.152.81:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,58d3b3307293d3cbe7488d28c8f751ee985f20b8@65.109.61.47:39656,1750291aa1de3b04f07161ad4c0f2a47e7879d63@65.21.63.46:26656,540a366efc3987627306bde0f1acb2354f277789@78.10.207.252:26656,00abaa0b6be5c41bbb6a72315b301091481a8aaa@95.128.140.24:12656,1e360e7ae5de39cddf3aa3fe5b380c89ba50f0ed@149.102.142.180:26656,0811f875c3b9587d7a5614007c4d151018d3c956@62.171.187.193:26656,f5d99801be3160120468babdfe6866b2c7b7ed58@65.109.111.159:26656,9024178fb93ce4062eea8f368285d721a2dd1a9b@45.61.161.15:26656,b402b5605e266dc7844fd20223082d798fee5dec@34.172.227.227:26656,05beef8bd94ad31ce038f13d67db3a3c36539ac5@62.141.44.89:39656,ed83ea3ba7f5f5826963867afe2db3ca34b08fd0@124.221.83.125:26657"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
