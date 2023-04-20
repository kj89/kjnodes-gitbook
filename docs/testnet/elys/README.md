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

**live-peers** (30)
```bash
peers="85f34862d3195daaeb6853369bd0439ed1804e8a@159.89.27.173:21956,72830131de8c4d80cad5e69326d7dc570be4dcf8@65.109.28.226:17656,6564e7b61aa54b00768573694f3de160961e48d9@144.91.64.15:21956,39d8b813be07d183c449f814aa77be8e853ace34@185.193.17.78:21956,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,09bf7359f3d2b8ef05d328d89019204d6627f4a4@94.16.117.238:24656,3174bb06e87392c74ad65a80c42feed816366a84@68.183.210.88:21956,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,bec0e32af9477ea6ea12f928a50bb7bbcdab05d9@161.97.167.196:38656,99c3868876955758b29aa52c26a4ad323054efeb@165.232.69.216:21956,42ec80cecb5fcda3d304d10b5302d824a3aeba5a@178.128.241.104:38656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,919929b0162de3c3a5a4b97d7971e043679912ea@65.108.72.253:38656,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,04fe647234dc6f180783ded240ac4d023f5bfe55@170.64.174.128:21956,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,ef5792644c527d083665d00d4e3cb98b316a060b@51.159.210.149:26656,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,3dd9e0f4f106cba1fa12c74927dd9b2ff80d80ef@65.108.200.60:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,ae7191b2b922c6a59456588c3a262df518b0d130@65.108.231.124:38656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
