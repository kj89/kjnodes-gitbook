# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

Archway is an incentivized smart contract chain for Cosmos  ecosystem which gives developers a simple way to build  scalable cross-chain dapps. The developers automatically  receive rewards for their contributions to the network.

**Chain ID**: constantine-3 | **Latest Version Tag**: v0.5.2 | **Wasm**: ON

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

**live-peers** (26)
```bash
peers="e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,b9ba5ae75fbdee6812d1aa53ff7154ed59938cbc@57.128.151.101:26656,c8171d5b90ea72992408f8cfcd3893256d22aabc@65.109.94.221:40656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,d1334258b592ebccb85a917aa65976b74e254a60@65.109.65.248:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,a8c07490f5aa649f5a17e0e7c3fcb93f144c6ed5@66.42.38.167:26656,3f073244fb1ae1f33de98ff7897255097ba55c3b@51.158.121.64:26656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,6b137e1df61936010ea30a354d8abd7010598e29@35.239.130.141:26656,d82343cb3d168522c54c4ffbfd4415e9b467e806@23.88.51.134:46656,7f46c5c86639e04183cea341d62c59213cdc4542@185.230.138.49:26656,68af2d5084fb7227758cf863f52804619ad2995e@194.163.166.53:15656,3591dd903e95c9b25618f90c4a6bda63861ab8ec@65.109.92.79:45656,294a03eabd098fe74ab1d5eac97d9fd11684d3db@120.226.39.215:26656,432f3efc2f96308ac92bcbbae6daaf1b4c39a3e7@75.119.154.2:15656,8df8a64ecf0aaba1e1faee06d005aa912d578549@65.109.89.5:41656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,088157569b6a372da45b1f4384dcc6f346c5a9c9@167.235.115.119:26656,11aa4b7b17ac0a3372e98d4cbf83aacd6cfbbfdd@113.22.84.30:15656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,147c1668031ee62a85bd7293a845fdcf4f7b1857@222.211.225.0:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
