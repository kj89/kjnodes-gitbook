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
peers="d907ce9285951a2a063789df2f6bd4cc86b33d53@142.132.155.178:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,01aaf7bce61622ab4f2f6cedbc57fa3aa5d3cf3c@167.235.1.101:26676,f6480d5563172e7de0b97b666c4d503d7c4daae8@94.130.225.23:26656,5f15c422f789fb7c1929f859006d43c27aa61ec0@31.220.84.183:27656,a42cc9d7134949ce2fa703c6e341a0bd9cc1984c@65.108.206.74:16656,98143b5dca162ba726536d07a6af6500d3e6fe1e@65.108.200.40:38656,501767323c5223bfe138d916189cb5427f7e3931@104.193.254.42:27656,8eaad55cb53a41262a98d76fd41c2ba4b7caf08c@185.169.252.221:26656,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
