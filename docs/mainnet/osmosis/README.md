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
peers="c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,ea5ce509e09790c70609c8dc87ad4b19a0f98855@168.119.108.203:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656,79824a84c7bc35716839ac9c47dc05cceabf42c0@34.173.85.215:26656,3e369738cb861a252e4836d553e982988e40a41b@15.235.53.45:2000,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,a8a72dce31fdd36db889b1203d9af5fb7155e4d3@65.108.122.246:26686,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,9f2df25f380a7e67a92c3dc5e7c33c08555b30dc@5.9.108.19:26656,677ef9606ea18a13b5dbfad19493d99d7ea068f5@149.56.24.130:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,c61bf85fd330bb702b1f13f58dd3cf83c5363bf2@149.56.26.22:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,c5afa50cac6814f16facafb0c680871ebd62482d@184.105.162.166:26656,c13125d0a7430de9448c97eea231e7dcab897df5@188.34.191.2:26756,7e7093598012bb58b06ba9c4cc3f1802bc99f485@54.150.142.243:26656,8a41a35b9685a336380bc0fcd3fd4d4fc07b6101@8.218.7.106:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,6acf893525c9c43dee575dc23fcab3aa1523ea87@74.118.136.232:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,75bae7b2af60155b6687ca3e5f92010d35cb0c12@54.164.100.216:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.169.186:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
