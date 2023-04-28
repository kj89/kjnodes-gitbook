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

**live-peers** (28)
```bash
peers="ca0d6b49b304c5f1c629809795f50440d5710b40@159.89.40.188:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,35de81a10ed992e427e6eb1d0d9ec3622d0f37fe@193.70.47.90:15956,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,14e492161cc595b9da7823c27d9e5862f9e2d2c1@173.215.85.171:20030,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.168.57:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,8f28518afd31a42ea81bb3232a50ab0cec4dcdf7@51.158.236.131:26656,8e1e342208f400bb10677617d4f08b31a3b48877@138.201.61.159:26656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@136.38.55.33:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,35cdec21668ac214c74a6e45d444f6933f094bc4@136.36.73.232:26646,15e7d5ef19a373da5ca7aebbe3b57203f21e0a07@198.244.179.127:26656,992b8ab3e7b0ff4025be3082a3bf72107580bd49@65.109.106.172:36656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,e8cafb5a121c9fe322e554f5a7f489b2d25abd4c@51.159.153.113:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,623720576706fab7cf29e6a37aed39b9852d68f0@65.109.69.154:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
