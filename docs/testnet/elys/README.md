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
peers="00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,5f15c422f789fb7c1929f859006d43c27aa61ec0@31.220.84.183:27656,d3235fc7392c1f789ce8d3176b44a378a110b99c@195.3.223.26:26656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,f3480371baafae419bfef68a64ace00dd8944bd6@65.109.92.241:10126,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,98143b5dca162ba726536d07a6af6500d3e6fe1e@65.108.200.40:38656,eea369326c859c0167e1085dd7d540c8c8e308fb@95.217.89.202:53656,8851667ffc0b35d3a993fce617fd7a1a736729ad@65.21.126.180:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
