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
peers="136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,f6480d5563172e7de0b97b666c4d503d7c4daae8@94.130.225.23:26656,7a496b16d41c366f736135b3b362a9ce80ca7dfa@161.97.167.196:38656,919929b0162de3c3a5a4b97d7971e043679912ea@65.108.72.253:38656,0977dd5475e303c99b66eaacab53c8cc28e49b05@65.109.92.79:38656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,55b38f49cf89235b7e193b1c9880a8e77316f6a6@167.235.7.34:57656,3891102c7aaa29dac326b6703ee7030618c92c72@89.58.16.33:26656,8723618f5dff7ac9b57472f90f2e86a2eb194e0a@71.236.119.108:25656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
