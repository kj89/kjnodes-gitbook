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
peers="e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,fb0b8dfc6d81be517e8150f532c5d5ef09e5c898@162.62.61.200:26656,7e9827b5154a4ec4de93e277b19f77a387661664@46.4.213.198:26656,e40e240706e5c551de40fefab1ad9fbf4a4bec23@141.94.73.39:42656,c0d0c9f1ef645bcf1c214b05581c9d4a4b45e97e@185.230.138.96:26656,261acb73f483d1cace653cb54f7b8815f63b7e56@54.36.227.1:26656,c0e7e484e576f5aca635449a4ed41c2e7097103f@65.109.30.197:23656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,5069525117c370eedfca4dbdf79a2d092c3b9687@173.249.49.123:24656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,e8d60ff778f3c27f54382ff22c7ac071f2a81027@35.223.36.227:26656,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,50fff25c44a764e50e83e08da7727fb2aa345101@65.109.93.58:40656,13dc844645671d5da8ee81ab969d19166c3df11d@65.109.90.169:15656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,eb70e2aaacbff6a3db3c63c9ff055d63df14c70b@47.90.189.130:26656,432f3efc2f96308ac92bcbbae6daaf1b4c39a3e7@75.119.154.2:15656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
