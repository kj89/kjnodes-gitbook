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
peers="9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,7e9827b5154a4ec4de93e277b19f77a387661664@46.4.213.198:26656,b9ba5ae75fbdee6812d1aa53ff7154ed59938cbc@57.128.151.101:26656,8df8a64ecf0aaba1e1faee06d005aa912d578549@65.109.89.5:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,354a554c8ba12260c130cc1d5b706b10aced51ab@143.198.206.192:34656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,bce4a3976c39d811d50b18ed104b0d04da398591@213.239.207.175:53656,0cf5d2bcc49c1acddb6b7b2bc547543ec2fbe844@34.239.246.206:26656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,a14e3d92fbacf59cec76a4f3cfb9c9ff599f892b@210.16.67.34:36656,124c2eaba28bac74c8d7128b923541b303b5241d@185.52.52.30:26656,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,447644c34095606449e8f7eb34eeea2d9b7f2216@65.109.225.25:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,abe084eabe7d78f187b9e464cfb73879814997de@113.22.84.30:15656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
