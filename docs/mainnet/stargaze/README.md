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
peers="4d5f5f3cf22a302041d262afbdb8592b8ad3e1a2@65.108.78.167:11956,1e1237931e262cd7a00803dfa1ce51b7a36eb1fa@194.163.150.135:26656,dc3037694a6bb18c1d570bb4c6278323a9286de8@5.9.48.85:36656,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656,5fb6adba37bfa000cf911124c4feb934a1f7ac88@65.108.237.88:26656,fc668bbf7e34d6926308487348b2655159198f1d@135.181.128.114:13756,7bca4f963ddc1d3863e0cc1815beab219e33302e@65.21.198.130:46656,54d4bf577c2dce3a8137d8fe7820b46d199344e5@135.181.76.35:26656,bae0d94b8f0f3dc8ea167a764e119c01dc2456f0@66.206.6.58:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
