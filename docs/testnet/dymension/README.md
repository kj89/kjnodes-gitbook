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
peers="b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,513557be25d2edc51481be90c808f72cd662e1d2@167.235.250.107:26656,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
