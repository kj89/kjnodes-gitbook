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

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@hypersign-testnet.rpc.kjnodes.com:31656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:31659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json
```

**live-peers** (10)
```
peers="2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,5cd888a5c37474ca778277cfd9dee7d24fe96094@95.217.214.107:26656,ce6686036f6554deb0490103dcc201172e7c3f2f@81.0.220.131:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856,7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,5b4482bfe02384184470070c3d3a4465cf0c18d4@144.91.82.61:31656,91089c0911b59f59fe2ec79fdae017f9beefbbfd@65.108.101.158:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
