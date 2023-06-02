# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (12)
```bash
peers="954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,613e133355a43be28b31d33d13c8814d6ea0c99f@34.75.8.154:26656,2d674121d87cfd1e03654da8fda7ec9f21e46713@65.109.233.78:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,61c3b93bc69ed2b209ffbf959c4a5701e6eb7416@95.217.163.250:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
