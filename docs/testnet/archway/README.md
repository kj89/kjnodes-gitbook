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

**live-peers** (30)
```bash
peers="e40e240706e5c551de40fefab1ad9fbf4a4bec23@141.94.73.39:42656,c0d0c9f1ef645bcf1c214b05581c9d4a4b45e97e@185.230.138.96:26656,63456b739a86b6dc5f38db642396b5fbe1896002@34.133.135.231:26656,8b96338b18c1e4a76a119fe0812c131a4e2cc96a@65.109.70.45:20656,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,e8d60ff778f3c27f54382ff22c7ac071f2a81027@35.223.36.227:26656,5069525117c370eedfca4dbdf79a2d092c3b9687@173.249.49.123:24656,232018c513b9096a78e42ffa08f3685c4dd6a030@102.182.132.127:26656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,28c405d93963c47825ccbb2e5af915f5351e8d71@88.99.3.158:11556,fc4ecb28fc3665af1fed087ca76f611e090442e9@149.102.130.209:26656,294a03eabd098fe74ab1d5eac97d9fd11684d3db@120.226.39.215:26656,a14e3d92fbacf59cec76a4f3cfb9c9ff599f892b@210.16.67.34:36656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,280fe9d15d5399bdd549487246dac82bab0a3fe8@220.85.113.33:26656,4928b2aa3a2c89d2700d3ca1192455aefde74c3c@142.132.202.87:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,a784ee58aa5c1fc8d16a14df642bad22383cf3af@185.246.87.183:15656,f0993a9eef446cbfed4ed78bcb4179143079a5f3@51.161.84.41:26356,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,1192b15c204c5ac6d99b4cce775c8447b312f92b@95.217.229.113:26656,0cf5d2bcc49c1acddb6b7b2bc547543ec2fbe844@34.239.246.206:26656,31f08ac1a5c3d4bbb9d486e1ea96b298e04625df@65.109.84.33:40656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,d1334258b592ebccb85a917aa65976b74e254a60@65.109.65.248:31656,7786f708c1851dd433a03f71ec3ff74d65895de7@34.31.130.235:26656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
