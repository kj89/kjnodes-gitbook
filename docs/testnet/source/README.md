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
peers="4466740c40895b6aad60a434f0ad3e3c5d5fe53c@213.239.216.252:22656,9260303a16969bbf4360b462d80ce12f77c4d3a1@43.131.35.28:26656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656,c749b47c438842d9874b515de130dfb11431360f@147.182.211.27:26656,4014d58eda8c78772e080ac4e7f60ec89db307e5@65.109.175.130:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,b958d18452ec5458323606d934906cc90d462203@194.233.93.124:26656,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
