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
peers="ebd3bdf55e5ebc84761840f1727e892f96a8dc0c@65.108.98.235:43256,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,15e7d5ef19a373da5ca7aebbe3b57203f21e0a07@198.244.179.127:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,5057950d34b67a67325f02949703388c4a35c1dd@154.53.59.87:19656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,c12c1ed98ab1f24266980c1f05ed0ca8812ca7aa@95.217.192.230:16656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,1f4e77295379ce0c928502d2b075157a8c8a9e64@51.83.96.150:26642,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,63c28f10976800fd783930067d3d3a4eef358b28@173.215.85.171:20070,35de81a10ed992e427e6eb1d0d9ec3622d0f37fe@193.70.47.90:15956,d29bed885306037dbe219278415025a2ea8880a4@51.159.134.79:26656,ec8608f6c529a15b7a0aa9a4b40151a08dc32fe4@65.109.65.221:26796,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,409c8a2b94d3835419127521347355ae47f07dd3@5.181.190.157:27656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,ca0d6b49b304c5f1c629809795f50440d5710b40@159.89.40.188:26656,6060a7c4f09dd7315f2c59b0c516f71e6e719a76@51.89.7.234:26642,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
