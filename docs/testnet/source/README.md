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
peers="bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,63d1b126558468634137b5705ab90151b16932f8@65.108.151.6:26656,d0bf1f313c3fe5d9e890f7754950238493497211@62.171.178.217:26656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656,14d1da3e6798ae897a551d179f91c4c4434d633f@178.20.43.18:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
