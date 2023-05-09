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

**live-peers** (30)
```bash
peers="bfcb384007647e50e02ab6a756deec9359c631dc@136.36.73.232:26636,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,8dd419e6ed9117dbc793a1a59f7eca3d2c615fb3@65.109.157.236:60556,a42cc9d7134949ce2fa703c6e341a0bd9cc1984c@65.108.206.74:16656,563206d6e64589beb9bf233e6e489fb1d1205d38@194.146.26.36:26656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,609c64cc50fb4ebbe7cae3347545d3950ea2c018@65.108.195.29:23656,1cd3163afca4ad48949afdf6f18133fd3181e303@65.108.40.46:57656,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,d986a31287d999efa5f7962d363cec25de6c45e0@65.21.134.243:26675,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,55b38f49cf89235b7e193b1c9880a8e77316f6a6@167.235.7.34:57656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,72830131de8c4d80cad5e69326d7dc570be4dcf8@65.109.28.226:17656,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,8aa0021c45a64f736e2192f5e520c768bc9fbae2@46.101.132.190:26656,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656,8d9845f7ef934ade824981b9145a26f00192b575@45.79.24.206:26656,b482200547e688be20afceefeef10716192a348b@65.109.82.112:2236,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,ae7191b2b922c6a59456588c3a262df518b0d130@65.108.231.124:38656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
