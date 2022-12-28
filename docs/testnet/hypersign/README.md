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
peers="22d2b3587e2ce6ae750c189b12461e7315d08ae4@167.235.151.119:26656,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856,5cd888a5c37474ca778277cfd9dee7d24fe96094@95.217.214.107:26656,3a9defcd334cefd6b8143ec1ecd8be5e51f1c1c5@95.214.53.46:46656,4aa182ce191cd089929544fe0612d33a02a2cde9@46.17.250.145:26656,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,cf94099349980f9593a3f0362c85fe7c6eda8b14@8.219.48.59:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
