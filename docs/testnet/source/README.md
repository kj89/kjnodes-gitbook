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
peers="4466740c40895b6aad60a434f0ad3e3c5d5fe53c@213.239.216.252:22656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,d0bf1f313c3fe5d9e890f7754950238493497211@62.171.178.217:26656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
