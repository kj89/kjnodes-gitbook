# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" width="150" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.3.1 | **Wasm**: OFF

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
peers="a42cc9d7134949ce2fa703c6e341a0bd9cc1984c@65.108.206.74:16656,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,04fe647234dc6f180783ded240ac4d023f5bfe55@170.64.174.128:21956,8aa0021c45a64f736e2192f5e520c768bc9fbae2@164.90.208.52:26656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,1cd3163afca4ad48949afdf6f18133fd3181e303@65.108.40.46:57656,8cc16cba9ccb2e1a555acb29bf53a9198ecae7ce@209.126.2.211:53656,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,d986a31287d999efa5f7962d363cec25de6c45e0@65.21.134.243:26675,b311e76cf8f66f52d144e1640471d49845c71ff9@108.175.1.36:21956,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,72de6c7078b16e378e28b44337568c33e5241953@159.65.82.47:38656,f64d9f82cc0ed53377d362fc648b959f6aa426dd@75.119.154.0:21956,734a87b41a015faf59a7d6266deea190421476c2@95.217.160.243:26656,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,ae22b82b1dc34fa0b1a64854168692310f562136@198.27.74.140:26656,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,fec2dfd0a7e0e174e90755eb60c750f5ccc43b40@199.175.98.115:53656,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,3174bb06e87392c74ad65a80c42feed816366a84@68.183.210.88:21956,85f34862d3195daaeb6853369bd0439ed1804e8a@159.89.27.173:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
