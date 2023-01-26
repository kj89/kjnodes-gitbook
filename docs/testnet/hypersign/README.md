# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.5 | **Wasm**: OFF

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
peers="23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,1380864bb38481fef4b2358026a5ed53fc027679@95.214.52.206:26656,f1e8d741d7437d62c15337e5f7475e139119cf8b@65.108.229.233:31656,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,3a9defcd334cefd6b8143ec1ecd8be5e51f1c1c5@95.214.53.46:46656,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,ca474a224fe7eaaefa6d336a205459b33fb30654@3.90.236.173:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
