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
peers="5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,3990d5a402ca8f9e53441b02e22f4558c5c85fc5@65.108.44.149:27756,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,3a9defcd334cefd6b8143ec1ecd8be5e51f1c1c5@95.214.53.46:46656,4aa182ce191cd089929544fe0612d33a02a2cde9@46.17.250.145:26656,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,5f708c16d745b30a839c9f5b4d378fa10a76edd0@3.145.187.21:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
