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

**live-peers** (29)
```bash
peers="9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,4928b2aa3a2c89d2700d3ca1192455aefde74c3c@142.132.202.87:26656,6d4f2faa284b9c9625e781309b637e92627b6afd@188.40.59.225:45656,13dc844645671d5da8ee81ab969d19166c3df11d@65.109.90.169:15656,8b96338b18c1e4a76a119fe0812c131a4e2cc96a@65.109.70.45:20656,5069525117c370eedfca4dbdf79a2d092c3b9687@173.249.49.123:24656,232018c513b9096a78e42ffa08f3685c4dd6a030@102.182.132.127:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,61f4a7303f2c0c942167cf3592e5922f1095b40d@95.217.107.249:26656,124c2eaba28bac74c8d7128b923541b303b5241d@185.52.52.30:26656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,9e441c3d16d73b1c29081b75e0bc14131d1d2dc5@120.226.39.233:26656,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,e8d60ff778f3c27f54382ff22c7ac071f2a81027@35.223.36.227:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,1556ee238d560485d82dccafdabb36aa3325cc06@165.73.113.212:26656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,5ae7629c56c6b710d5129e06a836fcaab06d2cee@43.157.17.204:26656,3fa606cdc1ea323e19d7c09648a4f3666f0bc672@211.219.19.69:29656,fc59f8fc08a5dc9e37fc458b7fe56e900fc2cb6f@34.30.158.159:26656,1192b15c204c5ac6d99b4cce775c8447b312f92b@95.217.229.113:26656,a28c1d9745dc92641eddcdb3421c34d150eb1f80@120.226.39.231:26656,294a03eabd098fe74ab1d5eac97d9fd11684d3db@120.226.39.215:26656,0ea6fb9170fb324f6862d040ccb33b282a7b1a63@85.10.193.142:26686,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,7a73eed76c58e36ebcef9f45202464c69f1a0485@208.64.58.50:26656,09727a04d6db150cead97984720b001025cbe7d1@119.131.15.129:26621,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
