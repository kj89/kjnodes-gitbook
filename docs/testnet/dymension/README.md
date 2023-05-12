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
peers="4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,ed76fabd897c8911942ac4fa1c91f3f0afa7fdda@65.108.225.70:26656,c5db84267f7dce8fa249b0d5365d59a7abeb0164@95.217.211.32:46656,88a1109df9ce1e7ad3b1a4c5183a602605cb2b2f@89.116.26.219:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
