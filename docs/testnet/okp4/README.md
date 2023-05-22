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
peers="1f4fa23210cc1d086a928a3c6de7c24f6c8f17ba@202.61.226.120:16656,78d923333e39e747c6a7fbfcc822ec6279990556@91.211.251.232:28656,d1c1b729eff9afe7dfd371f190df6282c82ccfad@65.109.89.5:31656,44c4ad482cf8f1d9e7e18968da78bd0349fe853e@5.78.54.193:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,1e48c09a0f78070e90ed49b2e3d59f8fdc188e74@162.55.234.70:55156,14f8949ab0a276d2e55c8fa6255430881978a619@185.192.96.236:26656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
