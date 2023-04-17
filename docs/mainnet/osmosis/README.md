# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

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
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,f1fe0a080d561d37a94bea6022cbc0972395a0f4@65.108.121.190:2000,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,5bda7b3070d62b4ddbea815e8bea6c6e9548d17d@65.108.140.115:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,f96947493f1edd08058afaeaef8f5830cc70b8f2@15.204.197.10:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.58:26656,f25a9d4030f22a93d1b3fe1d8ed57437793bd85c@195.14.6.2:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,c0c2c6ff9e456dc31c7f697c81168267dbb49339@34.83.112.45:26656,6acf893525c9c43dee575dc23fcab3aa1523ea87@74.118.136.232:26656,024a615ea051461357046c00f67eac6300b03215@65.108.128.240:26656,1990bfb9135023ca697bbb8a8d0defb6e4669478@211.219.19.74:26656,236a60841401f53c28f7609ea50ea88feb259a1e@5.9.100.51:36656,c61bf85fd330bb702b1f13f58dd3cf83c5363bf2@149.56.26.22:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,a5ce326c6a5b78ef57d5121825e041a3cba94146@142.132.202.98:26656,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,daa8a67c0641ab7017ed9ae1616ce24bd922030d@45.143.196.110:12556,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,4b8652191ae9f4fa462ed31713f7796630486110@46.137.178.175:26656,c13125d0a7430de9448c97eea231e7dcab897df5@188.34.191.2:26756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
