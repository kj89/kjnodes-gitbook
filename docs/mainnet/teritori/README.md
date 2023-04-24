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
peers="45f2d4f8ed2ef8d71a257cdeed27123f5fe3bef4@141.94.109.71:10356,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,15e7d5ef19a373da5ca7aebbe3b57203f21e0a07@198.244.179.127:26656,409c8a2b94d3835419127521347355ae47f07dd3@5.181.190.157:27656,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,efe721a953196d8c5f2375b86dcd54285aec565c@51.158.231.48:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,669470aba9778ccccd07127115dcdc30e141d7ae@65.108.232.248:33656,63c28f10976800fd783930067d3d3a4eef358b28@173.215.85.171:20070,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,5fb621ecd0f48889939c663a2d0796403d5a2552@65.109.104.118:61156,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,8f4db549de62fbb96cf4cf477e2af9c52f74a3dd@51.91.64.170:19656,7fed06d0391518f81f56fd8fbe964558f3b7d9da@37.59.21.96:15956,e3374c3d25a36f06662fa150043e5e6529d11570@88.198.32.17:31656,a8abf12f9b69a7d80999efe0aaafe5fcb28294d4@52.35.72.210:26656,35cdec21668ac214c74a6e45d444f6933f094bc4@144.202.72.17:26646,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46674"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
