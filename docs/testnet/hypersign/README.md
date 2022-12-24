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
peers="23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,f277d5a80e789ce69bb3318dfd5efea45986c073@176.9.22.117:31656,7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,84408be4e3f13dcd976568d6370e1c50e9eb614d@185.252.232.110:46656,89783a7453e69634cde9f9e4b2fd4309fb5298e5@161.97.172.20:26656,5cd888a5c37474ca778277cfd9dee7d24fe96094@95.217.214.107:26656,ac25bdc230944cc20f03913a8dae881c9b5f9c18@3.239.45.125:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
