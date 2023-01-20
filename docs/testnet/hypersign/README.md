# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.5 | **Wasm**: OFF

[Website](https://hypersign.id) | [Discord](https://discord.gg/DmuUjMrHVw) | [Twitter](https://twitter.com/hypersignchain)


## Public endpoints

* api: [https://hypersign-testnet.api.kjnodes.com](https://hypersign-testnet.api.kjnodes.com)
* rpc: [https://hypersign-testnet.rpc.kjnodes.com](https://hypersign-testnet.rpc.kjnodes.com)
* grpc: [https://hypersign-testnet.grpc.kjnodes.com](https://hypersign-testnet.grpc.kjnodes.com)

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
peers="2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,e7bb31c8fdd8d26a739bfd87cdf3ba7a8f90406e@65.21.145.228:31656,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,ce6686036f6554deb0490103dcc201172e7c3f2f@81.0.220.131:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
