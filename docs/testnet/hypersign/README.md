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
peers="23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,ce6686036f6554deb0490103dcc201172e7c3f2f@81.0.220.131:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,89783a7453e69634cde9f9e4b2fd4309fb5298e5@161.97.172.20:26656,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,5f708c16d745b30a839c9f5b4d378fa10a76edd0@3.145.187.21:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
