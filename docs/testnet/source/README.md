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
peers="a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,383a0684aadfe507e097c36b34d6243da59d9ed5@207.180.232.91:26656,b7ac13fa32c668611408a3dc9c15b092cea98db1@185.250.37.203:26656,8074071b4d046f400a10e26b331a5a10c27c1b37@185.250.37.206:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656,f6e7cb4ee4d608822802f58c85e93a7e34ce440d@65.108.237.232:28656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,05dbcd1bb0563107c5eeb98a8da9d6cd9197bfcd@65.21.129.95:21756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
