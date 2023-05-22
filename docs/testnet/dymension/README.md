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
peers="43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,30f4b85a5505a80204693f5971e7bb18920e6e68@168.119.180.142:26656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,e891edc820240a032c89a2ae8f17e3d1d44ecaf9@15.204.31.186:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
