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
peers="f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.71:26656,f95d9634ad68b8f0ac80ce308adb71d8c119ada5@141.98.219.104:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
