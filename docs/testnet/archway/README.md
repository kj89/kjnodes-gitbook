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

**live-peers** (21)
```bash
peers="7e9827b5154a4ec4de93e277b19f77a387661664@46.4.213.198:26656,bce4a3976c39d811d50b18ed104b0d04da398591@213.239.207.175:53656,5869fe239308895eed0cdfdfdf386c7642a36459@38.242.227.84:15656,daecb368a82196424929479a369ae9ebb9c3e413@185.185.82.234:26656,c0e7e484e576f5aca635449a4ed41c2e7097103f@65.109.30.197:23656,8b96338b18c1e4a76a119fe0812c131a4e2cc96a@65.109.70.45:20656,354a554c8ba12260c130cc1d5b706b10aced51ab@143.198.206.192:34656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,11aa4b7b17ac0a3372e98d4cbf83aacd6cfbbfdd@58.187.251.205:15656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,280fe9d15d5399bdd549487246dac82bab0a3fe8@220.85.113.33:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,a14e3d92fbacf59cec76a4f3cfb9c9ff599f892b@210.16.67.34:36656,4928b2aa3a2c89d2700d3ca1192455aefde74c3c@142.132.202.87:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
