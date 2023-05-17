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

**live-peers** (11)
```bash
peers="68f6c52147c9423300f5b503348bbb02b229820c@51.159.153.211:26656,802b8783727af8094d81f9cb0bf2ad9cc3d32aa0@193.46.243.144:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,6ebe5856a7617cb9309a923a3935687903d2607d@141.95.97.28:15256,64acca240c1149f94b8986ffea3ee1b4e0bd5fbe@45.150.64.115:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,8c3d6e4d065c6c171e2620f8ed8be5404fa61923@162.55.1.176:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
