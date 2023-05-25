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
peers="8f3b17746be8f6faba3457c1e039e4a2fe3cb483@65.108.111.32:26656,84323d88e00d3cc9ca0c29211305e4fa5d09372f@148.251.137.220:26656,06887c80bf8150af6331a993411a701d6c76c769@194.195.118.177:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,6f8eddb672e93eb3362a7cb1c843a4e26af71ebc@149.202.72.186:26629,06805bbbb45dbbcdadb963fda7f5b3733f331ebe@185.119.118.109:3000,c565abfb2686a51764dca1bacb5280098dda06a5@65.21.236.33:26656,7798342ae6f07e5c2e09bce8bab69e4485cacf64@5.9.72.212:3000,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:26986"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
