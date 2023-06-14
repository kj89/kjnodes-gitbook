# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

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
peers="7a496b16d41c366f736135b3b362a9ce80ca7dfa@161.97.167.196:38656,44f3a9ac5bfe5292edaea6e00ed2fdc4b0384573@143.198.198.204:26656,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,86987eeff225699e67a6543de3622b8a986cce28@91.183.62.162:26656,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,c67026e855a3ed0cb04f35445a9af48e6c5ae323@95.216.190.39:22656,f3480371baafae419bfef68a64ace00dd8944bd6@65.109.92.241:10126,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
