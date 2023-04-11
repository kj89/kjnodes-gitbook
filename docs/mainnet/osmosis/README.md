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
peers="a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,9203fbde463bd66bb451da3de390c7d3515c2bf2@65.108.46.248:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,22c0c06ee183b47d75f8d8ec6d6c63dca90c90e5@54.156.184.104:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,3e3f8f3a9ed941600550d090900aee639abb7906@93.159.134.158:56656,63b4a45bb2276fe141e69ce83750a2c53f1ceeda@198.244.202.196:26656,c0c2c6ff9e456dc31c7f697c81168267dbb49339@34.83.112.45:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,d40d9763093fa618ce3adbdd0e6758a5b33e9ca4@173.215.85.171:20050,f00230b8831dc5747808ca951e049323d03b00e3@20.14.83.162:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.169.186:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,9987bc535ad3e14d022344deeee17e8cbe426af8@141.94.196.93:26656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,da7994c3dc691b1f24aa3811a11d90c27683a307@66.206.15.130:26656,b50f242b1cce3b4a74ef2503aee317c23b822ec3@20.229.193.38:26656,a52bf14440a44ea8314b1e4fc2bc9917e7af5f18@65.109.52.178:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,ab4ea418db1c65c2517975988e2f35891637ff4a@185.111.159.235:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
