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
peers="8f3b17746be8f6faba3457c1e039e4a2fe3cb483@65.108.111.32:26656,fee838fe0381b3f74538a36d643991ceca3793c8@65.108.141.109:8656,6f8eddb672e93eb3362a7cb1c843a4e26af71ebc@149.202.72.186:26629,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.235:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656,54d4bf577c2dce3a8137d8fe7820b46d199344e5@135.181.76.35:26656,0edce41e754e9bb9a228d4d2b0878713f6bd6de9@65.108.99.169:26656,d9307d7d7e219461ab9c333104780181b6933e74@89.58.50.116:26656,dc3037694a6bb18c1d570bb4c6278323a9286de8@5.9.48.85:36656,a67a6e354a0a910149bdb13c985ca5ac16a333cd@217.160.249.168:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
