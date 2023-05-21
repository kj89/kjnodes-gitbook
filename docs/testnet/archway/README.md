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
peers="f7a7c6bf673c201c55ecf0d249df43826293d9d4@176.9.28.41:26656,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,b9ba5ae75fbdee6812d1aa53ff7154ed59938cbc@57.128.151.101:26656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,50fff25c44a764e50e83e08da7727fb2aa345101@65.109.93.58:40656,883e6d6e78f04be2cc7ac81f26e155de6103adf6@77.51.200.79:15656,e40e240706e5c551de40fefab1ad9fbf4a4bec23@141.94.73.39:42656,8b96338b18c1e4a76a119fe0812c131a4e2cc96a@65.109.70.45:20656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,b44be28e05e9d6e67e55ed3927471c0b119c0f0d@65.109.112.29:30656,fc4ecb28fc3665af1fed087ca76f611e090442e9@149.102.130.209:36656,900950a031cb758b761198e52b07fcc17616bd76@65.21.200.54:40656,987a1359dfed5f538bd5ce54ba019a3eaedabee6@65.109.37.228:56656,abe084eabe7d78f187b9e464cfb73879814997de@1.54.176.18:15656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11756,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
