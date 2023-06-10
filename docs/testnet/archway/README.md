# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

Archway is an incentivized smart contract chain for Cosmos  ecosystem which gives developers a simple way to build  scalable cross-chain dapps. The developers automatically  receive rewards for their contributions to the network.

**Chain ID**: constantine-3 | **Latest Version Tag**: v0.6.0 | **Wasm**: ON

[Website](https://archway.io) | [Discord](https://discord.gg/archwayhq) | [Twitter](https://twitter.com/archwayhq)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/archway-testnet](https://explorer.kjnodes.com/archway-testnet)

## Public endpoints

* api: [https://archway-testnet.api.kjnodes.com](https://archway-testnet.api.kjnodes.com)
* rpc: [https://archway-testnet.rpc.kjnodes.com](https://archway-testnet.rpc.kjnodes.com)
* grpc: archway-testnet.grpc.kjnodes.com:15690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@archway-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@archway-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/archway-testnet/addrbook.json > $HOME/.archway/config/addrbook.json
```

**live-peers** (22)
```bash
peers="1171accc7427f2ffb76fcaa5acdef518ff42c382@178.63.104.200:45656,6d4f2faa284b9c9625e781309b637e92627b6afd@188.40.59.225:45656,8b96338b18c1e4a76a119fe0812c131a4e2cc96a@65.109.70.45:20656,272009296f322b24c1e6b120feaa716edbbbe125@65.109.158.20:26676,8df8a64ecf0aaba1e1faee06d005aa912d578549@65.109.89.5:41656,2e4aa44eabb996442fa865ab04cbdcc46fffaf0b@65.109.155.238:27656,5069525117c370eedfca4dbdf79a2d092c3b9687@173.249.49.123:24656,261acb73f483d1cace653cb54f7b8815f63b7e56@54.36.227.1:26656,f0993a9eef446cbfed4ed78bcb4179143079a5f3@51.161.84.41:26356,e8d60ff778f3c27f54382ff22c7ac071f2a81027@35.223.36.227:26656,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,4928b2aa3a2c89d2700d3ca1192455aefde74c3c@142.132.202.87:26656,280fe9d15d5399bdd549487246dac82bab0a3fe8@220.85.113.33:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,5e0d6bfea56f7da5a1bdf9e4d1ee95c672a9d957@185.144.99.13:26656,eb70e2aaacbff6a3db3c63c9ff055d63df14c70b@47.90.189.130:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,e50d7fa6a50ac792e5df61ff621d9621e9fcc8aa@34.133.135.231:26656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
