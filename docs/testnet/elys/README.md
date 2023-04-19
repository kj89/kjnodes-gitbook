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

**live-peers** (31)
```bash
peers="01aaf7bce61622ab4f2f6cedbc57fa3aa5d3cf3c@167.235.1.101:26676,9e456e22da0930be2761123b7036e386a3247647@57.128.110.141:26656,85f34862d3195daaeb6853369bd0439ed1804e8a@159.89.27.173:21956,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,f29fe386022c463b3945955efe2b753e3bcad9a9@45.151.122.202:26656,6564e7b61aa54b00768573694f3de160961e48d9@144.91.64.15:21956,d622088b7a699cbc01591c628d7a3170329f31a4@31.220.84.183:656,ae7191b2b922c6a59456588c3a262df518b0d130@65.108.231.124:38656,ff9132635c5e1d1a287a4522bd65b28c3a17a10d@95.217.58.111:26656,42ec80cecb5fcda3d304d10b5302d824a3aeba5a@178.128.241.104:38656,501767323c5223bfe138d916189cb5427f7e3931@104.193.254.42:27656,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,f64d9f82cc0ed53377d362fc648b959f6aa426dd@75.119.154.0:21956,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,d412bdd0e608d07415eab12586ed7418a7821379@38.242.153.15:21956,e92be3a72a23a0c944633e63a67d0db1587dd98a@167.71.209.28:21956,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,04fe647234dc6f180783ded240ac4d023f5bfe55@170.64.174.128:21956,a82ae55cc1d96af39977175624537c17f6a70995@137.184.184.159:21956,3174bb06e87392c74ad65a80c42feed816366a84@68.183.210.88:21956,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,734a87b41a015faf59a7d6266deea190421476c2@95.217.160.243:26656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,3183a894566bbc5a4d55df6bf3636d2a9a942550@65.109.38.111:22056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
