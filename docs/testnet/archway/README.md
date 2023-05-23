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

**live-peers** (24)
```bash
peers="da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,e40e240706e5c551de40fefab1ad9fbf4a4bec23@141.94.73.39:42656,b9ba5ae75fbdee6812d1aa53ff7154ed59938cbc@57.128.151.101:26656,261acb73f483d1cace653cb54f7b8815f63b7e56@54.36.227.1:26656,883e6d6e78f04be2cc7ac81f26e155de6103adf6@77.51.200.79:15656,272009296f322b24c1e6b120feaa716edbbbe125@65.109.158.20:26676,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,6450606f42fce151ca3897d28ff81a908710f9ff@77.120.115.149:26656,b6031525e988eefd03452807806f08b0e9bc3289@15.235.46.50:26656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,c8171d5b90ea72992408f8cfcd3893256d22aabc@65.109.94.221:40656,354a554c8ba12260c130cc1d5b706b10aced51ab@143.198.206.192:34656,1171accc7427f2ffb76fcaa5acdef518ff42c382@178.63.104.200:45656,2a468911e735b2dfc41e6ea4250dddf8ea1ac561@65.108.13.154:31656,abe084eabe7d78f187b9e464cfb73879814997de@1.54.176.18:15656,8650338267af660914816765c438160e6c52190f@65.109.154.182:49656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
