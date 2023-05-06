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
peers="1e48c09a0f78070e90ed49b2e3d59f8fdc188e74@162.55.234.70:55156,77324cc79d15d8bef4cc7462395062d73f51ad62@65.109.38.208:46656,d1c1b729eff9afe7dfd371f190df6282c82ccfad@65.109.89.5:31656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,61544968b65e34a59513b67613519cd37ace7ecb@161.97.151.109:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,14f8949ab0a276d2e55c8fa6255430881978a619@185.192.96.236:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13656,9392c27a9a561c31e7a920dc6f577d663c473ef8@154.12.225.88:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
