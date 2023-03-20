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
peers="ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,8d5eac1042bac34cddd25d7601789fc03cb3f3a9@168.119.213.113:46656,78bc26c40c20715ca134b5d47a318a90dde95f12@78.46.61.117:04656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,e6ea3444ac85302c336000ac036f4d86b97b3d3e@38.146.3.199:20556,f91eda7a7c64cebd5ad465613b15ea8e8f78aebc@194.163.164.1:26656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,33ed8cb97aa678c7e4578ab39ac93ac94db426bb@95.217.236.79:46656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,8e0c3fc76a3c7510d28fff02d452ccf952450ca9@89.117.48.191:26656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
