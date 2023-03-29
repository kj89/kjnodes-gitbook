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
peers="7c720f2d079174ed7ce478b026ac3906a630d716@167.99.178.186:26656,ed26b4f13a7f388064aa89e5d6419b0e78e3e94e@209.126.81.190:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,07aa2f136bab33435df2ed64ba524b0ce19ec9d8@31.220.90.150:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,cffb2a5e8fe08ba5ce46a8f56a4a1cdf636cbf8e@5.231.205.142:26656,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,617214edc6dbd3d82765d66767ca56deb9660851@134.209.21.58:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,e678f78d3250fef1e6e0afcdb1ebdc5fe0d7138c@5.161.76.147:46656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
