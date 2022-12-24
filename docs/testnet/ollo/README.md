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

**live-peers** (24)
```
peers="7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,861d8791ee3912589a825278b28170f8c523dab0@45.147.199.129:26656,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,d6c305ccde3e850ac34228e41952508e48bfa86c@65.21.62.84:26656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,90c1f1775c36690b04bccc08ef942add99826358@38.242.212.52:32656,c0b03cf21640b12d78f6b4b50d7505d05d37f055@95.217.230.54:26656,45c6c9060c390a068cf1d6c1d9999af196b961ef@65.21.78.153:30656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,84d57c8b3b4c07acc97e922cd17b8fc6dfa79a3b@142.132.152.46:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,b1fe199b7ac2a7714c5d21524bb87810a2be94fb@135.181.178.53:32656,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,98ea25336f87ebca4180c974e8b26aec55611ecb@173.212.226.128:32656,ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
