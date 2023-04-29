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
peers="d986a31287d999efa5f7962d363cec25de6c45e0@65.21.134.243:26675,fc5a323a8c57393e84902e832a75f15bd0b898b2@84.46.242.124:53656,6b47fa2a93928cbe736853849887f111668d20a7@65.109.175.192:26656,5f15c422f789fb7c1929f859006d43c27aa61ec0@31.220.84.183:27656,501767323c5223bfe138d916189cb5427f7e3931@104.193.254.42:27656,3dd9e0f4f106cba1fa12c74927dd9b2ff80d80ef@65.108.200.60:32656,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,8aa0021c45a64f736e2192f5e520c768bc9fbae2@46.101.132.190:26656,8dd419e6ed9117dbc793a1a59f7eca3d2c615fb3@65.109.157.236:60556,1cd3163afca4ad48949afdf6f18133fd3181e303@65.108.40.46:57656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,a82ae55cc1d96af39977175624537c17f6a70995@137.184.184.159:21956,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,d9f2e28e398d42fe7ca8ed322ee168b3e867bc95@65.108.199.222:34656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,55b38f49cf89235b7e193b1c9880a8e77316f6a6@167.235.7.34:57656,fec2dfd0a7e0e174e90755eb60c750f5ccc43b40@199.175.98.115:53656,d907ce9285951a2a063789df2f6bd4cc86b33d53@142.132.155.178:16656,ae22b82b1dc34fa0b1a64854168692310f562136@198.27.74.140:26656,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
