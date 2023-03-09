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
peers="e634fbf8800f76cb911d03e665f2e573188147c0@154.53.32.30:26657,05beef8bd94ad31ce038f13d67db3a3c36539ac5@62.141.44.89:39656,aedf05252d5fac762d5732ab1bc8728a3337b81d@185.197.195.13:26656,b64a4369b555c14a8e05782f25841f54f634b724@101.35.224.91:26657,959a635aaea40cfc4ee75b01506d7816b3bb992e@66.94.104.84:26656,5a68b64792268713ea7c14d77da3ecd9f4eb43c0@212.90.120.247:26656,b402b5605e266dc7844fd20223082d798fee5dec@34.172.227.227:26656,e4ca253a75aa2651d0c0696639b6ce12f4a7244c@195.201.241.25:39656,6fefa7ece2ff81d1c228c31eda72692d9299d8bc@38.242.248.145:26656,4003c942d2fd79c1ef289673a01561681a49ec03@194.163.153.41:26656,b6db16ab4d2dfd61d0be94df4738ce5f1913de11@212.41.9.98:26656,c24993901b157f9515f162569a9eee65b9776674@155.133.22.19:36656,bf10da2792c9439edbfccce2cf0852e692039112@185.215.180.237:26656,6133b6a48cae4480b4c29c0bcc8e9ae501865943@141.164.63.169:26656,0811f875c3b9587d7a5614007c4d151018d3c956@62.171.187.193:26656,1750291aa1de3b04f07161ad4c0f2a47e7879d63@65.21.63.46:26656,dbfe627f6010f1167eb971ebe9bcd82dea9cf6d3@144.91.116.98:26656,4591a6d3bb34030aa3b7be72691e36eb72cd6eff@128.199.47.116:26656,f55ce3e7e95379654cc43f7d840d88f41eaaccec@118.69.175.70:26656,7cd09b8cfa8730a7ffc6b5796b51b346c10e1a4f@194.163.164.150:26656,55dfbbffebc40b147b2b765fc65a65711dafcbcd@31.220.78.145:39656,a5091d1afa277bab864a495d43226ee44f85604e@212.23.222.91:39656,64d2ea39df1cf635fccb17311c245b9fdc56194a@91.107.195.121:26656,ffec1bf617c0856ae62bb4fbf61f6199be965d0c@5.75.229.132:26656,e36ab19d3c46707e9dfec70be31023aed589c06c@161.97.142.54:26656,d2088d72ed310ca8e18a9ffcade2760dbee8423b@38.242.218.161:26656,cdc4fa8458e3225cc61b45ae6708cc5ccc0f2d18@38.242.153.228:26656,9e007b67fcd43335ef2f12759c4652ef25cfa511@178.128.211.233:26656,b410bd21ca4f2201804adf982c1624f910914da2@38.242.208.225:26656,97e7bdc9e3b377330b342e53005bb1756a9656b3@65.108.14.10:26656,594ac939aa2e63be343f2dfb28529640bdb5254d@124.221.84.227:26657,96349c8b30d41264bab5dabbed98b265925333a5@207.180.194.191:26656,ed83ea3ba7f5f5826963867afe2db3ca34b08fd0@124.221.83.125:26657,25d7a6c32516f18e3f45b0379460d8ed4e396b43@164.92.84.68:26656,db100df6875e24dd214d5b57181a14fc0db13dc0@194.163.171.26:26656,82d8f0d473863b8f104623539b0c4b65a997318a@146.190.226.211:26656,46b2205032ff6f15ce8cdca7d225aca3d84db47d@45.85.146.7:39656,9024178fb93ce4062eea8f368285d721a2dd1a9b@45.61.161.15:26656,e2324b10eb138c241b9a966b1e81659bfa6b68a3@138.201.251.62:26656,591b00c0bfdda9f94e40128869041d1da9ee1639@149.102.152.77:26656,4eb0cc5fa9727b3c1803536e9fe48b045cb9923e@194.60.201.124:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
