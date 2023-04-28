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

**live-peers** (30)
```bash
peers="3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,5f15c422f789fb7c1929f859006d43c27aa61ec0@31.220.84.183:27656,72de6c7078b16e378e28b44337568c33e5241953@159.65.82.47:38656,6564e7b61aa54b00768573694f3de160961e48d9@144.91.64.15:21956,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,1cd3163afca4ad48949afdf6f18133fd3181e303@65.108.40.46:57656,42d3a20613e443087ae5aec1f1e56c0a12cf8455@135.181.60.184:46656,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,8dd419e6ed9117dbc793a1a59f7eca3d2c615fb3@65.109.157.236:60556,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,a81a21bcee82aedbf2f731b7ba26ee8dca2c61d6@54.38.193.93:26676,8d9845f7ef934ade824981b9145a26f00192b575@45.79.24.206:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,8aa0021c45a64f736e2192f5e520c768bc9fbae2@46.101.132.190:26656,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,18e2316f09d3a78ffc5d03da731fddd678279653@85.190.246.191:35656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,ae7191b2b922c6a59456588c3a262df518b0d130@65.108.231.124:38656,86987eeff225699e67a6543de3622b8a986cce28@91.183.62.162:26656,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,919929b0162de3c3a5a4b97d7971e043679912ea@65.108.72.253:38656,a82ae55cc1d96af39977175624537c17f6a70995@137.184.184.159:21956,15263a87a09f90ba71d35cbddf17ff5178e9b133@65.21.225.10:40656,d412bdd0e608d07415eab12586ed7418a7821379@38.242.153.15:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
