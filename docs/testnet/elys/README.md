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
peers="fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,d907ce9285951a2a063789df2f6bd4cc86b33d53@142.132.155.178:16656,e27c08c6159ebe0fb6293336ee51e68c35fe2102@31.220.84.183:60756,fc5a323a8c57393e84902e832a75f15bd0b898b2@84.46.242.124:53656,86987eeff225699e67a6543de3622b8a986cce28@91.183.62.162:26656,d3235fc7392c1f789ce8d3176b44a378a110b99c@195.3.223.26:26656,609c64cc50fb4ebbe7cae3347545d3950ea2c018@65.108.195.29:23656,c67026e855a3ed0cb04f35445a9af48e6c5ae323@95.216.190.39:22656,a81a21bcee82aedbf2f731b7ba26ee8dca2c61d6@54.38.193.93:26676"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
