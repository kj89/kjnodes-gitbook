# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)




## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: [https://dymension-testnet.grpc.kjnodes.com](https://dymension-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:46656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:46659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (10)
```bash
peers="ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,a2e32d18a3bbcfeacf13ad6d82a096f2efdfd53c@170.64.182.38:26656,f2d185a19f27e8290163d63a28846601662b50f1@138.201.204.5:40656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,f8175ce7bc19d015ec17083fe19b80eae2bd2a9c@65.21.239.60:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
