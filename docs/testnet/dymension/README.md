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
peers="fe02e0280c6aedfeaea6f0d8e828dbc53f34e69a@91.107.232.129:26656,1f2b68851c8b17ed796e67af3c6734343e8a2684@65.108.97.58:2446,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,6011e62596d177073f3bed476622162652ab4310@164.68.105.143:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,54160abe97cd71abb3a83516fd8e4a47cb509fba@188.34.178.103:46656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,c15187cf9ea7a304499e5ae65facb53bea1e7fd7@45.79.87.51:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
