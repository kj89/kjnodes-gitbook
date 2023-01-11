# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.5 | **Wasm**: OFF

[Website](https://hypersign.id) | [Discord](https://discord.gg/DmuUjMrHVw) | [Twitter](https://twitter.com/hypersignchain)


## Public endpoints

* rpc: [https://hypersign-testnet.rpc.kjnodes.com](https://hypersign-testnet.rpc.kjnodes.com)
* api: [https://hypersign-testnet.api.kjnodes.com](https://hypersign-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@hypersign-testnet.rpc.kjnodes.com:31656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:31659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json
```

**live-peers** (10)
```bash
peers="7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,4aa182ce191cd089929544fe0612d33a02a2cde9@46.17.250.145:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656,23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
