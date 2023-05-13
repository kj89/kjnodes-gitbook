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
peers="ae22b82b1dc34fa0b1a64854168692310f562136@198.27.74.140:26656,3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,55b38f49cf89235b7e193b1c9880a8e77316f6a6@167.235.7.34:57656,86987eeff225699e67a6543de3622b8a986cce28@91.183.62.162:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,fec2dfd0a7e0e174e90755eb60c750f5ccc43b40@199.175.98.115:53656,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,d3235fc7392c1f789ce8d3176b44a378a110b99c@195.3.223.26:26656,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,8723618f5dff7ac9b57472f90f2e86a2eb194e0a@71.236.119.108:25656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
