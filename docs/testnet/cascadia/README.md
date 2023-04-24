# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" width="150" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:55090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:55656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:55659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d1469dbfc3becdf0ec1640d6812793f6d33a6eda@5.9.121.55:41956,f075e82ca89acfbbd8ef845c95bd3d50574904f5@159.69.110.238:36656,3979193577e4e379c6f81b130807ed8c8d4b4d84@5.189.178.222:36656,46b554c4cddbde4adb7b10e7b6c66e46845ffc33@135.181.116.109:22796,783a3f911d98ad2eee043721a2cf47a253f58ea1@65.108.108.52:33656,046e5fdfcf33f221da082b8e4161689bcb915135@77.91.84.30:39656,df3cd1c84b2caa56f044ac19cf0267a44f2e87da@51.79.27.11:26656,893b6d4be8b527b0eb1ab4c1b2f0128945f5b241@185.213.27.91:36656,63cf1e7583eabf365856027815bc1491f2bc7939@65.108.2.41:60556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
