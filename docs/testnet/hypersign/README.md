# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.6 | **Wasm**: OFF

[Website](https://hypersign.id) | [Discord](https://discord.gg/DmuUjMrHVw) | [Twitter](https://twitter.com/hypersignchain)




## Chain explorer
[https://explorer.kjnodes.com/hypersign-testnet](https://explorer.kjnodes.com/hypersign-testnet)

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
peers="7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,efcb16ec33d8e6233d1068fff679c6fd64bf5802@65.108.225.158:10956,a275d8018f683f279bf5167a72d294bfacafa839@178.63.102.172:41656,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
