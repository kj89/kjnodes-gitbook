# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.1 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/teritori](https://explorer.kjnodes.com/teritori)

## Public endpoints

* api: [https://teritori.api.kjnodes.com](https://teritori.api.kjnodes.com)
* rpc: [https://teritori.rpc.kjnodes.com](https://teritori.rpc.kjnodes.com)
* grpc: teritori.grpc.kjnodes.com:19090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@teritori.rpc.kjnodes.com:19656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:19659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (28)
```bash
peers="82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,1f858b8cc8e18ef05de79dd470ad29ba29ddbeb7@65.108.77.106:26889,d40face481bc00a617d9a29c39be412a776e28c2@116.202.36.240:10656,8f28518afd31a42ea81bb3232a50ab0cec4dcdf7@51.158.236.131:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,fb228fa92234e9e92614078cfe1994b2252ada56@162.55.245.149:2110,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,481519b310ec2ac596fdb87da0c5f5969d51f086@51.159.152.62:26656,15e7d5ef19a373da5ca7aebbe3b57203f21e0a07@198.244.179.127:26656,2da1141f27d403e9d0cd0ecf3f02d71a3ed5031a@142.132.134.181:30553,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,63c28f10976800fd783930067d3d3a4eef358b28@173.215.85.171:20070,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,43da931d00da102c002e0a227de7258b8fb1871a@144.126.135.53:26656,669470aba9778ccccd07127115dcdc30e141d7ae@65.108.232.248:33656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,c12c1ed98ab1f24266980c1f05ed0ca8812ca7aa@95.217.192.230:16656,35de81a10ed992e427e6eb1d0d9ec3622d0f37fe@193.70.47.90:15956,317d9a102d4a04337c65571c18df0e98269dce87@141.94.193.12:13656,2aab2f1c2c9b2a74c05ff53107f53b9b5cf75e6c@195.189.96.121:51656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
