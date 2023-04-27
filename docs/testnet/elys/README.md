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
peers="b7b044df4dc2e709972b79c04d9eb7d921e3b45f@116.202.227.117:53656,3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,9e456e22da0930be2761123b7036e386a3247647@57.128.110.141:26656,fc5a323a8c57393e84902e832a75f15bd0b898b2@84.46.242.124:53656,f3480371baafae419bfef68a64ace00dd8944bd6@65.109.92.241:10126,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,ae22b82b1dc34fa0b1a64854168692310f562136@198.27.74.140:26656,8dd419e6ed9117dbc793a1a59f7eca3d2c615fb3@65.109.157.236:60556,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,d9f2e28e398d42fe7ca8ed322ee168b3e867bc95@65.108.199.222:34656,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,86987eeff225699e67a6543de3622b8a986cce28@91.183.62.162:26656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,61284a4d71cd3a33771640b42f40b2afda389a1e@5.101.138.254:26656,1cd3163afca4ad48949afdf6f18133fd3181e303@65.108.40.46:57656,18842ea01d32c76aa7d1668a734ffbac231f1fe6@81.6.58.121:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,3dd9e0f4f106cba1fa12c74927dd9b2ff80d80ef@65.108.200.60:33656,d907ce9285951a2a063789df2f6bd4cc86b33d53@142.132.155.178:16656,8aa0021c45a64f736e2192f5e520c768bc9fbae2@46.101.132.190:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
