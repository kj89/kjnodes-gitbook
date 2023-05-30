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

**live-peers** (21)
```bash
peers="b9ba5ae75fbdee6812d1aa53ff7154ed59938cbc@57.128.151.101:26656,72ff166996ef9590879a7b7ab00b3b71529632a9@65.109.90.171:31656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,7786f708c1851dd433a03f71ec3ff74d65895de7@34.31.130.235:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,261acb73f483d1cace653cb54f7b8815f63b7e56@54.36.227.1:26656,8dfda1e1a1a690440810d8fdc19c5788ac5a4810@65.109.48.181:33656,e40e240706e5c551de40fefab1ad9fbf4a4bec23@141.94.73.39:42656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,9588fb1df2b32f50ca95c31dd92de0cd4724eac3@120.226.39.200:26656,d0a57dec1e14e60e73c9a3f89f7cf351a846bd8a@120.226.39.220:16656,5869fe239308895eed0cdfdfdf386c7642a36459@38.242.227.84:15656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,3591dd903e95c9b25618f90c4a6bda63861ab8ec@65.109.92.79:45656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,d1334258b592ebccb85a917aa65976b74e254a60@65.109.65.248:31656,0cf5d2bcc49c1acddb6b7b2bc547543ec2fbe844@34.239.246.206:26656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
