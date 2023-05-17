# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v9.1.0 | **Wasm**: OFF

[Website](https://hub.cosmos.network) | [Discord](https://discord.gg/cosmosnetwork) | [Twitter](https://twitter.com/cosmoshub)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cosmoshub](https://explorer.kjnodes.com/cosmoshub)

## Public endpoints

* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)
* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* grpc: cosmoshub.grpc.kjnodes.com:13490

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:13456
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:13459
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
```

**live-peers** (10)
```bash
peers="8698cb819c9a4503fe2c71055f1380d08edc5adf@204.16.244.116:26656,6ecca845883e9273062ee515d2657080e6539d9e@65.109.32.148:26726,81062b9a8807a1229543b84bae2898c50a1b1dfc@52.211.169.132:26656,322efd4fdc72a189a2fc8b2b597927831df2bbed@128.0.51.9:26656,4ebf074e8b4a24438bd0bd503b62b4728dfb8eae@35.212.101.35:26656,53b3651680ec3482d736808cbb3035940107f8ab@82.100.58.119:26656,d9dbd30f7e9ae99dc05645f48f4637c2f4a14645@34.107.9.71:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,64a0909aa38311baaba615c6299a4ca9d27fd7ef@44.209.21.229:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
