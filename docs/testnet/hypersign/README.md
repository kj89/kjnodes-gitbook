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
peers="a275d8018f683f279bf5167a72d294bfacafa839@178.63.102.172:41656,7b67ef0b793f09bc1bc76d29aa1503aab8a224ad@88.99.161.162:15656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,d72875380d7b0b68f071623996bd5a86b7491287@116.202.227.117:31656,23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
