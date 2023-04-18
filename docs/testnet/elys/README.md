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

**live-peers** (30)
```bash
peers="b311e76cf8f66f52d144e1640471d49845c71ff9@108.175.1.36:21956,f64d9f82cc0ed53377d362fc648b959f6aa426dd@75.119.154.0:21956,0c9b0a1bc1ce796c3d9497c7400977fc5bf01379@66.94.101.52:26656,9e456e22da0930be2761123b7036e386a3247647@57.128.110.141:26656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,0977dd5475e303c99b66eaacab53c8cc28e49b05@65.109.92.79:38656,86fef1d45a77465c7b2a1dd168a792b7dd3c8f37@178.128.24.90:21956,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,01aaf7bce61622ab4f2f6cedbc57fa3aa5d3cf3c@167.235.1.101:26676,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,39d8b813be07d183c449f814aa77be8e853ace34@185.193.17.78:21956,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,eea369326c859c0167e1085dd7d540c8c8e308fb@95.217.89.202:53656,eb07af5b4c6c0a208cdd8ca0187fe5da2e2602c2@64.226.103.162:26656,919929b0162de3c3a5a4b97d7971e043679912ea@65.108.72.253:38656,d907ce9285951a2a063789df2f6bd4cc86b33d53@142.132.155.178:16656,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,42ec80cecb5fcda3d304d10b5302d824a3aeba5a@178.128.241.104:38656,563206d6e64589beb9bf233e6e489fb1d1205d38@194.146.26.36:26656,8723618f5dff7ac9b57472f90f2e86a2eb194e0a@71.236.119.108:25656,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656,a346d8325a9c3cd40e32236eb6de031d1a2d895e@95.217.107.96:26156,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,90ba88f45bae35ec15d51da7c2290df7d1890fc9@65.109.65.163:21956,fca8c62196eff28b26089bf01e9984ea808d6f06@81.0.218.194:38656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
