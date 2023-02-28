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
peers="b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,4014d58eda8c78772e080ac4e7f60ec89db307e5@65.109.175.130:26656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,63d1b126558468634137b5705ab90151b16932f8@65.108.151.6:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,14d1da3e6798ae897a551d179f91c4c4434d633f@178.20.43.18:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
