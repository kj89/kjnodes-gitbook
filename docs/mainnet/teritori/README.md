# Services

[installation](./installation/ "mention") [upgrade](./upgrade/ "mention") [snapshot](./snapshot/ "mention") [state-sync](./state-sync/ "mention") [useful-commands](./useful-commands/ "mention")

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
peers="a57b53a46e6f473b42a6db6e0c0f216b1611efcb@65.108.240.52:26656,7fed06d0391518f81f56fd8fbe964558f3b7d9da@37.59.21.96:15956,44b2bf9d970aece0531d3d939c5c546a7ac9201a@34.219.76.190:26656,8e1e342208f400bb10677617d4f08b31a3b48877@138.201.61.159:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27166,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.38.210:27166,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,63c28f10976800fd783930067d3d3a4eef358b28@173.215.85.171:20070,15e7d5ef19a373da5ca7aebbe3b57203f21e0a07@198.244.179.127:26656,8f28518afd31a42ea81bb3232a50ab0cec4dcdf7@51.158.236.131:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,17308ce7e097819743a01c0d30fedaa27e9f16a4@141.95.65.73:15956,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,67a266c2819ef727e51232365d98db017e82b1c3@135.181.62.108:26686,409c8a2b94d3835419127521347355ae47f07dd3@5.181.190.157:27656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,e3374c3d25a36f06662fa150043e5e6529d11570@88.198.32.17:31656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,5057950d34b67a67325f02949703388c4a35c1dd@154.53.59.87:19656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
