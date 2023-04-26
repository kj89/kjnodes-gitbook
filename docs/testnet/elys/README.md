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
peers="fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,15263a87a09f90ba71d35cbddf17ff5178e9b133@65.21.225.10:40656,7a496b16d41c366f736135b3b362a9ce80ca7dfa@161.97.167.196:38656,0c9b0a1bc1ce796c3d9497c7400977fc5bf01379@66.94.101.52:26656,01aaf7bce61622ab4f2f6cedbc57fa3aa5d3cf3c@167.235.1.101:26676,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,536f604d0aaed29669ed90bd7864fe659bfffc9c@104.152.109.134:38656,0cbf883987ff0c8e72f6c75331b2af01c8074946@51.159.223.41:26656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,3174bb06e87392c74ad65a80c42feed816366a84@68.183.210.88:21956,04fe647234dc6f180783ded240ac4d023f5bfe55@170.64.174.128:21956,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,734a87b41a015faf59a7d6266deea190421476c2@95.217.160.243:26656,8723618f5dff7ac9b57472f90f2e86a2eb194e0a@71.236.119.108:25656,72de6c7078b16e378e28b44337568c33e5241953@159.65.82.47:38656,b311e76cf8f66f52d144e1640471d49845c71ff9@108.175.1.36:21956,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,1cd3163afca4ad48949afdf6f18133fd3181e303@65.108.40.46:57656,85f34862d3195daaeb6853369bd0439ed1804e8a@159.89.27.173:21956,0977dd5475e303c99b66eaacab53c8cc28e49b05@65.109.92.79:38656,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
