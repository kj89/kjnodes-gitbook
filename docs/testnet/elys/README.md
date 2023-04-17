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

**live-peers** (29)
```bash
peers="8aa0021c45a64f736e2192f5e520c768bc9fbae2@134.122.75.207:21956,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,8d9845f7ef934ade824981b9145a26f00192b575@45.79.24.206:26656,54114ce29b4625d75760851e71921d27bba0032a@157.245.201.247:21956,e92be3a72a23a0c944633e63a67d0db1587dd98a@167.71.209.28:21956,4988cbd7cac963a3a16886caa752373377ef32ff@45.67.217.151:21956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,39d8b813be07d183c449f814aa77be8e853ace34@185.193.17.78:21956,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,2bdb102d10ea61d369bfc65dc4614529b8c77140@45.77.46.100:21956,96df985f847f5ea8903696c20d45589d0cfee134@34.135.124.66:21956,d412bdd0e608d07415eab12586ed7418a7821379@38.242.153.15:21956,6564e7b61aa54b00768573694f3de160961e48d9@144.91.64.15:21956,b311e76cf8f66f52d144e1640471d49845c71ff9@108.175.1.36:21956,3183a894566bbc5a4d55df6bf3636d2a9a942550@65.109.38.111:22056,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,df8a39358aaa5d188f59ead77540bc96cf374f82@65.108.9.50:56656,0986b43c8562b0ccac19ee7cdcfc649ae2b22190@65.109.116.204:21956,ee401fbe1afe6546f78c8e0f5ee0ff8922a45b06@192.3.164.17:26656,15263a87a09f90ba71d35cbddf17ff5178e9b133@65.21.225.10:40656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,ff9132635c5e1d1a287a4522bd65b28c3a17a10d@95.217.58.111:26656,7a2ba46b795ee84cd73472039faa4b60e0228f0e@81.0.218.194:27656,3dd9e0f4f106cba1fa12c74927dd9b2ff80d80ef@65.108.200.60:32656,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,8cc16cba9ccb2e1a555acb29bf53a9198ecae7ce@209.126.2.211:53656,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,ae7191b2b922c6a59456588c3a262df518b0d130@65.108.231.124:38656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
