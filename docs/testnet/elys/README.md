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
peers="3891102c7aaa29dac326b6703ee7030618c92c72@89.58.16.33:26656,8851667ffc0b35d3a993fce617fd7a1a736729ad@65.21.126.180:30656,a81a21bcee82aedbf2f731b7ba26ee8dca2c61d6@54.38.193.93:26676,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,b7b044df4dc2e709972b79c04d9eb7d921e3b45f@116.202.227.117:53656,501767323c5223bfe138d916189cb5427f7e3931@104.193.254.42:27656,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
