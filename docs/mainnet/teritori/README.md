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
peers="ec8608f6c529a15b7a0aa9a4b40151a08dc32fe4@65.109.65.221:26796,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,63c28f10976800fd783930067d3d3a4eef358b28@173.215.85.171:20070,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,15e7d5ef19a373da5ca7aebbe3b57203f21e0a07@198.244.179.127:26656,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,722b63e6c65628b929f22013dcbcde980210cb44@176.9.127.54:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,c12c1ed98ab1f24266980c1f05ed0ca8812ca7aa@95.217.192.230:16656,942c99cb9ff717552f884639dda9f52ab66f9726@142.132.209.97:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,412afea7f33f6f91c85f8d149eff81acb6624bb3@195.201.63.87:42656,35de81a10ed992e427e6eb1d0d9ec3622d0f37fe@193.70.47.90:15956,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,409c8a2b94d3835419127521347355ae47f07dd3@5.181.190.157:27656,992b8ab3e7b0ff4025be3082a3bf72107580bd49@65.109.106.172:36656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,e8cafb5a121c9fe322e554f5a7f489b2d25abd4c@51.159.153.113:26656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,ca0d6b49b304c5f1c629809795f50440d5710b40@159.89.40.188:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
