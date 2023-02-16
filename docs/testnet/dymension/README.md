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
peers="e8a706e3a81a36a6dded6cc02eabaf5d355f4c1d@80.79.5.171:28656,1f2b68851c8b17ed796e67af3c6734343e8a2684@65.108.97.58:2446,e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,f11d87d4d7ed4497b446b0071ca59096126da671@165.22.96.174:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,c15187cf9ea7a304499e5ae65facb53bea1e7fd7@45.79.87.51:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
