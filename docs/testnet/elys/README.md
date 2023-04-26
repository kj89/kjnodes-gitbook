# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.4.0 | **Wasm**: OFF

[Website](https://elys.network) | [Discord](https://discord.gg/R9Gr6Vh7vC) | [Twitter](https://twitter.com/elys_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/elys-testnet](https://explorer.kjnodes.com/elys-testnet)

## Public endpoints

* api: [https://elys-testnet.api.kjnodes.com](https://elys-testnet.api.kjnodes.com)
* rpc: [https://elys-testnet.rpc.kjnodes.com](https://elys-testnet.rpc.kjnodes.com)
* grpc: elys-testnet.grpc.kjnodes.com:53090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@elys-testnet.rpc.kjnodes.com:53656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@elys-testnet.rpc.kjnodes.com:53659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/elys-testnet/addrbook.json > $HOME/.elys/config/addrbook.json
```

**live-peers** (14)
```bash
peers="86987eeff225699e67a6543de3622b8a986cce28@91.183.62.162:26656,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,78f73a31468143860a94ced6f245fc63a80742ac@75.119.146.181:38656,f29fe386022c463b3945955efe2b753e3bcad9a9@45.151.122.202:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,0977dd5475e303c99b66eaacab53c8cc28e49b05@65.109.92.79:38656,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656,71bd5f272277e707b1bec74f0ca10c7ac8472d92@209.145.60.179:26656,ae7191b2b922c6a59456588c3a262df518b0d130@65.108.231.124:38656,a81a21bcee82aedbf2f731b7ba26ee8dca2c61d6@54.38.193.93:26676,8d9845f7ef934ade824981b9145a26f00192b575@45.79.24.206:26656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,ae22b82b1dc34fa0b1a64854168692310f562136@198.27.74.140:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
