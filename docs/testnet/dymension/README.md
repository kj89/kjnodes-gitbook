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
peers="57a66a59cc291887f35e231b4469e2c957728862@46.4.5.45:20556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,fc827d9c55d49f0adb31720c134bd8f675ca7b27@95.216.193.163:26656,e4dec3315020ac14bc82e6f4b0696d1b0f65d999@138.201.204.5:40656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,d995d7079d975dea118a16014758838fe5cb8e2d@80.240.29.76:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
