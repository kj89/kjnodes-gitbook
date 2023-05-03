# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/okp4.png" alt=""><figcaption></figcaption></figure>

OKP4 is a revolutionary public blockchain protocol where communities are incentivized to  share data and services confidently. To maximize value from data, it needs to be processed  by complex algorithms and pooled with other datasets, to create valuable knowledge.

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v4.1.0 | **Wasm**: OFF

[Website](https://okp4.network) | [Discord](https://discord.gg/okp4) | [Twitter](https://twitter.com/OKP4_Protocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/okp4-testnet](https://explorer.kjnodes.com/okp4-testnet)

## Public endpoints

* api: [https://okp4-testnet.api.kjnodes.com](https://okp4-testnet.api.kjnodes.com)
* rpc: [https://okp4-testnet.rpc.kjnodes.com](https://okp4-testnet.rpc.kjnodes.com)
* grpc: okp4-testnet.grpc.kjnodes.com:13690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@okp4-testnet.rpc.kjnodes.com:13656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@okp4-testnet.rpc.kjnodes.com:13659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/okp4-testnet/addrbook.json > $HOME/.okp4d/config/addrbook.json
```

**live-peers** (10)
```bash
peers="42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,78d923333e39e747c6a7fbfcc822ec6279990556@91.211.251.232:28656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,c665d7fd39015a805f1af935293fefdc825a6b6b@185.144.99.16:26656,23e895e7d650f43e1f53522165607b71685f8cfa@65.108.75.107:26656,77324cc79d15d8bef4cc7462395062d73f51ad62@65.109.38.208:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13656,d1c1b729eff9afe7dfd371f190df6282c82ccfad@65.109.89.5:31656,82bb185819e5cf2bb6a9896447672efca27f28cb@65.109.15.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
