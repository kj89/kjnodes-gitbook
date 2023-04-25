# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" width="150" alt=""><figcaption></figcaption></figure>

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
peers="b7b044df4dc2e709972b79c04d9eb7d921e3b45f@116.202.227.117:53656,78f73a31468143860a94ced6f245fc63a80742ac@75.119.146.181:38656,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,72de6c7078b16e378e28b44337568c33e5241953@159.65.82.47:38656,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,a82ae55cc1d96af39977175624537c17f6a70995@137.184.184.159:21956,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,01aaf7bce61622ab4f2f6cedbc57fa3aa5d3cf3c@167.235.1.101:26676,8aa0021c45a64f736e2192f5e520c768bc9fbae2@164.90.208.52:26656,04fe647234dc6f180783ded240ac4d023f5bfe55@170.64.174.128:21956,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,f29fe386022c463b3945955efe2b753e3bcad9a9@45.151.122.202:26656,fec2dfd0a7e0e174e90755eb60c750f5ccc43b40@199.175.98.115:53656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,b311e76cf8f66f52d144e1640471d49845c71ff9@108.175.1.36:21956,42d3a20613e443087ae5aec1f1e56c0a12cf8455@135.181.60.184:46656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,9125a59d607d276549be833b01a6e6c40f892100@141.98.112.138:53656,18842ea01d32c76aa7d1668a734ffbac231f1fe6@68.142.182.44:26656,15263a87a09f90ba71d35cbddf17ff5178e9b133@65.21.225.10:40656,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,d412bdd0e608d07415eab12586ed7418a7821379@38.242.153.15:21956,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,45e30968d5a122a5d8e8e8c36635e6efec112839@45.151.123.12:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
