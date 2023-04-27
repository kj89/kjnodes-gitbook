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
peers="eee6cb357d3248ea8c6138fea2d8004963d32743@65.108.138.80:13756,54d4bf577c2dce3a8137d8fe7820b46d199344e5@135.181.76.35:26656,8f3b17746be8f6faba3457c1e039e4a2fe3cb483@65.108.111.32:26656,d3393f1ddc2b2f1ad4e91d86b429576ab1ed241f@195.154.99.18:28454,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,7ff48cc8533f31c1c14a687a0a193164dbefec38@194.163.171.38:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656,7bca4f963ddc1d3863e0cc1815beab219e33302e@65.21.198.130:46656,ce764e158a4a29a4af7606c38c44e976c69b3982@144.91.78.94:26656,0edce41e754e9bb9a228d4d2b0878713f6bd6de9@65.108.99.169:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
