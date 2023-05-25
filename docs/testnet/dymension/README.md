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
peers="1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,fc827d9c55d49f0adb31720c134bd8f675ca7b27@95.216.193.163:26656,3fdba29b1d02066f6406c611e1ae42e9ec76bbf2@185.197.194.227:26656,b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,95f016933b6b25a44a3b1257a45af1db3335ae61@65.109.30.110:11773,d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,b96cd46ed999632cf6d4e8896e83421277d319bf@65.109.107.219:44656,8c4da005c8a68682402293f951449f042e6f3dbf@164.92.190.234:21456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
