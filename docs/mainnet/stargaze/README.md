# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" width="150" alt=""><figcaption></figcaption></figure>

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
peers="ecd1947cddb25e84d800b4e9967dc98a3f05a38a@95.216.191.134:26656,6c7a904400f646e43eaf1ea76976de037392efa1@23.88.69.22:26566,0075beaca29af670b9ebe4acf74386d59ff5c365@77.68.90.48:26656,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656,c5ca72ea2b6d098ccfa7fc8b9c994fe4db854e2f@162.55.5.230:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.193.223:26656,a323f1878a8c015aa170fc73a8c8c74d508aa01f@138.197.11.201:26656,0edce41e754e9bb9a228d4d2b0878713f6bd6de9@65.108.99.169:26656,eee6cb357d3248ea8c6138fea2d8004963d32743@65.108.138.80:13756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
