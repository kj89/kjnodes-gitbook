# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.5.4 | **Wasm**: OFF

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
peers="3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,09bf7359f3d2b8ef05d328d89019204d6627f4a4@94.16.117.238:24656,86987eeff225699e67a6543de3622b8a986cce28@91.183.62.162:26656,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,3891102c7aaa29dac326b6703ee7030618c92c72@89.58.16.33:26656,42d3a20613e443087ae5aec1f1e56c0a12cf8455@135.181.60.184:46656,8723618f5dff7ac9b57472f90f2e86a2eb194e0a@71.236.119.108:25656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,3d5e561dfdc0922d5b05f7616cf9a31d4fd17121@65.21.232.160:21956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
