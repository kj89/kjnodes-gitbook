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

**live-peers** (11)
```
peers="f277d5a80e789ce69bb3318dfd5efea45986c073@176.9.22.117:31656,23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,22d2b3587e2ce6ae750c189b12461e7315d08ae4@167.235.151.119:26656,89783a7453e69634cde9f9e4b2fd4309fb5298e5@161.97.172.20:26656,52eee2c34150d621312087e49f118969472ba55f@149.102.137.192:26656,5cd888a5c37474ca778277cfd9dee7d24fe96094@95.217.214.107:26656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,4aa182ce191cd089929544fe0612d33a02a2cde9@46.17.250.145:26656,7991e99ee8c05906a2161d8b47d826240da5c5d2@54.254.83.241:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
