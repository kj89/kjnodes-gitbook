# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

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

**live-peers** (28)
```bash
peers="70d0a7fc3d57a61c7222b3d9891841aede5f5238@38.242.153.80:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,3bb1549a6b7536e673bb8b9a036485c5ec18ce76@194.34.232.36:39656,daeabf9286ea1331f07f7981c5425aeca5db1f5b@95.217.5.233:26656,3a5d2bd306d6a0b842e5b14dfd1fc5a1069b55d1@14.162.213.215:20156,6b9c70de7d5f44fe07198bdf950b6ef2ba0df244@75.119.132.184:26656,96f253c371a7f7f854faf7ffc5e0ee9fc4f8dd7f@165.227.32.93:26656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,4dbcf74d1c5760c2ef6037219c1c9b2e7a4cea63@194.163.137.48:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,4f61728aee644debb934f1afdc52e958dc3f4485@81.0.218.67:26656,42c34c76c4c1fa2f32a8c28849cba28549f71a03@109.123.243.27:26656,72d5f1f8ed170601cd297b1af220ead8bcb2537c@31.220.86.33:39656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,799ecf85b985e44ba30f3ff1c9da11fd4064d041@86.48.2.182:26656,31dfb28f50d112bc4090eb98bf0610fbf7a8cbc5@159.69.56.78:11656,ba6a46ae8fe4e1e95c0debfa1d4f3012fa6b33af@66.94.123.46:26656,0e90ac8e15b040c2a158b68f25299fc32a9d5940@89.117.57.25:26656,9920bfdee1f9f61221e0301b1823f050e8fb992f@193.203.203.121:26656,aa4a5e232eac72cceaedd89f036ea458c78f94b9@31.220.84.87:39656,828ecd9793395c8dbe7bab63ef2ca76c7474508d@78.47.148.190:26656,fb0d5b5d4d9d29e13ab0e11f7d58eac68f373554@194.163.153.99:26656,ed635eb28d417674a5f551f088772367622e7c92@138.68.99.211:26656,359ab5a45015c75b0ca847519254cb8d0aa3aa6c@65.108.206.74:26656,00b1c55019204641cada3f3f24d0c191f760745f@194.163.149.195:26656,83be009ed822ad05d877c26bfa457c95551128c0@167.99.249.130:26656,dfdfca675e009578b775d7febace9d15d97c3755@207.180.224.21:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
