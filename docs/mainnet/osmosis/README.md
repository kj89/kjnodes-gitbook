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
peers="82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,a52bf14440a44ea8314b1e4fc2bc9917e7af5f18@65.109.52.178:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,91ed0275dcc075ba506a150b446f32ca38d805e0@195.14.6.2:26656,bfc50a343de219d5cd744a81dab8f83911c076e5@65.109.90.96:26656,50491afd6cb3910f94ccbf7190ac32f693e76d5b@185.216.179.86:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,2904827f3ffa642bf7122d65cef27e1ab40a7346@35.74.104.174:16656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,5bda7b3070d62b4ddbea815e8bea6c6e9548d17d@65.108.140.115:26656,7e7093598012bb58b06ba9c4cc3f1802bc99f485@54.150.142.243:26656,c61bf85fd330bb702b1f13f58dd3cf83c5363bf2@149.56.26.22:26656,89d56cedcebfd6e962278a95238ef1c8abe809b7@51.79.79.68:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,c5afa50cac6814f16facafb0c680871ebd62482d@184.105.162.166:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
