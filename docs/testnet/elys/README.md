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
* grpc: elys-testnet.grpc.kjnodes.com:15390

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@elys-testnet.rpc.kjnodes.com:15356
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@elys-testnet.rpc.kjnodes.com:15359
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/elys-testnet/addrbook.json > $HOME/.elys/config/addrbook.json
```

**live-peers** (29)
```bash
peers="fc5a323a8c57393e84902e832a75f15bd0b898b2@84.46.242.124:53656,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,72de6c7078b16e378e28b44337568c33e5241953@159.65.82.47:38656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,8dd419e6ed9117dbc793a1a59f7eca3d2c615fb3@65.109.157.236:60556,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,d54489a9e8c661c27483df32cade388dbc0ebe69@65.109.52.56:21656,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,72830131de8c4d80cad5e69326d7dc570be4dcf8@65.109.28.226:17656,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,01aaf7bce61622ab4f2f6cedbc57fa3aa5d3cf3c@167.235.1.101:26676,0977dd5475e303c99b66eaacab53c8cc28e49b05@65.109.92.79:38656,5f15c422f789fb7c1929f859006d43c27aa61ec0@31.220.84.183:27656,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,bfcb384007647e50e02ab6a756deec9359c631dc@136.36.73.232:26636,8aa0021c45a64f736e2192f5e520c768bc9fbae2@46.101.132.190:26656,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,734a87b41a015faf59a7d6266deea190421476c2@199.241.137.74:26656,1cd3163afca4ad48949afdf6f18133fd3181e303@65.108.40.46:57656,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,8d9845f7ef934ade824981b9145a26f00192b575@45.79.24.206:26656,ae7191b2b922c6a59456588c3a262df518b0d130@65.108.231.124:38656,3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
