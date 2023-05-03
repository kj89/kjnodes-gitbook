# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (21)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,0cc5236b8a37e89af65c8504982ae0eb5b01e004@178.20.47.61:26656,fee8c13c90bc44816ad3b6dbca1d1044008b1b87@65.21.106.157:26656,6903fcc270cb5189033124fece49ce4bb4745ba0@38.242.245.13:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,bb7c79e9d370dc8ff87c2810f9196aaaa8d9f8ae@65.108.68.119:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,aaff99ce425ac9d062d1bca6f75987656e137307@138.201.34.19:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,b02f28e0675743b077186b363386f10845c9e122@194.233.74.249:26656,86a9ef837a37446469fc424b66e8fbf10d6619aa@84.46.255.162:26656,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,0945129df734538663010c1349f1b4f29da48687@89.117.48.176:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
