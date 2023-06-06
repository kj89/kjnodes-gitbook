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
peers="42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,4d659b7b244a68913bfbdc6c9e7aa1a64391238e@74.118.139.59:26656,f95d9634ad68b8f0ac80ce308adb71d8c119ada5@141.98.219.104:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
