# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)


## Public endpoints

* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (23)
```
peers="861d8791ee3912589a825278b28170f8c523dab0@45.147.199.129:26656,1f06a05a88b812f9e8147379a2bb82c8bab37e42@84.46.252.55:26656,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,bc73e1f3bde267171309e723416690c9c7404881@142.132.199.236:27656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,34f4de6082a894a3b6addab6c370e62238d43649@65.109.28.55:28656,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,c2bc7720a610d753b037d89e6c3f58f7c718e24f@116.202.117.229:32656,c0b03cf21640b12d78f6b4b50d7505d05d37f055@95.217.230.54:26656,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,90c1f1775c36690b04bccc08ef942add99826358@38.242.212.52:32656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,98ea25336f87ebca4180c974e8b26aec55611ecb@173.212.226.128:32656,6fb1ca4b01926c43fb28f5eadc4710d0e7df8624@176.126.87.165:26656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
