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
peers="a20572bc932668cf9f66598e9adc4151949da458@65.108.128.168:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.45.253:26656,dc3037694a6bb18c1d570bb4c6278323a9286de8@5.9.48.85:36656,f5fa74f9a41b3d71f29a95cb1c90717e193a337d@23.111.163.2:26656,663675af3a1ea846d7824fd6ad087b6b576bbd05@136.243.94.138:36656,b1ddf96ff6db5cfe77fa9c88dc2925f4525d0a02@141.94.141.144:56656,ce764e158a4a29a4af7606c38c44e976c69b3982@144.91.78.94:26656,0075beaca29af670b9ebe4acf74386d59ff5c365@77.68.90.48:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.104:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
