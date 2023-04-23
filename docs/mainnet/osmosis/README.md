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
peers="0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,0bb96aa57bc785dd71b65690f1efc9e8f1803548@164.90.144.186:32323,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,9379a49cadb2e71d896c2d4ebd5ca394e50bf983@18.116.211.23:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,793f7aab040e364497198c9ede6e1db4fc146a34@135.181.5.219:12555,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,2ff9bc1740a721a9baeda01abee181997bb65568@142.132.140.20:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,d557fd150f11883e93c23d8fcab19ef343db8096@35.215.38.241:26656,bcef965764a0d6bc15f1476c18133d52d0ff14b6@149.202.72.166:26624,f024eadf265f72f4240e5e3ea20eac22f6695ccb@159.65.100.92:26656,9f3b6a80b462c89ba9947cfc4d9365bd42e556d9@139.144.56.204:26656,c61bf85fd330bb702b1f13f58dd3cf83c5363bf2@149.56.26.22:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,ab4ea418db1c65c2517975988e2f35891637ff4a@185.111.159.235:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
