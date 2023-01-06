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
peers="23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,a275d8018f683f279bf5167a72d294bfacafa839@178.63.102.172:41656,2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,4aa182ce191cd089929544fe0612d33a02a2cde9@46.17.250.145:26656,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
