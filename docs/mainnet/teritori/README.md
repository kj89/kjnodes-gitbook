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
peers="412afea7f33f6f91c85f8d149eff81acb6624bb3@195.201.63.87:42656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,669470aba9778ccccd07127115dcdc30e141d7ae@65.108.232.248:33656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,e627e9bbff303c96e859de00e5deaaf5104911cd@51.15.228.89:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,15e7d5ef19a373da5ca7aebbe3b57203f21e0a07@198.244.179.127:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,7fed06d0391518f81f56fd8fbe964558f3b7d9da@37.59.21.96:15956,63c28f10976800fd783930067d3d3a4eef358b28@173.215.85.171:20070,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,8e1e342208f400bb10677617d4f08b31a3b48877@138.201.61.159:26656,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,409c8a2b94d3835419127521347355ae47f07dd3@5.181.190.157:27656,14fa46dbadd79647ebf3e5bc82326d2debc5fd52@51.159.142.254:26656,623720576706fab7cf29e6a37aed39b9852d68f0@65.109.69.154:36656,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,571084dbc97e895d11f748fccdcd1a098d8f169a@15.235.115.156:10002,992b8ab3e7b0ff4025be3082a3bf72107580bd49@65.109.106.172:36656,e8cafb5a121c9fe322e554f5a7f489b2d25abd4c@51.159.153.113:26656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,e3374c3d25a36f06662fa150043e5e6529d11570@88.198.32.17:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
