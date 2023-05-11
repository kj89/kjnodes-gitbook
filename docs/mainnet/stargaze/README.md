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
peers="673ad0cb62287afcdbe5e5c88b91e39ee1bd394a@65.21.181.67:26656,7798342ae6f07e5c2e09bce8bab69e4485cacf64@5.9.72.212:3000,6c7a904400f646e43eaf1ea76976de037392efa1@23.88.69.22:26566,344c62c700a59de6137ccd6cade56721cb1e9777@142.132.202.86:26656,c565abfb2686a51764dca1bacb5280098dda06a5@65.21.236.33:26656,4eeadb9b2af44a34252c8ba236a29fa4eb6931ab@141.95.155.224:10156,fc668bbf7e34d6926308487348b2655159198f1d@135.181.128.114:13756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,56a776a589fbc4d038db956791bcf75204c67872@172.105.112.35:26656,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
