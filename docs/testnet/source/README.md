# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" width="150" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: OFF

[Website](https://www.sourceprotocol.io/) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)




## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: source-testnet.grpc.kjnodes.com:28090

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

**live-peers** (9)
```bash
peers="a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,c749b47c438842d9874b515de130dfb11431360f@147.182.211.27:26656,3842f067439c4221e9f9535cdf59d22984d58fed@66.94.123.47:26656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
