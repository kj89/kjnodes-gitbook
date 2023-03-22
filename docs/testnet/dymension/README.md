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
peers="ae509356c743a12259248fa8df23e42dae885e05@78.46.84.144:26656,63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,869d03182da215ae0171ac37ee69a77ed59d1a38@135.181.253.11:46656,6c0ddab56755cd010f65f1f1201d29120a2d9092@38.242.202.200:31656,e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,3928de1971d20dd711a8695d628e036d85bea1d3@65.109.85.221:3240,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,6b00d8b9ad49cc2aa8d76416613bbbb10e6f56f7@65.109.108.150:26656,44df333024cebe9b8e8361ac67feaa930ec6dc1f@65.109.85.170:54656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,adf394846dc942b1fd03f6e310eda60b5eda7848@195.201.197.4:32656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,6ee2e6550cd3510c0fc912bf0632a894148a79a7@38.242.202.174:31656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
