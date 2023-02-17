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
peers="76894391ff3fb5937654758b12d1eecd69eb943e@161.97.151.64:26656,2c20351736d27e50952695801a4d77122ead307f@62.171.180.83:26656,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,b7ac13fa32c668611408a3dc9c15b092cea98db1@185.250.37.203:26656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,14d1da3e6798ae897a551d179f91c4c4434d633f@178.20.43.18:26656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
