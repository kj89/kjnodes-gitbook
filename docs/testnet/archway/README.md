# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

Archway is an incentivized smart contract chain for Cosmos  ecosystem which gives developers a simple way to build  scalable cross-chain dapps. The developers automatically  receive rewards for their contributions to the network.

**Chain ID**: constantine-3 | **Latest Version Tag**: v0.6.0 | **Wasm**: ON

[Website](https://archway.io) | [Discord](https://discord.gg/archwayhq) | [Twitter](https://twitter.com/archwayhq)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/archway-testnet](https://explorer.kjnodes.com/archway-testnet)

## Public endpoints

* api: [https://archway-testnet.api.kjnodes.com](https://archway-testnet.api.kjnodes.com)
* rpc: [https://archway-testnet.rpc.kjnodes.com](https://archway-testnet.rpc.kjnodes.com)
* grpc: archway-testnet.grpc.kjnodes.com:15690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@archway-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@archway-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/archway-testnet/addrbook.json > $HOME/.archway/config/addrbook.json
```

**live-peers** (24)
```bash
peers="9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,124c2eaba28bac74c8d7128b923541b303b5241d@185.52.52.30:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,20355d8c6b7e8c77576982bfca148b5cbd1a538d@185.230.138.95:26656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,d82343cb3d168522c54c4ffbfd4415e9b467e806@23.88.51.134:46656,50fff25c44a764e50e83e08da7727fb2aa345101@65.109.93.58:40656,280fe9d15d5399bdd549487246dac82bab0a3fe8@220.85.113.33:26656,a14e3d92fbacf59cec76a4f3cfb9c9ff599f892b@210.16.67.34:36656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,bce4a3976c39d811d50b18ed104b0d04da398591@213.239.207.175:53656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,41246c75725b60530f56a4ef3b033ba917b9ac09@80.254.8.54:15656,857515ed6ab05e8e59f74e1050cb9e653e899cac@159.223.220.1:26656,abe084eabe7d78f187b9e464cfb73879814997de@58.187.251.205:15656,2a468911e735b2dfc41e6ea4250dddf8ea1ac561@65.108.13.154:31656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,7786f708c1851dd433a03f71ec3ff74d65895de7@34.31.130.235:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
