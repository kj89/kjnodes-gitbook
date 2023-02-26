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
peers="d0bf1f313c3fe5d9e890f7754950238493497211@62.171.178.217:26656,fae907ab505bfd41fc2499bd002fd58adc6fc68a@173.249.26.69:26656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,6e4cdcb3039f1f8e97b8511c3b146cd14d41dc3d@65.109.112.20:11084,63d1b126558468634137b5705ab90151b16932f8@65.108.151.6:26656,829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,2c20351736d27e50952695801a4d77122ead307f@62.171.180.83:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
