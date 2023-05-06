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
peers="ae7191b2b922c6a59456588c3a262df518b0d130@65.108.231.124:38656,8aa0021c45a64f736e2192f5e520c768bc9fbae2@46.101.132.190:26656,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,734a87b41a015faf59a7d6266deea190421476c2@199.241.137.74:26656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,1cd3163afca4ad48949afdf6f18133fd3181e303@65.108.40.46:57656,8dd419e6ed9117dbc793a1a59f7eca3d2c615fb3@65.109.157.236:60556,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,f6480d5563172e7de0b97b666c4d503d7c4daae8@94.130.225.23:26656,563206d6e64589beb9bf233e6e489fb1d1205d38@194.146.26.36:26656,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,919929b0162de3c3a5a4b97d7971e043679912ea@65.108.72.253:38656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,f3480371baafae419bfef68a64ace00dd8944bd6@65.109.92.241:10126,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,bfcb384007647e50e02ab6a756deec9359c631dc@136.36.73.232:26636,b482200547e688be20afceefeef10716192a348b@65.109.82.112:2236,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,3d5e561dfdc0922d5b05f7616cf9a31d4fd17121@65.21.232.160:21956,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,34449aa442d5c5d98585c665be63b0ed58760d8f@182.1.235.195:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
