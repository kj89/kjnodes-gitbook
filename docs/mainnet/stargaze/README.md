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
peers="ff10ddf3e5853586cfeab268cbab77ccbabf6927@188.166.148.13:26656,a2d1e7db5fa370d1dfbc145f86c228202c270358@154.53.50.18:26656,f5fa74f9a41b3d71f29a95cb1c90717e193a337d@23.111.163.2:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,6c7a904400f646e43eaf1ea76976de037392efa1@23.88.69.22:26566,bb5a32a9301b06cd4f30c0e45ca023213c95e9f6@213.133.111.71:36656,8f3b17746be8f6faba3457c1e039e4a2fe3cb483@65.108.111.32:26656,673ad0cb62287afcdbe5e5c88b91e39ee1bd394a@65.21.181.67:26656,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,b99beb75e753224b2cf6b3dd8db48b47047c56f6@135.181.162.122:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
