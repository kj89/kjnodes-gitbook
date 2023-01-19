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
peers="f277d5a80e789ce69bb3318dfd5efea45986c073@176.9.22.117:31656,23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,e7bb31c8fdd8d26a739bfd87cdf3ba7a8f90406e@65.21.145.228:31656,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,ce6686036f6554deb0490103dcc201172e7c3f2f@81.0.220.131:26656,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,aa8c0064e866dc57b341a389006df8925a0718fe@5.161.55.130:31656,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656,3a9defcd334cefd6b8143ec1ecd8be5e51f1c1c5@95.214.53.46:46656,5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
