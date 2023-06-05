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

**live-peers** (30)
```bash
peers="b9ba5ae75fbdee6812d1aa53ff7154ed59938cbc@57.128.151.101:26656,7a2345a2e01f27576b3463a35e3b83f666d191d9@204.93.241.110:27657,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,5869fe239308895eed0cdfdfdf386c7642a36459@38.242.227.84:15656,3591dd903e95c9b25618f90c4a6bda63861ab8ec@65.109.92.79:45656,857515ed6ab05e8e59f74e1050cb9e653e899cac@159.223.220.1:26656,7e9827b5154a4ec4de93e277b19f77a387661664@46.4.213.198:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,7e31ab391f5b5756a75dc18b5275b609c81a34ee@34.122.164.239:26656,8df8a64ecf0aaba1e1faee06d005aa912d578549@65.109.89.5:41656,85c669e01f5fca4d1ef7636a9526296a0083bb1d@15.235.193.57:26656,28c405d93963c47825ccbb2e5af915f5351e8d71@88.99.3.158:11556,124c2eaba28bac74c8d7128b923541b303b5241d@185.52.52.30:26656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,6d4f2faa284b9c9625e781309b637e92627b6afd@188.40.59.225:45656,72ff166996ef9590879a7b7ab00b3b71529632a9@65.109.90.171:31656,2e4aa44eabb996442fa865ab04cbdcc46fffaf0b@65.109.155.238:27656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,31f08ac1a5c3d4bbb9d486e1ea96b298e04625df@65.109.84.33:40656,f259ea40048744ccf6efcea92579a36a4b06035e@34.29.232.227:26656,c56bad24170d2a7fa4b6316cc08b2432cc0b0db1@5.78.80.25:26656,a14e3d92fbacf59cec76a4f3cfb9c9ff599f892b@210.16.67.34:36656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
