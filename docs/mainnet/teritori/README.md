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
peers="722b63e6c65628b929f22013dcbcde980210cb44@176.9.127.54:26656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,11f78b7959eb7454ed6ec2bd77a3f45491463fc8@162.19.89.8:10756,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,15e7d5ef19a373da5ca7aebbe3b57203f21e0a07@198.244.179.127:26656,63c28f10976800fd783930067d3d3a4eef358b28@173.215.85.171:20070,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,8f28518afd31a42ea81bb3232a50ab0cec4dcdf7@51.158.236.131:26656,76ac8106e8b1169f1ef28f5c45558750db85d3dc@65.108.239.241:26656,942c99cb9ff717552f884639dda9f52ab66f9726@142.132.209.97:26656,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,8e1e342208f400bb10677617d4f08b31a3b48877@138.201.61.159:26656,9a215b682a48dfc0435c590e945c9c2c07915ca8@65.21.170.3:26656,409c8a2b94d3835419127521347355ae47f07dd3@5.181.190.157:27656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@136.38.55.33:26656,ebd3bdf55e5ebc84761840f1727e892f96a8dc0c@65.108.98.235:43256,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,1f4e77295379ce0c928502d2b075157a8c8a9e64@51.83.96.150:26642"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
