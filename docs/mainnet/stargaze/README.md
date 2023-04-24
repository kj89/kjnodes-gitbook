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
peers="c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.45.253:26656,afbbff9114b9e542aea7d07523f5528fc8d05f9b@185.252.220.89:26004,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.193.223:26656,a67a6e354a0a910149bdb13c985ca5ac16a333cd@217.160.249.168:26656,b1ddf96ff6db5cfe77fa9c88dc2925f4525d0a02@141.94.141.144:56656,0d9c5b7b4361cacb7ec5b08b818358f9cf23034b@65.108.66.92:26656,f5fa74f9a41b3d71f29a95cb1c90717e193a337d@23.111.163.2:26656,4da84cfcc0fcc8e144f9fdb4af4b175d8c6864a0@142.93.214.125:26656,d9307d7d7e219461ab9c333104780181b6933e74@89.58.50.116:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
