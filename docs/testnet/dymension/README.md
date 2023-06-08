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

**live-peers** (9)
```bash
peers="e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,b989bcba871776cf50d39c2e58763677dc082181@45.14.194.130:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,618ef1f11412046f6ae1230704f8d3bd9a3fee68@3.88.104.53:26656,801c31f8571c222764e742bd2fda625d40afe503@65.21.225.178:26666,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,7e1341d989d05c78d1c2f4e2353981a49b9c5829@85.10.203.15:06656,513557be25d2edc51481be90c808f72cd662e1d2@167.235.250.107:26656,e38aa6816fe5a0ac5acaa5f525d9ef7dc90905d1@194.126.173.150:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
