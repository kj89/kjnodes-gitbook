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

**live-peers** (23)
```bash
peers="e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,e40e240706e5c551de40fefab1ad9fbf4a4bec23@141.94.73.39:42656,5069525117c370eedfca4dbdf79a2d092c3b9687@173.249.49.123:24656,261acb73f483d1cace653cb54f7b8815f63b7e56@54.36.227.1:26656,13dc844645671d5da8ee81ab969d19166c3df11d@65.109.90.169:15656,a92fc11278a35f66f8a79e94e4dc3d4471a9f588@139.180.191.116:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,1192b15c204c5ac6d99b4cce775c8447b312f92b@95.217.229.113:26656,69aaa5c97f9a1316ae96c2bec6f559850f145cf7@102.182.132.127:26656,61f4a7303f2c0c942167cf3592e5922f1095b40d@95.217.107.249:26656,e8d60ff778f3c27f54382ff22c7ac071f2a81027@35.223.36.227:26656,bb5b725dfb5d2b667e8d0396b6ca5429af19ee4c@120.226.39.230:26656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,294a03eabd098fe74ab1d5eac97d9fd11684d3db@120.226.39.215:26656,c0e7e484e576f5aca635449a4ed41c2e7097103f@65.109.30.197:23656,50fff25c44a764e50e83e08da7727fb2aa345101@65.109.93.58:40656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,5fd50de776dc65d6f26e3963ccb6950642501fc4@135.181.6.226:27656,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
