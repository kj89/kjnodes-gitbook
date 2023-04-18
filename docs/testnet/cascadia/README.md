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
peers="6caf73a184fdec6f2b5ec43fe1218e4bd6c2bee9@178.63.52.213:36656,f075e82ca89acfbbd8ef845c95bd3d50574904f5@159.69.110.238:36656,de11c79dab6ea248fb72f9d93c2ff0eace14a5ac@94.250.201.130:26656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,603f78beb8ddc84de1f6375a792a9042f4e255c5@37.27.10.160:26656,d5ba7a2288ed176ae2e73d9ae3c0edffec3caed5@65.21.134.202:16756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656,8757ec250851234487f04466adacd3b1d37375f2@65.108.206.118:61556,5126c2904cf4d9ed9b2c6cd203fccbe3983229da@23.88.5.169:22656,1d61222b7b8e180aacebfd57fbd2d8ab95ebdc4c@65.109.93.152:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
