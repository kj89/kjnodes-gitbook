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

**live-peers** (20)
```bash
peers="7e9827b5154a4ec4de93e277b19f77a387661664@46.4.213.198:26656,fb0b8dfc6d81be517e8150f532c5d5ef09e5c898@162.62.61.200:26656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,8b96338b18c1e4a76a119fe0812c131a4e2cc96a@65.109.70.45:20656,c0d0c9f1ef645bcf1c214b05581c9d4a4b45e97e@185.230.138.96:26656,e40e240706e5c551de40fefab1ad9fbf4a4bec23@141.94.73.39:42656,7f46c5c86639e04183cea341d62c59213cdc4542@185.230.138.49:26656,346d791f15e87ec54676cde7379704beefadf048@65.108.105.99:31656,5069525117c370eedfca4dbdf79a2d092c3b9687@173.249.49.123:24656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,a14e3d92fbacf59cec76a4f3cfb9c9ff599f892b@210.16.67.34:36656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,e8d60ff778f3c27f54382ff22c7ac071f2a81027@35.223.36.227:26656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,1192b15c204c5ac6d99b4cce775c8447b312f92b@95.217.229.113:26656,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,0cf5d2bcc49c1acddb6b7b2bc547543ec2fbe844@34.239.246.206:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
