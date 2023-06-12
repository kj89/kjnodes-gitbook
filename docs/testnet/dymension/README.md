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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,fc827d9c55d49f0adb31720c134bd8f675ca7b27@95.216.193.163:26656,fde02d17cdfda6e642290ea6d1e50771629a88ef@213.239.215.195:39095,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,68f6c52147c9423300f5b503348bbb02b229820c@51.159.153.211:26656,09927421cd3aa47bc81f8f981e15c547bc490121@5.9.83.110:26656,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,5a0cee849e4a909b42c8b9b2df4a1e737ff2b715@194.233.90.134:26656,fe02e0280c6aedfeaea6f0d8e828dbc53f34e69a@91.107.232.129:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
