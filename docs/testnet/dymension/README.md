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
peers="54160abe97cd71abb3a83516fd8e4a47cb509fba@188.34.178.103:46656,6011e62596d177073f3bed476622162652ab4310@164.68.105.143:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,e5c22b3a303e323e7292d96f5aa2bc46140488f8@65.109.229.198:46656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,9111fd409e5521470b9b33a46009f5e53c646a0d@178.62.81.245:45656,dddc76ca6279ac90b12cf35b39c46a2fc2c2ce52@5.161.78.48:46656,7c720f2d079174ed7ce478b026ac3906a630d716@167.99.178.186:26656,f11d87d4d7ed4497b446b0071ca59096126da671@165.22.96.174:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
