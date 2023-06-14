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
peers="a8475788f47e385cba9f505c7c6de95124377212@142.132.178.2:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,7f928378eecafe22fe1e93d9f63db181cec3f8a3@145.239.143.76:11256,0d7ec1ea841e763267f197e2e0aa89467da24064@94.19.249.187:35656,be789ab36bc298b491735f2313d5f99abf452d1f@162.55.246.165:26656,f8175ce7bc19d015ec17083fe19b80eae2bd2a9c@65.21.239.60:46656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,f4be55edab4b5cb40464aa50def5d2cd39359e67@185.182.185.101:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
