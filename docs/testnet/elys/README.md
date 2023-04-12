# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" width="150" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.2.3 | **Wasm**: OFF

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
peers="63914e4b213c3579bdfa7be77f6403553b8cb7d5@78.46.61.117:18656,d907ce9285951a2a063789df2f6bd4cc86b33d53@142.132.155.178:16656,f29fe386022c463b3945955efe2b753e3bcad9a9@45.151.122.202:26656,86987eeff225699e67a6543de3622b8a986cce28@91.183.62.162:26656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,d9f2e28e398d42fe7ca8ed322ee168b3e867bc95@65.108.199.222:34656,3f75a8743a5b9242cfbb57652defe540a4c1a5d4@137.184.154.151:26656,df8a39358aaa5d188f59ead77540bc96cf374f82@65.108.9.50:56656,85f34862d3195daaeb6853369bd0439ed1804e8a@159.89.27.173:21956,fc5a323a8c57393e84902e832a75f15bd0b898b2@84.46.242.124:53656,9afae60bd06970b638eb5675df19afa9d7c90c5b@213.135.246.90:26656,ee401fbe1afe6546f78c8e0f5ee0ff8922a45b06@192.3.164.17:26656,3183a894566bbc5a4d55df6bf3636d2a9a942550@65.109.38.111:22056,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,7a2ba46b795ee84cd73472039faa4b60e0228f0e@81.0.218.194:27656,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,0c9b0a1bc1ce796c3d9497c7400977fc5bf01379@66.94.101.52:26656,4988cbd7cac963a3a16886caa752373377ef32ff@45.67.217.151:21956,54114ce29b4625d75760851e71921d27bba0032a@157.245.201.247:21956,9b9aa9b87d5ef37f491899c945e869899b843ce4@65.109.26.146:53656,d412bdd0e608d07415eab12586ed7418a7821379@38.242.153.15:21956,34449aa442d5c5d98585c665be63b0ed58760d8f@182.1.232.10:21956,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,3174bb06e87392c74ad65a80c42feed816366a84@68.183.210.88:21956,62143d664e3ab84229e16fabbdea3c3dbd7defa4@157.230.32.34:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
