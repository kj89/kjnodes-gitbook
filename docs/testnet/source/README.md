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
peers="ddb472d197b8a732bb3f8878035603769aa4c85b@161.35.75.82:26656,829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,6e4cdcb3039f1f8e97b8511c3b146cd14d41dc3d@65.109.112.20:11084,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
