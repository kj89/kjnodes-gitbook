# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:29090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:29656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:29659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.10:26656,366c970c48c290810a1c79e65766a4e964ac044c@68.219.212.74:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.169.186:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,b084089897e1ea470750a9ab08c6425bb66fee98@20.241.82.136:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,f860ee99ef34f10155065a97e95da07f712f1d6b@116.202.169.6:26666,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@169.155.168.250:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,8cd04b204cf7bcbbe0f62e818b3d9ab47195aca3@20.39.195.201:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,594321750643b7a70c27dbc9440c41206a8c19d9@195.14.6.2:26656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,294fb7588a6966bb9096a79eed8979fe6f42380e@207.148.88.210:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,2904827f3ffa642bf7122d65cef27e1ab40a7346@35.74.104.174:16656,5ee0a923bdd973f312bc2f5a4a6f25b817e3aba1@40.76.143.93:26656,75bae7b2af60155b6687ca3e5f92010d35cb0c12@54.164.100.216:26656,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,c13125d0a7430de9448c97eea231e7dcab897df5@188.34.191.2:26756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
