# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.6.0 | **Wasm**: OFF

[Website](https://elys.network) | [Discord](https://discord.gg/R9Gr6Vh7vC) | [Twitter](https://twitter.com/elys_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/elys-testnet](https://explorer.kjnodes.com/elys-testnet)

## Public endpoints

* api: [https://elys-testnet.api.kjnodes.com](https://elys-testnet.api.kjnodes.com)
* rpc: [https://elys-testnet.rpc.kjnodes.com](https://elys-testnet.rpc.kjnodes.com)
* grpc: elys-testnet.grpc.kjnodes.com:15390

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@elys-testnet.rpc.kjnodes.com:15356
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@elys-testnet.rpc.kjnodes.com:15359
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/elys-testnet/addrbook.json > $HOME/.elys/config/addrbook.json
```

**live-peers** (10)
```bash
peers="f6480d5563172e7de0b97b666c4d503d7c4daae8@94.130.225.23:26656,d3235fc7392c1f789ce8d3176b44a378a110b99c@195.3.223.26:26656,43a905999c0a910bef08b5b5d0b5a29358200abb@65.109.175.192:38656,f3480371baafae419bfef68a64ace00dd8944bd6@65.109.92.241:10126,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,a42cc9d7134949ce2fa703c6e341a0bd9cc1984c@65.108.206.74:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,3891102c7aaa29dac326b6703ee7030618c92c72@89.58.16.33:26656,09bf7359f3d2b8ef05d328d89019204d6627f4a4@94.16.117.238:24656,ae22b82b1dc34fa0b1a64854168692310f562136@198.27.74.140:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
