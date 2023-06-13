# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:12990

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:12956
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:12959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,830acc854d8936c4f147e7e6e6254feae395da66@142.132.199.236:28656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.71:26656,e39039de5575f01b4ec5267452626e40ac822f19@65.108.101.44:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
