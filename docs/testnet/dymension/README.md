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
peers="54160abe97cd71abb3a83516fd8e4a47cb509fba@188.34.178.103:46656,09927421cd3aa47bc81f8f981e15c547bc490121@5.9.83.110:26656,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,c36184fec2fb60bf7be775390c1cd6619c0201ef@209.126.81.240:26656,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,88a1109df9ce1e7ad3b1a4c5183a602605cb2b2f@89.116.26.219:26656,cffb2a5e8fe08ba5ce46a8f56a4a1cdf636cbf8e@5.231.205.142:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,7c720f2d079174ed7ce478b026ac3906a630d716@167.99.178.186:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
