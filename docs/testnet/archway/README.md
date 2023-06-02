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

**live-peers** (19)
```bash
peers="124c2eaba28bac74c8d7128b923541b303b5241d@185.52.52.30:26656,3591dd903e95c9b25618f90c4a6bda63861ab8ec@65.109.92.79:45656,5869fe239308895eed0cdfdfdf386c7642a36459@38.242.227.84:15656,a92fc11278a35f66f8a79e94e4dc3d4471a9f588@139.180.191.116:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,d82343cb3d168522c54c4ffbfd4415e9b467e806@23.88.51.134:46656,280fe9d15d5399bdd549487246dac82bab0a3fe8@220.85.113.33:26656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,20355d8c6b7e8c77576982bfca148b5cbd1a538d@185.230.138.95:26656,50fff25c44a764e50e83e08da7727fb2aa345101@65.109.93.58:40656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,7e9827b5154a4ec4de93e277b19f77a387661664@46.4.213.198:26656,99360b01621c9250e7bc09951e00551045027374@93.78.208.38:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
