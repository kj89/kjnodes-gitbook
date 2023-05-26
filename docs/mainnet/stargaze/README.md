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

**live-peers** (11)
```bash
peers="fc668bbf7e34d6926308487348b2655159198f1d@135.181.128.114:13756,b99beb75e753224b2cf6b3dd8db48b47047c56f6@135.181.162.122:26656,344c62c700a59de6137ccd6cade56721cb1e9777@142.132.202.86:26656,7798342ae6f07e5c2e09bce8bab69e4485cacf64@5.9.72.212:3000,6f8eddb672e93eb3362a7cb1c843a4e26af71ebc@149.202.72.186:26629,4eeadb9b2af44a34252c8ba236a29fa4eb6931ab@141.95.155.224:10156,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.235:26656,bb5a32a9301b06cd4f30c0e45ca023213c95e9f6@213.133.111.71:36656,ccb1f620a420bc4c2286ad816aca5c9656869430@45.34.1.114:36656,673ad0cb62287afcdbe5e5c88b91e39ee1bd394a@65.21.181.67:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
