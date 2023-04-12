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
peers="c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,706c4e87fb2ab9e5fe99cad8e775eb5add88f2b2@20.77.6.8:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,91ed0275dcc075ba506a150b446f32ca38d805e0@195.14.6.2:26656,4789251e86ae993cc3e9d2ee66c338fb38ff154b@20.39.195.201:26656,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,a52bf14440a44ea8314b1e4fc2bc9917e7af5f18@65.109.52.178:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,22c0c06ee183b47d75f8d8ec6d6c63dca90c90e5@54.156.184.104:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,8a6d1179752c44d6cee9a900bbe88956486dd724@139.180.185.11:26856,c61bf85fd330bb702b1f13f58dd3cf83c5363bf2@149.56.26.22:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656,5bda7b3070d62b4ddbea815e8bea6c6e9548d17d@65.108.140.115:26656,793f7aab040e364497198c9ede6e1db4fc146a34@135.181.5.219:12555,c0c2c6ff9e456dc31c7f697c81168267dbb49339@34.83.112.45:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
