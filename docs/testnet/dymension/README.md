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
peers="e678f78d3250fef1e6e0afcdb1ebdc5fe0d7138c@5.161.76.147:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652,e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,8d5eac1042bac34cddd25d7601789fc03cb3f3a9@168.119.213.113:46656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,f4be55edab4b5cb40464aa50def5d2cd39359e67@185.182.185.101:26656,5a0cee849e4a909b42c8b9b2df4a1e737ff2b715@194.233.90.134:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
