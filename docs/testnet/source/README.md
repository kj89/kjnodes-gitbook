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
peers="b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,383a0684aadfe507e097c36b34d6243da59d9ed5@207.180.232.91:26656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,b958d18452ec5458323606d934906cc90d462203@194.233.93.124:26656,3cbc833fd321709754d194189dd0622ce4d7c642@135.181.144.20:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
