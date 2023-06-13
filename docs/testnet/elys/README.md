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
peers="136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,d3235fc7392c1f789ce8d3176b44a378a110b99c@195.3.223.26:26656,fe9268ae399ae130b43441cbfcf45f9f3146a035@65.108.75.107:33656,609c64cc50fb4ebbe7cae3347545d3950ea2c018@65.108.195.29:23656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,d907ce9285951a2a063789df2f6bd4cc86b33d53@142.132.155.178:16656,f29fe386022c463b3945955efe2b753e3bcad9a9@45.151.122.202:26656,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656,c818535eb8b383614277baf4fa661c61dbf2130d@167.114.172.204:15356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
