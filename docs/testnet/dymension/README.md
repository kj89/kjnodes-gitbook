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
peers="1dba47148fef299a00d7803af5d4c3d02c002fbd@209.97.136.200:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,6cf94ed068c7401ba8e6f9a49143fd90df415e83@195.201.237.198:46656,8d5eac1042bac34cddd25d7601789fc03cb3f3a9@168.119.213.113:46656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,fde02d17cdfda6e642290ea6d1e50771629a88ef@213.239.215.195:39095,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
