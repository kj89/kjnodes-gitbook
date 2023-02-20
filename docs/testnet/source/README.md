# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/source.png" width="150" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: OFF

[Website](https://www.sourceprotocol.io/) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)




## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: [https://source-testnet.grpc.kjnodes.com](https://source-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:28656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:28659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (10)
```bash
peers="b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,14d1da3e6798ae897a551d179f91c4c4434d633f@178.20.43.18:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,9f9d7c982cf37dd113192c6d4a5c4c0ac1997a25@185.22.152.217:26656,3842f067439c4221e9f9535cdf59d22984d58fed@66.94.123.47:26656,9260303a16969bbf4360b462d80ce12f77c4d3a1@43.131.35.28:26656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,c5eccf228a25f979592297311bfe2cc8ef94e482@95.111.229.159:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
