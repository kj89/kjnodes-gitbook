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
peers="d3235fc7392c1f789ce8d3176b44a378a110b99c@195.3.223.26:26656,42d3a20613e443087ae5aec1f1e56c0a12cf8455@135.181.60.184:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,55b38f49cf89235b7e193b1c9880a8e77316f6a6@167.235.7.34:57656,b7b044df4dc2e709972b79c04d9eb7d921e3b45f@116.202.227.117:53656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,3d5e561dfdc0922d5b05f7616cf9a31d4fd17121@65.21.232.160:21956,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
