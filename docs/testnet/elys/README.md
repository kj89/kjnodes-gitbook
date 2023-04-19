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
peers="fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,d622088b7a699cbc01591c628d7a3170329f31a4@31.220.84.183:656,919929b0162de3c3a5a4b97d7971e043679912ea@65.108.72.253:38656,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,e92be3a72a23a0c944633e63a67d0db1587dd98a@167.71.209.28:21956,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,a065d05a896c4a2e50451aa2994b1f37e95f92c2@195.3.220.169:26656,ff9132635c5e1d1a287a4522bd65b28c3a17a10d@95.217.58.111:26656,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,d986a31287d999efa5f7962d363cec25de6c45e0@65.21.134.243:26675,f64d9f82cc0ed53377d362fc648b959f6aa426dd@75.119.154.0:21956,a82ae55cc1d96af39977175624537c17f6a70995@137.184.184.159:21956,04fe647234dc6f180783ded240ac4d023f5bfe55@170.64.174.128:21956,45e30968d5a122a5d8e8e8c36635e6efec112839@45.151.123.12:21956,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,3174bb06e87392c74ad65a80c42feed816366a84@68.183.210.88:21956,b7b044df4dc2e709972b79c04d9eb7d921e3b45f@116.202.227.117:53656,86fef1d45a77465c7b2a1dd168a792b7dd3c8f37@178.128.24.90:21956,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,ae7191b2b922c6a59456588c3a262df518b0d130@65.108.231.124:38656,3183a894566bbc5a4d55df6bf3636d2a9a942550@65.109.38.111:22056,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
