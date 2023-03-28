# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:46090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:46656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:46659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (20)
```bash
peers="e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,cb55a7878bc9a079446a42dd134d2facd7724a12@134.122.121.129:46656,88a1109df9ce1e7ad3b1a4c5183a602605cb2b2f@89.116.26.219:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,e8a706e3a81a36a6dded6cc02eabaf5d355f4c1d@80.79.5.171:28656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,2afd537c6cca30a46393545a6aa69235d3fdb398@38.242.241.117:26656,64acca240c1149f94b8986ffea3ee1b4e0bd5fbe@45.150.64.115:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,54160abe97cd71abb3a83516fd8e4a47cb509fba@188.34.178.103:46656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
