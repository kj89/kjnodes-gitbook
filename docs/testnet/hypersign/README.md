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
peers="22d2b3587e2ce6ae750c189b12461e7315d08ae4@167.235.151.119:26656,89783a7453e69634cde9f9e4b2fd4309fb5298e5@161.97.172.20:26656,5b4482bfe02384184470070c3d3a4465cf0c18d4@144.91.82.61:31656,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,f277d5a80e789ce69bb3318dfd5efea45986c073@176.9.22.117:31656,cf94099349980f9593a3f0362c85fe7c6eda8b14@8.219.48.59:26656,7991e99ee8c05906a2161d8b47d826240da5c5d2@54.254.83.241:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
