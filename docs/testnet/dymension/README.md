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
peers="747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,e8a706e3a81a36a6dded6cc02eabaf5d355f4c1d@80.79.5.171:28656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,da812134fe8148863dfea7ba9615e5444291c45a@5.231.205.142:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,47921c153041fb2f048c1e174b6d02ac0efab7a9@38.242.207.16:26656,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,998b19ed2c580acaa2fdb5057e2930a38f041750@65.109.122.105:60556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
