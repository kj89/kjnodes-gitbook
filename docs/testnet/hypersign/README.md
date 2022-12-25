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
peers="2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,22d2b3587e2ce6ae750c189b12461e7315d08ae4@167.235.151.119:26656,4aa182ce191cd089929544fe0612d33a02a2cde9@46.17.250.145:26656,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,aa8c0064e866dc57b341a389006df8925a0718fe@5.161.55.130:31656,ac25bdc230944cc20f03913a8dae881c9b5f9c18@3.239.45.125:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,5b4482bfe02384184470070c3d3a4465cf0c18d4@144.91.82.61:31656,f1e8d741d7437d62c15337e5f7475e139119cf8b@65.108.229.233:31656,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
