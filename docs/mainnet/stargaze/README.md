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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,6c7a904400f646e43eaf1ea76976de037392efa1@23.88.69.22:26566,85591aa9be728b7f705382794a5c1d73dae8f2ae@141.94.196.138:26656,c2054e53fdb2f5cafb1a2f633de064143c16057c@93.189.30.126:26656,663675af3a1ea846d7824fd6ad087b6b576bbd05@136.243.94.138:36656,7798342ae6f07e5c2e09bce8bab69e4485cacf64@5.9.72.212:3000,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.45.253:26656,b99beb75e753224b2cf6b3dd8db48b47047c56f6@135.181.162.122:26656,84323d88e00d3cc9ca0c29211305e4fa5d09372f@148.251.137.220:26656,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
