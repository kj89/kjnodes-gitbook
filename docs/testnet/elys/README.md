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
peers="136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,9e456e22da0930be2761123b7036e386a3247647@57.128.110.141:26656,919929b0162de3c3a5a4b97d7971e043679912ea@65.108.72.253:38656,7a496b16d41c366f736135b3b362a9ce80ca7dfa@161.97.167.196:38656,d9f2e28e398d42fe7ca8ed322ee168b3e867bc95@65.108.199.222:34656,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,a82ae55cc1d96af39977175624537c17f6a70995@137.184.184.159:21956,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,8dd419e6ed9117dbc793a1a59f7eca3d2c615fb3@65.109.157.236:60556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,8aa0021c45a64f736e2192f5e520c768bc9fbae2@46.101.132.190:26656,1cd3163afca4ad48949afdf6f18133fd3181e303@65.108.40.46:57656,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,fc5a323a8c57393e84902e832a75f15bd0b898b2@84.46.242.124:53656,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,78f73a31468143860a94ced6f245fc63a80742ac@75.119.146.181:38656,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,a42cc9d7134949ce2fa703c6e341a0bd9cc1984c@65.108.206.74:16656,ae7191b2b922c6a59456588c3a262df518b0d130@65.108.231.124:38656,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,3dd9e0f4f106cba1fa12c74927dd9b2ff80d80ef@65.108.200.60:33656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,b311e76cf8f66f52d144e1640471d49845c71ff9@108.175.1.36:21956,09bf7359f3d2b8ef05d328d89019204d6627f4a4@94.16.117.238:24656,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
