# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" alt=""><figcaption></figcaption></figure>

Stargaze is a Cosmos zone (layer 1 proof-of-stake blockchain).  It is the base layer node software for the Stargaze NFT Marketplace.

**Chain ID**: stargaze-1 | **Latest Version Tag**: v9.0.0 | **Wasm**: ON

[Website](https://www.stargaze.zone) | [Discord](https://discord.gg/stargaze) | [Twitter](https://twitter.com/stargazezone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/stargaze](https://explorer.kjnodes.com/stargaze)

## Public endpoints

* api: [https://stargaze.api.kjnodes.com](https://stargaze.api.kjnodes.com)
* rpc: [https://stargaze.rpc.kjnodes.com](https://stargaze.rpc.kjnodes.com)
* grpc: stargaze.grpc.kjnodes.com:15890

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stargaze.rpc.kjnodes.com:15856
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stargaze.rpc.kjnodes.com:15859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stargaze/addrbook.json > $HOME/.starsd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="fc668bbf7e34d6926308487348b2655159198f1d@135.181.128.114:13756,0edce41e754e9bb9a228d4d2b0878713f6bd6de9@65.108.99.169:26656,6f8eddb672e93eb3362a7cb1c843a4e26af71ebc@149.202.72.186:26629,f7ca23e1dd99af4ebff6601a2010f77eecdde83d@5.180.210.150:26656,6e5e6a674f41f7b1e6515ba735fbb836c0d89849@66.172.36.140:52656,b1ddf96ff6db5cfe77fa9c88dc2925f4525d0a02@141.94.141.144:56656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,15bf6fc85e4e37b2c96e35c7b76816670ad63c18@65.108.75.107:8656,4da84cfcc0fcc8e144f9fdb4af4b175d8c6864a0@142.93.214.125:26656,5fb6adba37bfa000cf911124c4feb934a1f7ac88@65.108.237.88:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
