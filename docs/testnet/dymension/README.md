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
peers="e4dec3315020ac14bc82e6f4b0696d1b0f65d999@138.201.204.5:40656,4e94581e03f46c2bda293fa47db05c2fa8883256@190.102.106.50:29656,82b51653205df40d43f257041db2da0f9f1644fa@178.63.26.94:46656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,68f6c52147c9423300f5b503348bbb02b229820c@51.159.153.211:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,8a66c13470c05acbd4d8711d21adbb67cc03dd1f@45.151.123.238:26656,b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,44df333024cebe9b8e8361ac67feaa930ec6dc1f@65.109.85.170:54656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
