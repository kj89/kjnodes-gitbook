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
peers="6caf73a184fdec6f2b5ec43fe1218e4bd6c2bee9@178.63.52.213:36656,f075e82ca89acfbbd8ef845c95bd3d50574904f5@159.69.110.238:36656,146ec57e1c3c26d11369a1a76f97efa079901f90@159.69.201.172:25656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,24c3bd618c6c6c0df40968382e6b408429a020c7@95.217.217.253:50656,577e5876fab3d5f94a43522a58f2fe0f07445599@95.217.211.32:30656,5623331ab53459146cbb60efadf42899373f844b@37.27.6.70:26656,001933f36a6ec7c45b3c4cef073d0372daa5344d@194.163.155.84:49656,6fd64f8f811c6a2988015043fda38587ca9cf263@49.12.221.223:23656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
