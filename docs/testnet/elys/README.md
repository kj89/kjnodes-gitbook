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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,f6480d5563172e7de0b97b666c4d503d7c4daae8@94.130.225.23:26656,5f15c422f789fb7c1929f859006d43c27aa61ec0@31.220.84.183:27656,7a496b16d41c366f736135b3b362a9ce80ca7dfa@161.97.167.196:38656,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,6b47fa2a93928cbe736853849887f111668d20a7@65.109.175.192:26656,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,ef5792644c527d083665d00d4e3cb98b316a060b@51.159.210.149:26656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,1cd3163afca4ad48949afdf6f18133fd3181e303@65.108.40.46:57656,ae22b82b1dc34fa0b1a64854168692310f562136@198.27.74.140:26656,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,734a87b41a015faf59a7d6266deea190421476c2@199.241.137.74:26656,8dd419e6ed9117dbc793a1a59f7eca3d2c615fb3@65.109.157.236:60556,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,8aa0021c45a64f736e2192f5e520c768bc9fbae2@46.101.132.190:26656,d986a31287d999efa5f7962d363cec25de6c45e0@65.21.134.243:26675,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,55b38f49cf89235b7e193b1c9880a8e77316f6a6@167.235.7.34:57656,a42cc9d7134949ce2fa703c6e341a0bd9cc1984c@65.108.206.74:16656,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,fec2dfd0a7e0e174e90755eb60c750f5ccc43b40@199.175.98.115:53656,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,15263a87a09f90ba71d35cbddf17ff5178e9b133@65.21.225.10:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
