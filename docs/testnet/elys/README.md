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
peers="5f15c422f789fb7c1929f859006d43c27aa61ec0@31.220.84.183:27656,3891102c7aaa29dac326b6703ee7030618c92c72@89.58.16.33:26656,86987eeff225699e67a6543de3622b8a986cce28@91.183.62.162:26656,43a905999c0a910bef08b5b5d0b5a29358200abb@65.109.175.192:38656,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,7a496b16d41c366f736135b3b362a9ce80ca7dfa@161.97.167.196:38656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
