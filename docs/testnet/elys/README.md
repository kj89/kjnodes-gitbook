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
peers="8851667ffc0b35d3a993fce617fd7a1a736729ad@65.21.126.180:30656,09bf7359f3d2b8ef05d328d89019204d6627f4a4@94.16.117.238:24656,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,3891102c7aaa29dac326b6703ee7030618c92c72@89.58.16.33:26656,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,72de6c7078b16e378e28b44337568c33e5241953@159.65.82.47:38656,3d5e561dfdc0922d5b05f7616cf9a31d4fd17121@65.21.232.160:21956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
