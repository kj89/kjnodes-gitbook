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

**live-peers** (30)
```bash
peers="526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,63c28f10976800fd783930067d3d3a4eef358b28@173.215.85.171:20070,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,15e7d5ef19a373da5ca7aebbe3b57203f21e0a07@198.244.179.127:26656,35de81a10ed992e427e6eb1d0d9ec3622d0f37fe@193.70.47.90:15956,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,4cef2b81f82420434c6ce0dc43ca04ad18ef773f@65.108.75.107:15656,c12c1ed98ab1f24266980c1f05ed0ca8812ca7aa@95.217.192.230:16656,28ffbde471fa1c1bb848ab3c8ea4ecbf5833529a@81.196.253.241:17656,412afea7f33f6f91c85f8d149eff81acb6624bb3@195.201.63.87:42656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,8480ce1f929a9410567d315a5b3fc2709c2807a7@93.115.25.106:51656,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,efe721a953196d8c5f2375b86dcd54285aec565c@51.158.231.48:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
