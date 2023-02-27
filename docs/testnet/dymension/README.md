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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,998b19ed2c580acaa2fdb5057e2930a38f041750@65.109.122.105:60556,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,88fdaf5ff074dc2010ccb0416e421f3819201eb6@212.23.222.125:30586,65242d54d20a6c16a401004a8fb936343d9cae99@65.109.106.91:26656,d995d7079d975dea118a16014758838fe5cb8e2d@80.240.29.76:26656,e1d6bdf47f76bdfdba90d4bedc780539d9766bbe@172.104.199.176:26656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
