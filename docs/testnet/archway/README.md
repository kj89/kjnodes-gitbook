# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

Archway is an incentivized smart contract chain for Cosmos  ecosystem which gives developers a simple way to build  scalable cross-chain dapps. The developers automatically  receive rewards for their contributions to the network.

**Chain ID**: constantine-3 | **Latest Version Tag**: v1.0.0-rc.1 | **Wasm**: ON

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

**live-peers** (27)
```bash
peers="fc4ecb28fc3665af1fed087ca76f611e090442e9@149.102.130.209:26656,b9715f1954b3e75cb5db6b8c0d04f0a2d22ccb45@185.246.87.183:26656,13dc844645671d5da8ee81ab969d19166c3df11d@65.109.90.169:15656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,b6031525e988eefd03452807806f08b0e9bc3289@15.235.46.50:26656,5069525117c370eedfca4dbdf79a2d092c3b9687@173.249.49.123:24656,e8d60ff778f3c27f54382ff22c7ac071f2a81027@35.223.36.227:26656,69aaa5c97f9a1316ae96c2bec6f559850f145cf7@102.182.132.127:26656,9e441c3d16d73b1c29081b75e0bc14131d1d2dc5@120.226.39.233:26656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,1192b15c204c5ac6d99b4cce775c8447b312f92b@95.217.229.113:26656,453c95abab8d3e2d6a31f9a377f9f12cbe618c55@51.159.57.101:26656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,c56bad24170d2a7fa4b6316cc08b2432cc0b0db1@5.78.80.25:26656,3f1522525ed21a10de4d4c6dd873e715d3e9ab8e@116.98.234.21:26656,7f46c5c86639e04183cea341d62c59213cdc4542@185.230.138.49:26656,61f4a7303f2c0c942167cf3592e5922f1095b40d@95.217.107.249:26656,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,f0993a9eef446cbfed4ed78bcb4179143079a5f3@51.161.84.41:26356,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,50fff25c44a764e50e83e08da7727fb2aa345101@65.109.93.58:40656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,147c1668031ee62a85bd7293a845fdcf4f7b1857@118.113.218.78:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
