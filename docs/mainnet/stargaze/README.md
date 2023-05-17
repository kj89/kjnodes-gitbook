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
peers="fc668bbf7e34d6926308487348b2655159198f1d@135.181.128.114:13756,673ad0cb62287afcdbe5e5c88b91e39ee1bd394a@65.21.181.67:26656,7798342ae6f07e5c2e09bce8bab69e4485cacf64@5.9.72.212:3000,d9307d7d7e219461ab9c333104780181b6933e74@89.58.50.116:26656,4da84cfcc0fcc8e144f9fdb4af4b175d8c6864a0@142.93.214.125:26656,82d89abe4024c54b68b8d07887cbb7f3d0710f71@130.61.146.203:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.45.253:26656,d3393f1ddc2b2f1ad4e91d86b429576ab1ed241f@195.154.99.18:28454,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,0edce41e754e9bb9a228d4d2b0878713f6bd6de9@65.108.99.169:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
