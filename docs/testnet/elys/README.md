# Services

[installation](./installation/ "mention") [upgrade](./upgrade/ "mention") [snapshot](./snapshot/ "mention") [state-sync](./state-sync/ "mention") [useful-commands](./useful-commands/ "mention")

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
peers="3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,0c9b0a1bc1ce796c3d9497c7400977fc5bf01379@66.94.101.52:26656,78f73a31468143860a94ced6f245fc63a80742ac@75.119.146.181:38656,6b47fa2a93928cbe736853849887f111668d20a7@65.109.175.192:26656,734a87b41a015faf59a7d6266deea190421476c2@95.217.160.243:26656,04fe647234dc6f180783ded240ac4d023f5bfe55@170.64.174.128:21956,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,0cbf883987ff0c8e72f6c75331b2af01c8074946@51.159.223.41:26656,f29fe386022c463b3945955efe2b753e3bcad9a9@45.151.122.202:26656,86987eeff225699e67a6543de3622b8a986cce28@91.183.62.162:26656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,d986a31287d999efa5f7962d363cec25de6c45e0@65.21.134.243:26675,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,8aa0021c45a64f736e2192f5e520c768bc9fbae2@164.90.208.52:26656,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,fc5a323a8c57393e84902e832a75f15bd0b898b2@84.46.242.124:53656,bec0e32af9477ea6ea12f928a50bb7bbcdab05d9@161.97.167.196:38656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,a82ae55cc1d96af39977175624537c17f6a70995@137.184.184.159:21956,85f34862d3195daaeb6853369bd0439ed1804e8a@159.89.27.173:21956,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,536f604d0aaed29669ed90bd7864fe659bfffc9c@104.152.109.134:38656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
