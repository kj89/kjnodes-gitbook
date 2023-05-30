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

**live-peers** (25)
```bash
peers="088157569b6a372da45b1f4384dcc6f346c5a9c9@167.235.115.119:26656,da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,c0d0c9f1ef645bcf1c214b05581c9d4a4b45e97e@185.230.138.96:26656,7f46c5c86639e04183cea341d62c59213cdc4542@185.230.138.49:26656,72ff166996ef9590879a7b7ab00b3b71529632a9@65.109.90.171:31656,6450606f42fce151ca3897d28ff81a908710f9ff@77.120.115.149:26656,8b728546d0e0e422c1cd9e9f9cb6a3e67ac3e86d@184.174.37.152:15656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,fc59f8fc08a5dc9e37fc458b7fe56e900fc2cb6f@34.30.158.159:26656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,abe084eabe7d78f187b9e464cfb73879814997de@113.22.84.30:15656,05413d5814b6efbb1cddec9ae240b2c638a127f5@222.106.187.14:53100,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,a92fc11278a35f66f8a79e94e4dc3d4471a9f588@139.180.191.116:26656,8dfda1e1a1a690440810d8fdc19c5788ac5a4810@65.109.48.181:33656,272009296f322b24c1e6b120feaa716edbbbe125@65.109.158.20:26676,d82343cb3d168522c54c4ffbfd4415e9b467e806@23.88.51.134:46656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
