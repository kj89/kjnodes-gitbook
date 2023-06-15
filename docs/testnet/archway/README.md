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

**live-peers** (26)
```bash
peers="6d4f2faa284b9c9625e781309b637e92627b6afd@188.40.59.225:45656,1171accc7427f2ffb76fcaa5acdef518ff42c382@178.63.104.200:45656,a14e3d92fbacf59cec76a4f3cfb9c9ff599f892b@210.16.67.34:36656,b9ba5ae75fbdee6812d1aa53ff7154ed59938cbc@57.128.151.101:26656,d1334258b592ebccb85a917aa65976b74e254a60@65.109.65.248:31656,2e4aa44eabb996442fa865ab04cbdcc46fffaf0b@65.109.155.238:27656,1413664d3cfa37c2d661f740b2b47105433f3872@65.21.139.155:34656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,5069525117c370eedfca4dbdf79a2d092c3b9687@173.249.49.123:24656,232018c513b9096a78e42ffa08f3685c4dd6a030@102.182.132.127:26656,c0e7e484e576f5aca635449a4ed41c2e7097103f@65.109.30.197:23656,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,e8d60ff778f3c27f54382ff22c7ac071f2a81027@35.223.36.227:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,280fe9d15d5399bdd549487246dac82bab0a3fe8@220.85.113.33:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,f0993a9eef446cbfed4ed78bcb4179143079a5f3@51.161.84.41:26356,7f46c5c86639e04183cea341d62c59213cdc4542@185.230.138.49:26656,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,e40e240706e5c551de40fefab1ad9fbf4a4bec23@141.94.73.39:42656,a06988c902dc5af9186ad023bc8a115453c8be7f@118.71.135.203:15656,e50d7fa6a50ac792e5df61ff621d9621e9fcc8aa@34.133.135.231:26656,6dbe7c10f3471b3f34ac7070035e3938b2b8c946@119.131.15.129:26621,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
