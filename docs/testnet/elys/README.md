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

**live-peers** (27)
```bash
peers="9655cfb7db5ff69586359c42db7fb8dbe7555613@167.235.7.34:57656,09bf7359f3d2b8ef05d328d89019204d6627f4a4@94.16.117.238:24656,7965a8bcea48990e465a87209fdd6375f7d5f94d@64.226.90.157:26656,45e30968d5a122a5d8e8e8c36635e6efec112839@45.151.123.12:21956,d412bdd0e608d07415eab12586ed7418a7821379@38.242.153.15:21956,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,4988cbd7cac963a3a16886caa752373377ef32ff@45.67.217.151:21956,6564e7b61aa54b00768573694f3de160961e48d9@144.91.64.15:21956,54114ce29b4625d75760851e71921d27bba0032a@157.245.201.247:21956,b311e76cf8f66f52d144e1640471d49845c71ff9@108.175.1.36:21956,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,2bdb102d10ea61d369bfc65dc4614529b8c77140@45.77.46.100:21956,a82ae55cc1d96af39977175624537c17f6a70995@137.184.184.159:21956,96df985f847f5ea8903696c20d45589d0cfee134@34.135.124.66:21956,defe650a7bda2a55048832ab2e47f34e565130c9@157.230.245.237:21956,e92be3a72a23a0c944633e63a67d0db1587dd98a@167.71.209.28:21956,39d8b813be07d183c449f814aa77be8e853ace34@185.193.17.78:21956,3183a894566bbc5a4d55df6bf3636d2a9a942550@65.109.38.111:22056,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,116521cee5c0a5a48eec263fb21b88d559e89f2c@194.163.167.138:54656,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,8d9845f7ef934ade824981b9145a26f00192b575@45.79.24.206:26656,4b9789401d7c7833bbc577bae003bcfbd3656bba@65.109.28.226:17656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
