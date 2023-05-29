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
peers="5f15c422f789fb7c1929f859006d43c27aa61ec0@31.220.84.183:27656,8723618f5dff7ac9b57472f90f2e86a2eb194e0a@71.236.119.108:25656,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,3891102c7aaa29dac326b6703ee7030618c92c72@89.58.16.33:26656,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
