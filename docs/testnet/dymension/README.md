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
peers="f8175ce7bc19d015ec17083fe19b80eae2bd2a9c@65.21.239.60:46656,8e0c3fc76a3c7510d28fff02d452ccf952450ca9@89.117.48.191:26656,33ed8cb97aa678c7e4578ab39ac93ac94db426bb@95.217.236.79:46656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,a9444e3bca5023eaaa6b670258bedfa8dcbaf7cf@116.202.170.159:24256,68f6c52147c9423300f5b503348bbb02b229820c@51.159.153.211:26656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,54160abe97cd71abb3a83516fd8e4a47cb509fba@188.34.178.103:46656,f91eda7a7c64cebd5ad465613b15ea8e8f78aebc@194.163.164.1:26656,c36184fec2fb60bf7be775390c1cd6619c0201ef@209.126.81.240:26656,ed26b4f13a7f388064aa89e5d6419b0e78e3e94e@209.126.81.190:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,998b19ed2c580acaa2fdb5057e2930a38f041750@65.109.122.105:60556,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
