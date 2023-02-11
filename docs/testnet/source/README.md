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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,ddb472d197b8a732bb3f8878035603769aa4c85b@161.35.75.82:26656,14d1da3e6798ae897a551d179f91c4c4434d633f@178.20.43.18:26656,4466740c40895b6aad60a434f0ad3e3c5d5fe53c@213.239.216.252:22656,b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,9f9d7c982cf37dd113192c6d4a5c4c0ac1997a25@185.22.152.217:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
