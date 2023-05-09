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
peers="af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,6cf94ed068c7401ba8e6f9a49143fd90df415e83@195.201.237.198:46656,82b51653205df40d43f257041db2da0f9f1644fa@178.63.26.94:46656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,88a1109df9ce1e7ad3b1a4c5183a602605cb2b2f@89.116.26.219:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,3a2379acd357b59f70ac355e0f2ad23661d45932@65.21.200.7:8000,63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
