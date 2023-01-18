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
peers="23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,1380864bb38481fef4b2358026a5ed53fc027679@95.214.52.206:26656,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856,3990d5a402ca8f9e53441b02e22f4558c5c85fc5@65.108.44.149:27756,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,aa8c0064e866dc57b341a389006df8925a0718fe@5.161.55.130:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,f277d5a80e789ce69bb3318dfd5efea45986c073@176.9.22.117:31656,cf94099349980f9593a3f0362c85fe7c6eda8b14@8.219.48.59:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
