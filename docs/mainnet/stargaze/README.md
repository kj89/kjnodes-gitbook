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
* grpc: stargaze.grpc.kjnodes.com:58090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stargaze.rpc.kjnodes.com:58656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stargaze.rpc.kjnodes.com:58659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stargaze/addrbook.json > $HOME/.starsd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="0edce41e754e9bb9a228d4d2b0878713f6bd6de9@65.108.99.169:26656,0d9c5b7b4361cacb7ec5b08b818358f9cf23034b@65.108.66.92:26656,d607a30dcc5f90c6142f5c1969fed692157b5493@138.201.30.152:26656,7798342ae6f07e5c2e09bce8bab69e4485cacf64@5.9.72.212:3000,0075beaca29af670b9ebe4acf74386d59ff5c365@77.68.90.48:26656,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656,dc3037694a6bb18c1d570bb4c6278323a9286de8@5.9.48.85:36656,85591aa9be728b7f705382794a5c1d73dae8f2ae@141.94.196.138:26656,ccb1f620a420bc4c2286ad816aca5c9656869430@45.34.1.114:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
