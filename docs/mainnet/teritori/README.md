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
peers="ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,15e7d5ef19a373da5ca7aebbe3b57203f21e0a07@198.244.179.127:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,5fb621ecd0f48889939c663a2d0796403d5a2552@65.109.104.118:61156,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,8e1e342208f400bb10677617d4f08b31a3b48877@138.201.61.159:26656,942c99cb9ff717552f884639dda9f52ab66f9726@142.132.209.97:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.168.57:26656,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,317d9a102d4a04337c65571c18df0e98269dce87@141.94.193.12:13656,35cdec21668ac214c74a6e45d444f6933f094bc4@136.36.73.232:26646,28456ac1dded17760432c3f1d759c7d50ab6ed3e@51.250.83.54:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,ca0d6b49b304c5f1c629809795f50440d5710b40@159.89.40.188:26656,7fed06d0391518f81f56fd8fbe964558f3b7d9da@37.59.21.96:15956,623720576706fab7cf29e6a37aed39b9852d68f0@65.109.69.154:36656,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,8480ce1f929a9410567d315a5b3fc2709c2807a7@93.115.25.106:51656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@136.38.55.33:26656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,b78dd48a9d34146f04801f479a82348a19a69ab7@51.159.154.57:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
