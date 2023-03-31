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

**live-peers** (10)
```bash
peers="e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,ed26b4f13a7f388064aa89e5d6419b0e78e3e94e@209.126.81.190:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,6229800969107d039254a8e6888aaeb464cda44d@167.99.186.186:26656,63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,140d07c40c964eb063d4526561ca92e8ed796b9b@65.109.82.249:29656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,c36184fec2fb60bf7be775390c1cd6619c0201ef@209.126.81.240:26656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
