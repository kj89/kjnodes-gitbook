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

**live-peers** (22)
```bash
peers="b44be28e05e9d6e67e55ed3927471c0b119c0f0d@65.109.112.29:30656,6d4f2faa284b9c9625e781309b637e92627b6afd@188.40.59.225:45656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,e40e240706e5c551de40fefab1ad9fbf4a4bec23@141.94.73.39:42656,261acb73f483d1cace653cb54f7b8815f63b7e56@54.36.227.1:26656,8df8a64ecf0aaba1e1faee06d005aa912d578549@65.109.89.5:41656,8b96338b18c1e4a76a119fe0812c131a4e2cc96a@65.109.70.45:20656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,e50d7fa6a50ac792e5df61ff621d9621e9fcc8aa@34.133.135.231:26656,b9ba5ae75fbdee6812d1aa53ff7154ed59938cbc@57.128.151.101:26656,272009296f322b24c1e6b120feaa716edbbbe125@65.109.158.20:26676,fc4ecb28fc3665af1fed087ca76f611e090442e9@149.102.130.209:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,d82343cb3d168522c54c4ffbfd4415e9b467e806@23.88.51.134:46656,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,147c1668031ee62a85bd7293a845fdcf4f7b1857@222.211.225.0:26656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,0cf5d2bcc49c1acddb6b7b2bc547543ec2fbe844@34.239.246.206:26656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
