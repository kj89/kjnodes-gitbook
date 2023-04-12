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
peers="63c28f10976800fd783930067d3d3a4eef358b28@173.215.85.171:20070,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,ca0d6b49b304c5f1c629809795f50440d5710b40@159.89.40.188:26656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,75d41a5ab4f826b7ba468a6c4912dbd8f4541428@178.18.251.126:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,c12c1ed98ab1f24266980c1f05ed0ca8812ca7aa@95.217.192.230:16656,11f78b7959eb7454ed6ec2bd77a3f45491463fc8@162.19.89.8:10756,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,d701007d71d071234e0375fd859a1127300a1835@107.155.109.202:26656,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,6060a7c4f09dd7315f2c59b0c516f71e6e719a76@51.89.7.234:26642,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,35de81a10ed992e427e6eb1d0d9ec3622d0f37fe@193.70.47.90:15956,e627e9bbff303c96e859de00e5deaaf5104911cd@51.15.228.89:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.168.57:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
