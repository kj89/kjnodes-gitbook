# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="f075e82ca89acfbbd8ef845c95bd3d50574904f5@159.69.110.238:36656,fc698cb2ca4daff21f0e4c377503343cc72dd5eb@64.225.100.42:26656,af8b5486e4938c3bd9ab56fd5ee03d26857089a1@31.220.95.213:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,b71287a85b70df75e1405c6831634738e6b957ab@65.108.72.253:15656,035df68157b66066b00390d74c6d4f4895cb1ef9@95.217.155.184:26656,b4e2a2a72d058e7080c5698ebd6e5aa3e596a6a0@158.220.98.132:26656,494570d1973bfe4a4989bd7773d8607433a5ba21@89.58.45.204:60556,44a325485b1affd949a952811ceb76fb47f84e10@78.47.105.76:26656,b16f557d619c960cdc0b461085e53279d8f4e022@95.216.16.111:55656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
