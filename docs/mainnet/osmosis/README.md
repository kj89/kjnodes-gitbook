# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:29090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:29656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:29659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,12910da249bcee4cdafbef938b10b51c94c0057e@5.9.142.165:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,a5d0842d58c0fdd4ed10a39fd9c897cd168906d2@65.21.195.98:26706,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,ab3be1a8b463ac07d457dcce7af6b95cc7bae46b@46.4.79.183:26736,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,170e681516b039be361df87eb626ee81c08f07a4@157.245.115.42:26656,95dbddda671081fb433871fa612ff5291242d93d@45.67.221.200:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,9f2df25f380a7e67a92c3dc5e7c33c08555b30dc@5.9.108.19:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.71:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,6366085c975f286739a135450e262eb1e32937d3@162.19.18.137:7003,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,c5afa50cac6814f16facafb0c680871ebd62482d@184.105.162.166:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
