# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="e34cc8a12a5274272ff861b4fe3042e98697e500@46.17.250.108:60956,040d0b6ffefba3283b5763e26c352c7b1b232c1f@65.109.90.171:34656,b5494479585215f109efcfedb9083f623c888fde@159.69.209.122:18656,046e5fdfcf33f221da082b8e4161689bcb915135@77.91.84.30:39656,5f1bcdfe67b0cd55ed12a06454206c7f1ab4b35b@95.216.160.203:26656,e5ec693f420974e252ddbb488670925cc7e3524a@37.120.191.47:60756,7f61eb8869a103eac4a0ad02bd7ce1f42c0041bc@5.9.59.220:33656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,f47667544d7d5b65f316ba5ab8fca2e81e8fe4f4@157.90.208.222:36656,ad417c4efa59e21b43e8e256c73b9939f1c22a0e@23.88.42.28:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
