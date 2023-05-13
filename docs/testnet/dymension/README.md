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
peers="fc827d9c55d49f0adb31720c134bd8f675ca7b27@95.216.193.163:26656,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
