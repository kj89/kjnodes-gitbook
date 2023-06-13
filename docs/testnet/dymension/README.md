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
peers="d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,b989bcba871776cf50d39c2e58763677dc082181@45.14.194.130:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,adf394846dc942b1fd03f6e310eda60b5eda7848@195.201.197.4:32656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,f4be55edab4b5cb40464aa50def5d2cd39359e67@185.182.185.101:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,fc827d9c55d49f0adb31720c134bd8f675ca7b27@95.216.193.163:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
