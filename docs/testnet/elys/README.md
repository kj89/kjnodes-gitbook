# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

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
peers="ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,ae22b82b1dc34fa0b1a64854168692310f562136@198.27.74.140:26656,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,9e456e22da0930be2761123b7036e386a3247647@57.128.110.141:26656,fc5a323a8c57393e84902e832a75f15bd0b898b2@84.46.242.124:53656,7a496b16d41c366f736135b3b362a9ce80ca7dfa@161.97.167.196:38656,8d9845f7ef934ade824981b9145a26f00192b575@45.79.24.206:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,565af6e0caaedd94fe5611e5d1a6683562b5d970@89.58.16.33:38656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
