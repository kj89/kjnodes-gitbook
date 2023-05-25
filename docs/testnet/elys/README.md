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
peers="136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,af58431c7bf3ce9cfc4f77f5243cc40e37454b50@65.109.154.182:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,f6480d5563172e7de0b97b666c4d503d7c4daae8@94.130.225.23:26656,8851667ffc0b35d3a993fce617fd7a1a736729ad@65.21.126.180:30656,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,b7b044df4dc2e709972b79c04d9eb7d921e3b45f@116.202.227.117:53656,72de6c7078b16e378e28b44337568c33e5241953@159.65.82.47:38656,72830131de8c4d80cad5e69326d7dc570be4dcf8@65.109.28.226:17656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
