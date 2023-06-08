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
peers="3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,44f3a9ac5bfe5292edaea6e00ed2fdc4b0384573@143.198.198.204:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,fc5a323a8c57393e84902e832a75f15bd0b898b2@84.46.242.124:53656,9e456e22da0930be2761123b7036e386a3247647@57.128.110.141:26656,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,7a496b16d41c366f736135b3b362a9ce80ca7dfa@161.97.167.196:38656,e27c08c6159ebe0fb6293336ee51e68c35fe2102@31.220.84.183:60756,8723618f5dff7ac9b57472f90f2e86a2eb194e0a@71.236.119.108:25656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
