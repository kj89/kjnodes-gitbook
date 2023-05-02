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
* grpc: teritori.grpc.kjnodes.com:11990

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@teritori.rpc.kjnodes.com:11956
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:11959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (30)
```bash
peers="efe721a953196d8c5f2375b86dcd54285aec565c@51.158.231.48:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,8e1e342208f400bb10677617d4f08b31a3b48877@138.201.61.159:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.201:26656,45f2d4f8ed2ef8d71a257cdeed27123f5fe3bef4@141.94.109.71:10356,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@136.38.55.33:26656,409c8a2b94d3835419127521347355ae47f07dd3@5.181.190.157:27656,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,7fed06d0391518f81f56fd8fbe964558f3b7d9da@37.59.21.96:15956,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.168.57:26656,3069b058b5ed85c3cdb2cf18fb1d255d966b53af@193.149.187.8:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,a35dc0cd0efd7e04d3334d781112bae0698a8f57@164.92.131.1:26656,8f28518afd31a42ea81bb3232a50ab0cec4dcdf7@51.158.236.131:26656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,e3374c3d25a36f06662fa150043e5e6529d11570@88.198.32.17:31656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,593b8319d1d4b1958e7daba8c3bbb56795cb59ba@146.59.81.92:51656,bdc0136f16ef53e5df84957549c876693345bbd6@51.159.2.19:24493"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
