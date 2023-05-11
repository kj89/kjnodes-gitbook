# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:14690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:14656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:14659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (10)
```bash
peers="ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,e891edc820240a032c89a2ae8f17e3d1d44ecaf9@15.204.31.186:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,96ffe4b68c3f97cbeae4b4362634bf1054c7aeeb@142.132.151.99:15658,88a1109df9ce1e7ad3b1a4c5183a602605cb2b2f@89.116.26.219:26656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,802b8783727af8094d81f9cb0bf2ad9cc3d32aa0@193.46.243.144:26656,dddc76ca6279ac90b12cf35b39c46a2fc2c2ce52@5.161.78.48:46656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
