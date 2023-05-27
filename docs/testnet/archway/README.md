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

**live-peers** (21)
```bash
peers="9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,261acb73f483d1cace653cb54f7b8815f63b7e56@54.36.227.1:26656,ac7e3903648ea720a8c3a8fec4051f8fabbc79cf@185.185.82.252:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,1171accc7427f2ffb76fcaa5acdef518ff42c382@178.63.104.200:45656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,50fff25c44a764e50e83e08da7727fb2aa345101@65.109.93.58:40656,8dfda1e1a1a690440810d8fdc19c5788ac5a4810@65.109.48.181:33656,d82343cb3d168522c54c4ffbfd4415e9b467e806@23.88.51.134:46656,6b137e1df61936010ea30a354d8abd7010598e29@35.239.130.141:26656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,b9715f1954b3e75cb5db6b8c0d04f0a2d22ccb45@185.246.87.183:26656,abe084eabe7d78f187b9e464cfb73879814997de@113.22.84.30:15656,900950a031cb758b761198e52b07fcc17616bd76@65.21.200.54:40656,7786f708c1851dd433a03f71ec3ff74d65895de7@34.31.130.235:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
