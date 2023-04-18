# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" width="150" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.3.1 | **Wasm**: OFF

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

**live-peers** (16)
```bash
peers="701a382e03978c54f1176145460125516b6a4672@3.144.113.232:26656,f3480371baafae419bfef68a64ace00dd8944bd6@65.109.92.241:10126,a42cc9d7134949ce2fa703c6e341a0bd9cc1984c@65.108.206.74:16656,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,0c9b0a1bc1ce796c3d9497c7400977fc5bf01379@66.94.101.52:26656,d9f2e28e398d42fe7ca8ed322ee168b3e867bc95@65.108.199.222:34656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,8723618f5dff7ac9b57472f90f2e86a2eb194e0a@71.236.119.108:25656,536f604d0aaed29669ed90bd7864fe659bfffc9c@104.152.109.134:38656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,01aaf7bce61622ab4f2f6cedbc57fa3aa5d3cf3c@167.235.1.101:26676,3183a894566bbc5a4d55df6bf3636d2a9a942550@65.109.38.111:22056,42ec80cecb5fcda3d304d10b5302d824a3aeba5a@178.128.241.104:38656,34449aa442d5c5d98585c665be63b0ed58760d8f@182.1.229.96:21956,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656,0977dd5475e303c99b66eaacab53c8cc28e49b05@65.109.92.79:38656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
