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
peers="5b4482bfe02384184470070c3d3a4465cf0c18d4@144.91.82.61:31656,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856,ce6686036f6554deb0490103dcc201172e7c3f2f@81.0.220.131:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,15d2f1bc2bfaa143388465ea115c59e5ce6e77dc@65.109.39.223:26656,efcb16ec33d8e6233d1068fff679c6fd64bf5802@65.108.225.158:10956,9876d1b1e5b5968c1c729559325dd909f93c1d34@65.108.238.61:56656,84408be4e3f13dcd976568d6370e1c50e9eb614d@185.252.232.110:46656,cf94099349980f9593a3f0362c85fe7c6eda8b14@8.219.48.59:26656,56615e02aa90e35a20a1fc4c46e78bb00956f07b@192.118.76.199:26681"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
