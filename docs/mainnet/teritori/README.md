# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/teritori.png" alt=""><figcaption></figcaption></figure>

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
peers="47a2d6c1c16f68b1c78bb9d11ef265fc961ebe00@65.108.106.172:27656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,370bf5f5b9ce655403d05753c355798288c1f120@89.245.24.92:23356,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@136.38.55.33:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,8bc43ca5dc51b7f71063df48d9f95de5da76353b@51.89.98.102:54256,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,409c8a2b94d3835419127521347355ae47f07dd3@5.181.190.157:27656,9a215b682a48dfc0435c590e945c9c2c07915ca8@65.21.170.3:26656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,46c9a9c7f0a07f813bfdd940ed506ccf00b11975@198.244.200.229:26656,63c28f10976800fd783930067d3d3a4eef358b28@173.215.85.171:20070,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,8e1e342208f400bb10677617d4f08b31a3b48877@138.201.61.159:26656,bdc0136f16ef53e5df84957549c876693345bbd6@51.159.2.19:24493,5fb621ecd0f48889939c663a2d0796403d5a2552@65.109.104.118:61156,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,412afea7f33f6f91c85f8d149eff81acb6624bb3@195.201.63.87:42656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
