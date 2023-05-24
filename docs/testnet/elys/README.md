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
peers="0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,d9f2e28e398d42fe7ca8ed322ee168b3e867bc95@65.108.199.222:34656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,0977dd5475e303c99b66eaacab53c8cc28e49b05@65.109.92.79:38656,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656,af58431c7bf3ce9cfc4f77f5243cc40e37454b50@65.109.154.182:40656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,72de6c7078b16e378e28b44337568c33e5241953@159.65.82.47:38656,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
