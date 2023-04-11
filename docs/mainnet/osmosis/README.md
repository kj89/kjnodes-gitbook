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

**live-peers** (29)
```bash
peers="71f2451869d7363ce5d91366143de63069641303@65.108.71.166:33656,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,63b4a45bb2276fe141e69ce83750a2c53f1ceeda@198.244.202.196:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,2d06b9ae6c8c359fb4ab84f7b88a0429d2095a6b@65.109.111.235:26656,ab4ea418db1c65c2517975988e2f35891637ff4a@185.111.159.235:2000,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,b3efb3700c13c2340133cfa0f1f6e942c157917c@20.229.193.38:26656,6acf893525c9c43dee575dc23fcab3aa1523ea87@74.118.136.232:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,a52bf14440a44ea8314b1e4fc2bc9917e7af5f18@65.109.52.178:26656,22c0c06ee183b47d75f8d8ec6d6c63dca90c90e5@54.156.184.104:26656,236a60841401f53c28f7609ea50ea88feb259a1e@5.9.100.51:36656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,91ed0275dcc075ba506a150b446f32ca38d805e0@195.14.6.2:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,729219c108c059824ea9a17c09d11adc99226db4@66.172.36.139:36656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
