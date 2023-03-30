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
peers="ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,96ffe4b68c3f97cbeae4b4362634bf1054c7aeeb@142.132.151.99:15658,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,6011e62596d177073f3bed476622162652ab4310@164.68.105.143:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,07aa2f136bab33435df2ed64ba524b0ce19ec9d8@31.220.90.150:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,54160abe97cd71abb3a83516fd8e4a47cb509fba@188.34.178.103:46656,2afd537c6cca30a46393545a6aa69235d3fdb398@38.242.241.117:26656,e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,617214edc6dbd3d82765d66767ca56deb9660851@134.209.21.58:26656,147a0021cff3c34251adb3ad7194574011fa3192@176.57.189.36:11656,ed26b4f13a7f388064aa89e5d6419b0e78e3e94e@209.126.81.190:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,3a8bb83d5c5afb13ae2c1c3b91c97928e277f6a5@142.132.205.94:15658,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,6229800969107d039254a8e6888aaeb464cda44d@167.99.186.186:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
