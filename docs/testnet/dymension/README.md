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
peers="3df2154255d44bee7f036531e7575bdff152207f@51.178.65.184:27656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,f8175ce7bc19d015ec17083fe19b80eae2bd2a9c@65.21.239.60:46656,5d689e09a129c03c003f05850262f03b2433a384@51.79.30.141:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,8d5eac1042bac34cddd25d7601789fc03cb3f3a9@168.119.213.113:46656,236b71988898dff63cef139f83a64f5fbfd9d8d7@135.181.18.112:55696,11fe4c887e890c03cd109f61e8a80ecb77873013@134.209.184.190:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
