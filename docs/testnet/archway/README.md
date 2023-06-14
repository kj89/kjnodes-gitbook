# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

Archway is an incentivized smart contract chain for Cosmos  ecosystem which gives developers a simple way to build  scalable cross-chain dapps. The developers automatically  receive rewards for their contributions to the network.

**Chain ID**: constantine-3 | **Latest Version Tag**: v1.0.0-rc.1 | **Wasm**: ON

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
peers="0ea6fb9170fb324f6862d040ccb33b282a7b1a63@85.10.193.142:26686,261acb73f483d1cace653cb54f7b8815f63b7e56@54.36.227.1:26656,c8171d5b90ea72992408f8cfcd3893256d22aabc@65.109.94.221:40656,d1334258b592ebccb85a917aa65976b74e254a60@65.109.65.248:31656,f259ea40048744ccf6efcea92579a36a4b06035e@34.29.232.227:26656,a28c1d9745dc92641eddcdb3421c34d150eb1f80@120.226.39.231:26656,294a03eabd098fe74ab1d5eac97d9fd11684d3db@120.226.39.215:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,5069525117c370eedfca4dbdf79a2d092c3b9687@173.249.49.123:24656,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,232018c513b9096a78e42ffa08f3685c4dd6a030@169.0.53.8:26656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,05413d5814b6efbb1cddec9ae240b2c638a127f5@222.106.187.14:53100,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,e8d60ff778f3c27f54382ff22c7ac071f2a81027@35.223.36.227:26656,fc4ecb28fc3665af1fed087ca76f611e090442e9@149.102.130.209:26656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,7786f708c1851dd433a03f71ec3ff74d65895de7@34.31.130.235:26656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,5ae7629c56c6b710d5129e06a836fcaab06d2cee@43.131.30.29:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
