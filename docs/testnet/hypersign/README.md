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
peers="5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,b946e1722d17420f911dd58d716964b43dfd12a9@65.108.238.217:11204,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556,3990d5a402ca8f9e53441b02e22f4558c5c85fc5@65.108.44.149:27756,2641ddcf28d8adf448edb573de1efba0b6971d9e@178.154.222.128:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,aa8c0064e866dc57b341a389006df8925a0718fe@5.161.55.130:31656,f277d5a80e789ce69bb3318dfd5efea45986c073@176.9.22.117:31656,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
