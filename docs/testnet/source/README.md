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
peers="829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,3842f067439c4221e9f9535cdf59d22984d58fed@66.94.123.47:26656,4014d58eda8c78772e080ac4e7f60ec89db307e5@65.109.175.130:26656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
