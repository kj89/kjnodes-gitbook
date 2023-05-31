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
peers="c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,e6b9d01d5adc8ab1106f142b18f5ea5da00ec306@144.76.82.52:26656,4d659b7b244a68913bfbdc6c9e7aa1a64391238e@74.118.139.59:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,9f2df25f380a7e67a92c3dc5e7c33c08555b30dc@5.9.108.19:26656,95dbddda671081fb433871fa612ff5291242d93d@45.67.221.200:26656,2048e1bc1f020fa210fb475e7a0ec0948919609f@185.217.125.64:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
