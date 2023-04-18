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

**live-peers** (29)
```bash
peers="41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,4cef2b81f82420434c6ce0dc43ca04ad18ef773f@65.108.75.107:15656,c12c1ed98ab1f24266980c1f05ed0ca8812ca7aa@95.217.192.230:16656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,11f78b7959eb7454ed6ec2bd77a3f45491463fc8@162.19.89.8:10756,5cabaab828aea4bcc60e20c5a87b469c43023557@65.108.141.109:15656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,63c28f10976800fd783930067d3d3a4eef358b28@173.215.85.171:20070,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,5057950d34b67a67325f02949703388c4a35c1dd@154.53.59.87:19656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,15e7d5ef19a373da5ca7aebbe3b57203f21e0a07@198.244.179.127:26656,35de81a10ed992e427e6eb1d0d9ec3622d0f37fe@193.70.47.90:15956,7fed06d0391518f81f56fd8fbe964558f3b7d9da@37.59.21.96:15956,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,d40face481bc00a617d9a29c39be412a776e28c2@116.202.36.240:10656,942c99cb9ff717552f884639dda9f52ab66f9726@142.132.209.97:26656,3069b058b5ed85c3cdb2cf18fb1d255d966b53af@193.149.187.8:26656,efe721a953196d8c5f2375b86dcd54285aec565c@51.158.231.48:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
